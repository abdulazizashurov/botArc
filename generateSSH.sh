openssl genrsa -out pkey.pem 2048 &&\
openssl req -new -x509 -days 3650 -key pkey.pem -out cert.pem