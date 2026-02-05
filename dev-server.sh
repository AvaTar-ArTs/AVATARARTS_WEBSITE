#!/bin/bash
# AvatarArts Website Development Script
# Starts the development server with Node.js wrapper

echo "==========================================="
echo "AvatarArts Website Development Server"
echo "==========================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r CONFIG/requirements_lite.txt
else
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Start the Flask application
echo "Starting AvatarArts website on http://localhost:8080"
echo "Press Ctrl+C to stop the server"
cd CORE/APP/
python -c "
from app import app
print('AvatarArts Website is running on http://localhost:8080')
print('Press Ctrl+C to stop the server')
try:
    app.run(host='127.0.0.1', port=8080, debug=False)
except KeyboardInterrupt:
    print('\\nShutting down AvatarArts website...')
"