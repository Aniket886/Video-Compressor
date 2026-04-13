<div align="center">

# 🎬 CompressVideo

### A powerful, privacy-first desktop video compressor — no browser, no cloud, no limits.

Compress videos **up to 10 GB** with intelligent quality control, right on your machine.

<br/>

[![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-4.0%2B-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)](https://ffmpeg.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-555555?style=for-the-badge&logo=windows&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-6366f1?style=for-the-badge)](#)

<br/>

[**⚡ Quick Start**](#-quick-start) · [**📖 Usage Guide**](#-usage-guide) · [**🔧 Troubleshooting**](#-troubleshooting) · [**🤝 Contributing**](#-contributing)

</div>

---

## 🌟 Why CompressVideo?

| 🌐 Browser Tools | ✅ CompressVideo |
|-----------------|----------------|
| 100 MB – 1 GB file limit | **Up to 10 GB** |
| Uploads video to a server | **100% local processing** |
| Slow (limited by internet) | **Fast native FFmpeg** |
| Often show ads / paywalls | **Free & open-source** |
| No quality control | **3 quality presets + custom bitrate** |

---

## ✨ Features

- 🎯 **Smart Compression** — Automatically calculates the optimal bitrate to hit your exact target file size
- 📁 **Large File Support** — Handles videos up to 10 GB, far beyond browser-based tools
- 💡 **Size Recommendations** — Context-aware suggestions based on your video's properties
- ⚠️ **Quality Warnings** — Alerts you before compression noticeably degrades quality
- 📊 **Real-time Progress** — Live progress bar with percentage display while compressing
- ❌ **Cancel Anytime** — Safely interrupt compression mid-process
- 🔒 **Privacy First** — All processing is local; your videos never leave your machine
- 🌐 **Works Offline** — No internet required after initial setup
- 🎨 **Modern UI** — Clean card-based layout built with tkinter (no browser needed)

---

## ⚡ Quick Start

> Get up and running in under 5 minutes.

### 1 — Install FFmpeg

<details>
<summary>🪟 Windows</summary>

```powershell
# Option A: Chocolatey (recommended)
choco install ffmpeg

# Option B: Scoop
scoop install ffmpeg

# Option C: Manual — download from https://ffmpeg.org/download.html
# Extract to C:\ffmpeg, then add C:\ffmpeg\bin to your system PATH
# OR just place ffmpeg.exe in the same folder as main.py
```

</details>

<details>
<summary>🍎 macOS</summary>

```bash
brew install ffmpeg
```

</details>

<details>
<summary>🐧 Linux</summary>

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch
sudo pacman -S ffmpeg
```

</details>

Verify your install:
```bash
ffmpeg -version
```

---

### 2 — Clone the Repository

```bash
git clone https://github.com/yourusername/compressvideo.git
cd compressvideo
```

> **No extra dependencies!** The app only uses Python's standard library (`tkinter`, `subprocess`, `threading`, `pathlib`, etc.).

---

### 3 — Run the App

| OS | Command |
|----|---------|
| **Windows** | Double-click `run.bat` or run `run.bat` in Command Prompt |
| **macOS / Linux** | `chmod +x run.sh && ./run.sh` |
| **Any (Python)** | `python main.py` / `python3 main.py` |

---

## 📖 Usage Guide

### Workflow

```mermaid
flowchart LR
    A([🚀 Launch App]) --> B([📂 Select Video])
    B --> C([🔍 Review Info])
    C --> D([⚙️ Choose Settings])
    D --> E([▶ Compress])
    E --> F([✅ View Results])
    F --> B
```

### Step-by-Step

**1 — Select your video**
- Click **"Select Video"** or drag & drop a file onto the window
- Supported formats: `MP4 · MOV · AVI · MKV · WebM · FLV · WMV`

**2 — Review video information**
After loading, the app shows: file name, original size, duration, format, and resolution.

**3 — Choose compression settings**

| Option | Description |
|--------|-------------|
| 🟢 Best Quality | Minimal compression, near-original quality |
| 🔵 Good Compression | Balanced quality and size reduction |
| 🟠 Compact | Maximum compression, smallest output |
| 🎛️ Manual | Set a custom target size (50 MB – 5 GB) |

**4 — Pick an output format**

`MP4` (recommended) · `WebM` · `MOV` · *Keep Original*

**5 — Hit "Compress Video"**

The app will calculate optimal bitrate, run FFmpeg, and show a real-time progress bar.

**6 — View Results**

After completion you'll see: before/after size, percentage saved, and an **"Open Folder"** button to jump straight to the output file.

> [!TIP]
> Use **"Compress Another"** to process more files without restarting the app.

---

## 🎛️ Quality Presets

| Preset | CRF Value | File Size | Best For |
|--------|:---------:|:---------:|----------|
| **High** | 18 | Larger | Archival, professional use |
| **Balanced** | 23 | Medium | Web sharing, social media |
| **Compact** | 28 | Smallest | Email attachments, storage saving |

> **CRF (Constant Rate Factor):** Lower = better quality & larger file · Higher = smaller file & lower quality

---

## 📦 Supported Formats

| Format | Input | Output |
|--------|:-----:|:------:|
| MP4 | ✅ | ✅ |
| MOV | ✅ | ✅ |
| AVI | ✅ | ✅ |
| MKV | ✅ | ✅ |
| WebM | ✅ | ✅ |
| FLV | ✅ | — |
| WMV | ✅ | — |

---

## 💻 System Requirements

<details>
<summary>View Requirements</summary>

### Minimum
| Component | Requirement |
|-----------|-------------|
| OS | Windows 10/11 · macOS 10.14+ · Ubuntu 18.04+ |
| Python | 3.7 or later |
| FFmpeg | 4.0 or later |
| RAM | 4 GB |
| Free Storage | 2× the size of your input video |

### Recommended
| Component | Recommendation |
|-----------|----------------|
| OS | Windows 11 / macOS 13+ / Ubuntu 22.04+ |
| Python | 3.10+ |
| FFmpeg | 6.0+ |
| RAM | 8 GB or more |
| CPU | Multi-core processor |
| Storage | SSD with 20 GB+ free |

</details>

---

## 🔬 Technical Details

<details>
<summary>Architecture & Algorithm</summary>

### Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.7+ |
| GUI | `tkinter` (Python built-in) |
| Video Processing | FFmpeg (via `subprocess`) |
| Threading | Python `threading` module |
| File I/O | `pathlib`, `os` |

### Compression Algorithm

```python
# Calculate optimal bitrate to hit target file size
target_bits    = target_size_mb * 8 * 1024 * 1024
total_bitrate  = target_bits / duration_seconds

# Split between streams
video_bitrate  = total_bitrate * 0.95              # 95% → video
audio_bitrate  = min(128_000, total_bitrate * 0.05) # 5% → audio (capped at 128 kbps)
```

### FFmpeg Command

```bash
ffmpeg -i input.mp4 \
  -c:v libx264 \
  -preset medium \
  -crf 23 \
  -b:v <calculated_video_bitrate> \
  -c:a aac \
  -b:a <calculated_audio_bitrate> \
  -movflags +faststart \
  output.mp4
```

### Output File Naming
```
original_name_compressed_YYYYMMDD_HHMMSS.mp4
```

</details>

---

## 🔧 Troubleshooting

<details>
<summary>❗ "FFmpeg Not Found" Error</summary>

**Cause:** FFmpeg is not installed or not on PATH.

**Fix:**
1. Confirm install: `ffmpeg -version`
2. Check PATH:
   - Windows: `where ffmpeg` in Command Prompt
   - macOS/Linux: `which ffmpeg`
3. **Windows shortcut:** Copy `ffmpeg.exe` into the same folder as `main.py`
4. Restart terminal after changing PATH

</details>

<details>
<summary>❗ App Won't Start</summary>

**Cause:** Python not installed or wrong version.

**Fix:**
1. Check version: `python --version` (must be 3.7+)
2. Run directly to see errors: `python main.py`
3. On macOS/Linux: `python3 main.py`

</details>

<details>
<summary>❗ Compression Fails Mid-Way</summary>

**Possible causes:** Insufficient disk space, corrupted source file, or permission error.

**Fix:**
1. Ensure you have **at least 2× the video size** in free space
2. Try a different source file to rule out corruption
3. Convert to MP4 first if using an exotic format
4. Check write permissions on the output folder

</details>

<details>
<summary>❗ Progress Stuck at 0%</summary>

**Fix:**
1. Open Task Manager / Activity Monitor — check for an `ffmpeg` process
2. Try with a small test file (< 100 MB) first
3. Temporarily disable antivirus — it may be blocking FFmpeg's subprocess
4. Restart the application

</details>

<details>
<summary>❗ "Out of Memory" Error</summary>

**Fix:**
1. Close other heavy applications to free RAM
2. For videos > 5 GB, ensure at least 8 GB RAM is free
3. Use the **Compact** preset (lower memory usage)

</details>

<details>
<summary>❗ Output Video Won't Play</summary>

**Fix:**
1. Switch output format to **MP4** (most universal)
2. Use the **High** quality preset
3. Test the original source file first — it may already be corrupted
4. Try opening with [VLC Media Player](https://www.videolan.org/)

</details>

> [!NOTE]
> For issues not listed here, run `python main.py` directly in your terminal to capture the full error output, then open a [GitHub Issue](https://github.com/yourusername/compressvideo/issues) with: OS version, `python --version`, `ffmpeg -version`, and the full error text.

---

## 🗺️ Roadmap

| Version | Features |
|---------|----------|
| **v1.1** | Drag-and-drop · Recent files · Batch compression · Platform presets (YouTube, Instagram, TikTok) |
| **v1.2** | Video preview/thumbnail · Trim before compress · NVENC / QuickSync / VideoToolbox acceleration |
| **v2.0** | Advanced (custom FFmpeg options) · AI quality optimization · Multi-language support |

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

**Quick workflow:**
```bash
# 1. Fork & clone
git clone https://github.com/YOUR_USERNAME/compressvideo.git

# 2. Create your feature branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m "Add amazing feature"

# 4. Push & open a Pull Request
git push origin feature/amazing-feature
```

**Ways to help:**
- 🐛 [Report bugs](https://github.com/yourusername/compressvideo/issues/new?labels=bug)
- 💡 [Request features](https://github.com/yourusername/compressvideo/issues/new?labels=feature+request)
- 📝 Improve documentation
- 🧪 Write tests

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for full text.

---

## 🙏 Acknowledgments

- **[FFmpeg](https://ffmpeg.org/)** — The backbone of all video processing in this app
- **[Python Software Foundation](https://www.python.org/)** — For Python and the built-in `tkinter` framework

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [INSTALL.md](INSTALL.md) | Detailed installation guide for all platforms |
| [FAQ.md](FAQ.md) | Frequently asked questions |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines |
| [CHANGELOG.md](CHANGELOG.md) | Full version history |
| [COMMANDS.md](COMMANDS.md) | Command-line reference |

---

<div align="center">

**Made with ❤️ using Python & FFmpeg**

*Last Updated: April 2026*

⭐ **If you find this project helpful, please give it a star!** ⭐

</div>
