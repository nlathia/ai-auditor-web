# Makefile command: `make localhost` 
# This script launches the flask app locally

echo "\n ⏱  Launching locally (use ctrl+c to exit)..."

open http://127.0.0.1:5000
FLASK_DEBUG=1 flask run
