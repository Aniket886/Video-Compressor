# Installation Guide

Complete step-by-step installation instructions for CompressVideo on all platforms.

## Table of Contents

- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation](#linux-installation)
- [FFmpeg Installation](#ffmpeg-installation)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## Windows Installation

### Method 1: Using Pre-built Binaries (Recommended)

#### Step 1: Install FFmpeg

1. **Download FFmpeg**:
   - Visit: https://ffmpeg.org/download.html
   - Click on "Windows builds from gyan.dev"
   - Download the "ffmpeg-release-essentials.zip"

2. **Extract FFmpeg**:
   - Extract the ZIP file
   - Move the extracted folder to `C:\ffmpeg`
   - Your structure should look like:
     ```
     C:\ffmpeg\bin\
         ffmpeg.exe
         ffprobe.exe
         ...
     ```

3. **Add FFmpeg to PATH**:
   - Press `Win + X` and select "System"
   - Click "Advanced system settings" (left panel)
   - Click "Environment Variables"
   - Under "System variables", find "Path" and click "Edit"
   - Click "New" and add: `C:\ffmpeg\bin`
   - Click "OK" on all dialogs

4. **Verify Installation**:
   - Open Command Prompt (`Win + R`, type `cmd`, press Enter)
   - Run: `ffmpeg -version`
   - You should see version information

#### Step 2: Install CompressVideo

1. **Download the App**:
   ```bash
   # Using Git (if installed)
   git clone https://github.com/Aniket886/Video-Compressor.git
   
   # Or download ZIP from GitHub and extract
   ```

2. **Navigate to the folder**:
   ```bash
   cd Video-Compressor
   ```

3. **Run the application**:
   - Double-click `run.bat`
   - Or open Command Prompt and run:
     ```bash
     run.bat
     ```

### Method 2: Using Chocolatey

```powershell
# Install Chocolatey if not installed
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install FFmpeg
choco install ffmpeg

# Download and run CompressVideo
git clone https://github.com/Aniket886/Video-Compressor.git
cd Video-Compressor
run.bat
```

### Method 3: Using Scoop

```powershell
# Install Scoop if not installed
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

# Install FFmpeg
scoop install ffmpeg

# Download and run CompressVideo
git clone https://github.com/Aniket886/Video-Compressor.git
cd Video-Compressor
run.bat
```

---

## macOS Installation

### Method 1: Using Homebrew (Recommended)

#### Step 1: Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install FFmpeg

```bash
brew install ffmpeg
```

#### Step 3: Download and Run CompressVideo

```bash
# Download the app
git clone https://github.com/Aniket886/Video-Compressor.git
cd Video-Compressor

# Make run script executable
chmod +x run.sh

# Run the app
./run.sh
```

### Method 2: Using MacPorts

```bash
# Install MacPorts from https://www.macports.org/install.php

# Install FFmpeg
sudo port install ffmpeg

# Download and run CompressVideo
git clone https://github.com/Aniket886/Video-Compressor.git
cd Video-Compressor
chmod +x run.sh
./run.sh
```

### Method 3: Manual Installation

1. **Download FFmpeg**:
   - Visit: https://ffmpeg.org/download.html
   - Download macOS static build
   - Extract and move to `/usr/local/bin/`

2. **Download CompressVideo**:
   ```bash
   git clone https://github.com/Aniket886/Video-Compressor.git
   cd Video-Compressor
   python3 main.py
   ```

---

## Linux Installation

### Ubuntu/Debian

#### Step 1: Install FFmpeg

```bash
# Update package list
sudo apt update

# Install FFmpeg
sudo apt install ffmpeg

# Verify installation
ffmpeg -version
```

#### Step 2: Install Python (if not installed)

```bash
# Check Python version
python3 --version

# If not installed or < 3.7
sudo apt install python3 python3-tk
```

#### Step 3: Download and Run

```bash
# Download the app
git clone https://github.com/Aniket886/Video-Compressor.git
cd Video-Compressor

# Run
chmod +x run.sh
./run.sh
```

### Fedora

```bash
# Install FFmpeg
sudo dnf install ffmpeg

# Install Python if needed
sudo dnf install python3 python3-tkinter

# Download and run
git clone https://github.com/Aniket886/Video-Compressor.git
cd Video-Compressor
chmod +x run.sh
./run.sh
```

### Arch Linux

```bash
# Install FFmpeg
sudo pacman -S ffmpeg

# Install Python if needed
sudo pacman -S python tk

# Download and run
git clone https://github.com/Aniket886/Video-Compressor.git
cd Video-Compressor
chmod +x run.sh
./run.sh
```

---

## FFmpeg Installation Details

### What is FFmpeg?

FFmpeg is a free, open-source software project for handling video, audio, and other multimedia files. It includes:
- **ffmpeg**: The main command-line tool
- **ffprobe**: Tool for analyzing media files
- Codecs for encoding/decoding various formats

### Why is it Required?

CompressVideo is essentially a user-friendly interface for FFmpeg. All actual video processing is done by FFmpeg, which provides:
- Industry-standard compression algorithms
- Support for virtually all video formats
- Optimized encoding performance
- Reliable, battle-tested codebase

### FFmpeg Version Requirements

- **Minimum**: FFmpeg 4.0
- **Recommended**: FFmpeg 5.0 or later
- **Latest**: FFmpeg 6.x (best performance)

### Alternative: Portable FFmpeg

If you can't install FFmpeg system-wide, you can use a portable version:

#### Windows Portable

1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract to any folder (e.g., `D:\tools\ffmpeg`)
3. In CompressVideo, place `ffmpeg.exe` in the same folder as `main.py`
4. The app will automatically detect it

#### macOS/Linux Portable

1. Download static build from https://ffmpeg.org/download.html
2. Extract to a folder
3. Update PATH in your shell profile:
   ```bash
   export PATH="/path/to/ffmpeg:$PATH"
   ```

---

## Verification

After installation, verify everything is working:

### Check Python

```bash
python --version
# or
python3 --version

# Expected: Python 3.7 or later
```

### Check FFmpeg

```bash
ffmpeg -version

# Expected: Version information displayed
```

### Check tkinter

```bash
python -c "import tkinter; print(tkinter.Tcl().eval('info version'))"

# Expected: Version number (e.g., 8.6)
```

### Test CompressVideo

```bash
# Navigate to app folder
cd Video-Compressor

# Run
python main.py

# Expected: Application window opens
```

---

## Troubleshooting

### Windows-Specific Issues

#### "FFmpeg is not recognized as an internal command"

**Cause**: FFmpeg not in PATH

**Solution 1**: Add to PATH
1. Follow Step 3 in Windows Method 1
2. Restart Command Prompt

**Solution 2**: Use portable version
1. Place `ffmpeg.exe` in the same folder as `main.py`
2. The app will detect it automatically

#### "Python was not found"

**Cause**: Python not installed or not in PATH

**Solution**:
1. Install Python from https://python.org
2. During installation, check "Add Python to PATH"
3. Restart Command Prompt

#### "No module named tkinter"

**Cause**: tkinter not installed

**Solution**:
1. Reinstall Python with tkinter support
2. Or run: `pip install tk`

### macOS-Specific Issues

#### "command not found: brew"

**Cause**: Homebrew not installed

**Solution**:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then add to your shell profile:
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

#### "No module named _tkinter"

**Cause**: tkinter not installed with Python

**Solution**:
```bash
brew install python-tk
```

### Linux-Specific Issues

#### "Could not find the database of available applications"

**Cause**: Package lists outdated

**Solution**:
```bash
sudo apt update
```

#### "E: Unable to locate package ffmpeg"

**Cause**: Repository not available

**Solution**:
```bash
# Enable Universe repository
sudo add-apt-repository universe
sudo apt update
sudo apt install ffmpeg
```

### General Issues

#### "Permission denied" when running run.sh

**Solution**:
```bash
chmod +x run.sh
./run.sh
```

#### App opens but immediately closes

**Cause**: Missing FFmpeg or Python error

**Solution**:
1. Run directly to see error:
   ```bash
   python main.py
   ```
2. Check error message
3. Follow appropriate fix above

#### Slow compression

**Cause**: Using CPU encoding (software)

**Possible solutions**:
1. Close other applications
2. Use "Compact" quality preset (faster)
3. Enable hardware acceleration (if available):
   ```bash
   # For NVIDIA GPUs
   ffmpeg -hwaccel cuda -i input.mp4 ...
   
   # For Intel QuickSync
   ffmpeg -hwaccel qsv -i input.mp4 ...
   ```

---

## Getting Help

If you're still having trouble:

1. **Check the logs**: Run `python main.py` in terminal to see errors
2. **Visit the Wiki**: Check our documentation
3. **Open an Issue**: Report your problem with:
   - Operating system and version
   - Python version (`python --version`)
   - FFmpeg version (`ffmpeg -version`)
   - Complete error message
   - Steps you've already tried

---

## Quick Reference

### One-Line Installation

**Windows (with Chocolatey)**:
```powershell
choco install ffmpeg; git clone https://github.com/Aniket886/Video-Compressor.git; cd Video-Compressor; run.bat
```

**macOS (with Homebrew)**:
```bash
brew install ffmpeg && git clone https://github.com/Aniket886/Video-Compressor.git && cd Video-Compressor && chmod +x run.sh && ./run.sh
```

**Ubuntu**:
```bash
sudo apt update && sudo apt install ffmpeg python3 python3-tk -y && git clone https://github.com/Aniket886/Video-Compressor.git && cd Video-Compressor && chmod +x run.sh && ./run.sh
```

---

**Next Steps**: See [README.md](README.md) for usage instructions.
