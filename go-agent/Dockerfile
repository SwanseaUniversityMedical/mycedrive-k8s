FROM golang:1.25 AS builder

WORKDIR /app
RUN git config --global http.proxy http://192.168.10.15:8080

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

FROM alpine:latest

WORKDIR /root/

COPY --from=builder /app/main .

CMD ["./main"]