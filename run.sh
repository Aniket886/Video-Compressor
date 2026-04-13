#!/bin/bash

echo "=========================================="
echo "   CompressVideo - Desktop App"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ERROR: Python is not installed"
        echo "Please install Python 3.7 or later"
        exit 1
    fi
    PYTHON=python
else
    PYTHON=python3
fi

echo "Starting CompressVideo..."
$PYTHON main.py
