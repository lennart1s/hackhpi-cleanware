FROM golang:1.18-alpine3.15 AS builder

WORKDIR /app
COPY ${PWD} /app

RUN go mod download
RUN go build -o ./main

EXPOSE 8000

CMD ["./main"]
