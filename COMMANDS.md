# Command Reference

Quick reference for using CompressVideo from the command line.

## Basic Usage

```bash
# Windows
python main.py

# macOS / Linux
python3 main.py
```

## File Structure

```
Video-Compressor/
├── main.py          # Main application
├── run.bat          # Windows launcher script
├── run.sh           # Unix launcher script
├── requirements.txt  # Dependencies
└── docs/            # Documentation
```

## Common Commands

### Check Requirements

```bash
# Check Python version
python --version        # Windows
python3 --version      # macOS/Linux

# Check FFmpeg
ffmpeg -version

# Check if tkinter is installed
python -c "import tkinter; print(tkinter.TkVersion)"
```

### Run Application

```bash
# Direct execution
python main.py

# Using launcher (Windows)
run.bat

# Using launcher (Unix)
./run.sh

# Run with specific Python version
python3.9 main.py
```

### Development Commands

```bash
# Syntax check
python -m py_compile main.py

# Run with verbose output
python -v main.py

# Profile performance
python -m cProfile main.py
```

## Platform-Specific

### Windows

```cmd
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Run
python main.py

# Deactivate
deactivate
```

### macOS/Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Run
python main.py

# Deactivate
deactivate
```

## Troubleshooting Commands

```bash
# Check FFmpeg path
which ffmpeg          # macOS/Linux
where ffmpeg          # Windows

# Test FFmpeg
ffmpeg -f lavfi -i testsrc=duration=1:size=640x480:rate=30 test.mp4

# Check Python modules
python -c "import tkinter; import subprocess; import json; print('All modules OK')"

# List all imports in main.py
grep "^import\|^from" main.py | sort | uniq
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error |
| 2 | FFmpeg not found |
| 3 | Invalid file |
| 4 | Compression failed |

## Environment Variables

```bash
# Custom FFmpeg path
export FFMPEG_PATH=/usr/local/bin/ffmpeg

# Debug mode
export COMPRESSVIDEO_DEBUG=1

# Disable hardware acceleration
export COMPRESSVIDEO_NO_HW=1
```

## Advanced Usage

### Custom FFmpeg Arguments

Edit `main.py` and modify the `compress_video` function:

```python
# Add custom arguments
cmd = [
    self.ffmpeg_path,
    '-i', self.current_file,
    '-c:v', 'libx264',
    '-preset', 'slow',        # Change preset
    '-crf', '20',             # Change CRF
    '-c:a', 'aac',
    '-b:a', '256k',           # Change audio bitrate
    '-vf', 'scale=1920:1080', # Add video filter
    output_path
]
```

### Batch Processing Script

Create `batch.py`:

```python
import os
import subprocess

video_folder = "/path/to/videos"
output_folder = "/path/to/output"

for filename in os.listdir(video_folder):
    if filename.endswith((".mp4", ".mov", ".avi")):
        input_path = os.path.join(video_folder, filename)
        output_path = os.path.join(output_folder, f"compressed_{filename}")
        
        subprocess.run([
            "ffmpeg", "-i", input_path,
            "-c:v", "libx264", "-crf", "23",
            "-c:a", "aac", "-b:a", "128k",
            output_path
        ])
```

Run with:
```bash
python batch.py
```

## Quick Tips

1. **Use launcher scripts**: `./run.sh` or `run.bat`
2. **Check dependencies first**: Verify FFmpeg is installed
3. **Free up resources**: Close other apps before compressing large videos
4. **Test with small files first**: Verify everything works
5. **Monitor disk space**: Ensure 2x video size is available
