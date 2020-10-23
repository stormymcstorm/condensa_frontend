#!/bin/bash

export FLASK_APP=server.py

# Start flask and react servers
(trap 'kill 0' SIGINT; flask run & yarn start)