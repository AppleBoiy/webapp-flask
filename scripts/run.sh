#!/bin/bash

# Load environment variables from the specified .env file
if [ "$1" == "dev" ]; then
  export $(grep -v '^#' ./denv/.env.dev | xargs)
elif [ "$1" == "prod" ]; then
  export $(grep -v '^#' ./denv/.env.prod | xargs)
else
  echo "Usage: ./run.sh [dev|prod]"
  exit 1
fi

# Run the Flask application with Gunicorn
gunicorn -w $GUNICORN_WORKERS -b 0.0.0.0:8000 "flaskr:create_app()"