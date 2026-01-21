FROM golang:1.25 AS builder

WORKDIR /app
RUN git config --global http.proxy http://192.168.10.15:8080

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build -o main .

FROM alpine:latest

WORKDIR /root/

COPY --from=builder /app/main .

CMD ["./main"]