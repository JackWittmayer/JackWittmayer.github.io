#!/bin/bash
# Setup script to create and initialize the virtual environment

set -e

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

deactivate

echo "✓ Setup complete!"
echo ""
echo "To use the virtual environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To build posts, run:"
echo "  ./build.sh"
echo "  or"
echo "  source .venv/bin/activate && python3 build_posts.py"
