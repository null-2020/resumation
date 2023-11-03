#!/bin/bash
if [[ $1 == "debug" ]]
then
  echo "Starting app in debug mode"
  flask --app app run --debug &
  npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
else
  echo "Starting app"
  flask --app app run &
  npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
fi