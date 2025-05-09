#!/bin/bash

# Stop any running containers
echo "Stopping any running containers..."
docker compose down --remove-orphans

# Start the Chrome container
echo "Starting Chrome container..."
docker compose up -d chrome

# Wait for Chrome to be ready
echo "Waiting for Chrome to be ready..."
sleep 5

# Open the noVNC viewer in the default browser with auto-connect parameters
echo "Opening noVNC viewer in browser with auto-connect..."
xdg-open "http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password=" || open "http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password=" || start "http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password="

# Wait for browser to open
echo "Waiting for browser to open..."
sleep 3

# Start Xvfb in the background
echo "Starting Xvfb..."
Xvfb :99 -screen 0 1920x1080x24 -ac &

# Export the DISPLAY environment variable
echo "Setting DISPLAY environment variable..."
export DISPLAY=:99

# Run the tests
echo "Running tests..."
pytest main_driver.py -v