# oil_price_notify


docker build -t oil_price_notify .



docker run -d --name oil_price_notify --restart unless-stopped --env-file .env oil_price_notify