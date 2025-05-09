#!/bin/bash
set -e

# Clean up any previous X server instances
rm -f /tmp/.X*-lock /tmp/.X11-unix/X*

# Start Xvfb
Xvfb :99 -screen 0 1920x1080x24 -ac +extension GLX +render -noreset -nolisten tcp &
export DISPLAY=:99
sleep 1

# Clean Chrome user data
rm -rf /tmp/chrome-user-data
mkdir -p /tmp/chrome-user-data
chmod 777 /tmp/chrome-user-data

# Execute the Python script
exec python /app/main_driver.py
