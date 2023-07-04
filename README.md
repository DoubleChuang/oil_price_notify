# oil_price_notify

## How to use
Create a .env file, and modify the LINE_TOKEN BINANCE_API_KEY BINANCE_SECRET in the file

```
LINE_NOTIFY_TOKEN=YOUR_LINE_TOKEN
ALERT_PRICE=80
```

Build docker image from source code

```
docker build -t oil_price_notify .
```

Run image as a container

```
docker run --rm --name oil_price_notify --env-file .env oil_price_notify
```

Run by Docker Images built with GitHub Actions

```
docker run --rm --name oil_price_notify --env-file .env ghcr.io/doublechuang/oil_price_notify:5df202e
```