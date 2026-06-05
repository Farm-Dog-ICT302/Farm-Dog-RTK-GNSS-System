#!/bin/bash

#Create ssl sert and key

openssl req \
  -x509 \
  -newkey rsa:4096 \
  -nodes \
  -keyout key.pem \
  -out cert.pem \
  -days 365

read
