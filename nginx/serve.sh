#!/bin/bash


echo "Setting up nginx environment ..."
envsubst < /api_nginx.conf.template > /etc/nginx/sites-enabled/api_nginx.conf
echo "Starting nginx server ..."
exec nginx -g "daemon off;"
