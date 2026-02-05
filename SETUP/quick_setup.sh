#!/bin/bash
# AvatarArts Website Quick Setup Script
# Sets up the AvatarArts website for avatararts.org domain

set -e  # Exit on any error

echo "==========================================="
echo "AvatarArts Website Quick Setup"
echo "Setting up avatararts.org website"
echo "==========================================="

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "Checking prerequisites..."
if ! command_exists python3; then
    echo "Error: python3 is not installed"
    exit 1
fi

if ! command_exists pip; then
    echo "Error: pip is not installed"
    exit 1
fi

if ! command_exists git; then
    echo "Error: git is not installed"
    exit 1
fi

echo "All prerequisites found!"

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "Project root directory: $PROJECT_ROOT"

# Check if we're in the correct directory
if [ ! -f "$PROJECT_ROOT/CORE/APP/app.py" ]; then
    echo "Error: Could not find the AvatarArts website files in the expected location"
    echo "Expected to find CORE/APP/app.py in: $PROJECT_ROOT"
    exit 1
fi

# Ask for confirmation
echo ""
echo "This script will:"
echo "1. Create a Python virtual environment"
echo "2. Install all required dependencies"
echo "3. Create a basic configuration"
echo "4. Set up the website for local development"
echo ""
read -p "Do you want to continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Setup cancelled."
    exit 0
fi

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv "$PROJECT_ROOT/venv"
source "$PROJECT_ROOT/venv/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r "$PROJECT_ROOT/CONFIG/requirements.txt"

# Create basic configuration if it doesn't exist
if [ ! -f "$PROJECT_ROOT/CONFIG/.env" ]; then
    echo "Creating configuration file..."
    cat > "$PROJECT_ROOT/CONFIG/.env" << EOF
# AvatarArts Website Configuration
FLASK_APP=CORE.APP.app:app
FLASK_ENV=development
FLASK_DEBUG=True
AVATARARTS_SECRET_KEY=dev-secret-key-change-in-production
DATABASE_URL=sqlite:///$PROJECT_ROOT/avatararts.db
SUNO_API_KEY=
GITHUB_TOKEN=
NOCTURNEMELODIES_PATH=/Users/steven/Music/nocTurneMeLoDieS
AVATARARTS_V4_PATH=/Users/steven/Music/nocTurneMeLoDieS/github.com/ichoake/AvaTar-Arts/V4_SUNO_INTEGRATION
EOF
    echo "Configuration file created at $PROJECT_ROOT/CONFIG/.env"
    echo "Please update the configuration with your actual values"
fi

# Create upload directory if it doesn't exist
mkdir -p "$PROJECT_ROOT/STATIC/uploads"

# Create basic database if using SQLite
if [ ! -f "$PROJECT_ROOT/avatararts.db" ]; then
    echo "Creating basic database..."
    touch "$PROJECT_ROOT/avatararts.db"
fi

# Create log directory
mkdir -p "$PROJECT_ROOT/logs"

echo ""
echo "==========================================="
echo "Setup Complete!"
echo "==========================================="

echo ""
echo "To run the website locally:"
echo "1. Activate the virtual environment:"
echo "   source $PROJECT_ROOT/venv/bin/activate"
echo "2. Navigate to the project directory:"
echo "   cd $PROJECT_ROOT"
echo "3. Run the development server:"
echo "   python CORE/APP/app.py"
echo "4. Visit http://localhost:5000 in your browser"
echo ""

echo "Configuration file created at: $PROJECT_ROOT/CONFIG/.env"
echo "Please update it with your actual API keys and paths"
echo ""

echo "For production deployment, see: $PROJECT_ROOT/SETUP/setup_guide.md"
echo ""

echo "Next steps:"
echo "- Update the configuration file with your actual values"
echo "- Customize the website content in the TEMPLATES directory"
echo "- Add your own images to the STATIC/IMAGES directory"
echo "- Test the website functionality"
echo ""

echo "Need help? Check the documentation at: $PROJECT_ROOT/DOCUMENTATION/"
echo ""