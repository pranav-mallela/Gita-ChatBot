#!/bin/bash

# Build Docker image and run container
docker build -t gita-chatbot .
docker run -p 8080:8051 gita-chatbot
