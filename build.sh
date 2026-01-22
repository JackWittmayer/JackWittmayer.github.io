#!/bin/bash
# Build script that activates the virtual environment and runs the build

set -e

# Activate the virtual environment
source .venv/bin/activate

# Run the build script
python3 build_posts.py

# Deactivate the virtual environment
deactivate

echo "✓ Build complete!"
