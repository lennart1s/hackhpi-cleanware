# hackhpi-cleanware

## Vision

Make the world a better place

## Goals

1. Use as much renewable energy as possible
2. As little movment as possivle for high priority tasks

## Modules

### Weather to kilowats

1.    `docker build -t weatherkw .`
2.   `docker run -p 8000:8000 -t weatherkw`
3.    `curl -X POST "http://localhost:8000/?days=1" -H 'Content-Type: application/json' -d '{"lat":"51.50","long":"-0.118","capacity":"23"}' -v `

Therefore, supply `lat,lang,capacity` to the endpoint to get stats for the location. `days=x` will output the forecast for x days, by default 4. Check the return status code for `200`, otherwise blame the user.

![image](https://user-images.githubusercontent.com/98784263/159130539-14998162-afcc-4fed-9fee-d6ca518ee9f5.png)

## Hasso hat's!🤑

