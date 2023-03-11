#!/bin/bash


echo "Setting up nginx environment ..."
./env_setup.sh

echo "Starting nginx server ..."
exec nginx -g "daemon off;"
