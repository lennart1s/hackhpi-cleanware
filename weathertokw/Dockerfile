FROM golang:1.18-alpine3.15 AS builder

WORKDIR /app
COPY ${PWD} /app

ENV api_key=92IQL3i8robcMWhbStuIxk9EZvY7nXsdJPDYjOOB

RUN go mod download
RUN go build -o ./main

EXPOSE 8000

CMD ["./main"]
