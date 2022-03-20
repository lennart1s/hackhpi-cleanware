# hackhpi-cleanware

## Vision

Make the world a better place

## Goals

1. Use as much renewable energy as possible
2. As little movment as possivle for high priority tasks

## Modules

Run the project:

1. `git clone https://github.com/lennart1s/hackhpi-cleanware/`
2. `sudo docker-compose up`

### Weather to kilowats

1.    `docker build -t weatherkw .`
2.   `docker run -p 8000:8000 -t weatherkw -d`
3.    `curl -X POST "http://localhost:8000/?days=1" -H 'Content-Type: application/json' -d '{"lat":"51.50","long":"-0.118","capacity":"23","turbines":"10"}' -v `

Therefore, supply `lat,lang,capacity,turbines` to the endpoint to get stats for the location. `days=x` will output the forecast for x days, by default 4. Check the return status code for `200`, otherwise blame the user.



## Hasso hat's!🤑

