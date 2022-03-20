package main

import (
	"encoding/json"
	"fmt"
	"io"
	"math"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"
)

var api_key string = os.Getenv("api_key")

type WeatherHandler struct {
	rng *rand.Rand
}

type Response struct {
	StartTime int64     `json:"startime"`
	Kilowatts []float64 `json:"kw"`
}

type HTTPError struct {
	Error string `json:"error"`
	Kind  string `json:"kind"`
}

type SolarRadiationAPIResponse struct {
	Inputs struct {
		Dataset        string `json:"dataset"`
		Timeframe      string `json:"timeframe"`
		Lat            string `json:"lat"`
		Lon            string `json:"lon"`
		SystemCapacity string `json:"system_capacity"`
		Azimuth        string `json:"azimuth"`
		Tilt           string `json:"tilt"`
		ArrayType      string `json:"array_type"`
		ModuleType     string `json:"module_type"`
		Losses         string `json:"losses"`
	} `json:"inputs"`
	Errors   []interface{} `json:"errors"`
	Warnings []interface{} `json:"warnings"`
	Version  string        `json:"version"`
	SscInfo  struct {
		Version int    `json:"version"`
		Build   string `json:"build"`
	} `json:"ssc_info"`
	StationInfo struct {
		Lat               float64 `json:"lat"`
		Lon               float64 `json:"lon"`
		Elev              float64 `json:"elev"`
		Tz                float64 `json:"tz"`
		Location          string  `json:"location"`
		City              string  `json:"city"`
		State             string  `json:"state"`
		SolarResourceFile string  `json:"solar_resource_file"`
		Distance          int     `json:"distance"`
	} `json:"station_info"`
	Outputs struct {
		AcMonthly      []float64 `json:"ac_monthly"`
		PoaMonthly     []float64 `json:"poa_monthly"`
		SolradMonthly  []float64 `json:"solrad_monthly"`
		DcMonthly      []float64 `json:"dc_monthly"`
		AcAnnual       float64   `json:"ac_annual"`
		SolradAnnual   float64   `json:"solrad_annual"`
		CapacityFactor float64   `json:"capacity_factor"`
		Ac             []float64 `json:"ac"`
		Poa            []float64 `json:"poa"`
		Dn             []float64 `json:"dn"`
		Dc             []float64 `json:"dc"`
		Df             []float64 `json:"df"`
		Tamb           []float64 `json:"tamb"`
		Tcell          []float64 `json:"tcell"`
		Wspd           []float64 `json:"wspd"`
	} `json:"outputs"`
}

type Request struct {
	Lat      string `json:"lat"`
	Long     string `json:"long"`
	Capacity string `json:"capacity"`
	Turbines string `json:"turbines"`
}

func (wh *WeatherHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method != http.MethodPost {
		fmt.Fprint(w, "{\"error\":\"Invalid method, use POST\",\"kind\":\"\"}\n")
		return
	}

	requestData := &Request{}
	err := json.NewDecoder(r.Body).Decode(requestData)

	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode(HTTPError{
			Error: err.Error(), Kind: "decoding incoming request json",
		})
		return
	}

	client := &http.Client{}
	req, err := http.NewRequest("GET", "https://developer.nrel.gov/api/pvwatts/v6.json?", nil)

	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		json.NewEncoder(w).Encode(HTTPError{
			Error: err.Error(), Kind: "creating request",
		})
		return
	}

	query := req.URL.Query()

	query.Add("api_key", api_key)
	query.Add("dataset", "intl")
	query.Add("format", "json")
	query.Add("timeframe", "hourly")
	query.Add("lat", requestData.Lat)
	query.Add("lon", requestData.Long)
	query.Add("losses", "15")
	query.Add("module_type", "0")
	query.Add("array_type", "1")
	query.Add("tilt", "40")
	query.Add("azimuth", "180")
	query.Add("system_capacity", requestData.Capacity)

	req.URL.RawQuery = query.Encode()
	resp, err := client.Do(req)

	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		json.NewEncoder(w).Encode(HTTPError{
			Error: err.Error(), Kind: "sending request",
		})
		return
	}

	if resp.StatusCode != http.StatusOK {
		bodyBytes, _ := io.ReadAll(resp.Body)
		w.WriteHeader(http.StatusInternalServerError)
		json.NewEncoder(w).Encode(HTTPError{
			Error: string(bodyBytes), Kind: "request to third party data source",
		})
		return
	}

	responseData := &SolarRadiationAPIResponse{}
	err = json.NewDecoder(resp.Body).Decode(responseData)

	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		json.NewEncoder(w).Encode(HTTPError{
			Error: err.Error(), Kind: "decoding json response",
		})
		return
	}

	days := r.URL.Query().Get("days")
	val, err := strconv.Atoi(days)

	// set default in case of error
	if days == "" || err != nil || val < 0 {
		val = 4
	}

	responseTime := time.Now().Unix()

	kw := make([]float64, val*24)
	l1, _ := strconv.ParseFloat(requestData.Lat, 64)
	l2, _ := strconv.ParseFloat(requestData.Long, 64)

	mu := math.Abs(l1 - l2)
	sigma := math.Max(l1, l2) / math.Min(l1, l2)
	sigma = sigma * sigma
	turbines, _ := strconv.Atoi(requestData.Turbines)

	for i := 0; i < val*24; i++ {
		kw[i] = math.Abs(wh.rng.NormFloat64()*math.Sqrt(sigma)+mu)*float64(turbines) + responseData.Outputs.Ac[i]
	}

	json.NewEncoder(w).Encode(Response{
		StartTime: responseTime - (responseTime % (60 * 60 * 24)),
		Kilowatts: kw,
	})
}

func main() {
	http.Handle("/", &WeatherHandler{
		rand.New(rand.NewSource(time.Now().Unix())),
	})
	http.ListenAndServe(":8000", nil)
}
