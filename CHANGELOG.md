# Changelog

All notable changes to CompressVideo will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Drag and drop file support
- Batch compression for multiple files
- Hardware acceleration support (NVENC, QuickSync)
- Video trimming before compression
- Preset profiles (YouTube, Instagram, TikTok)
- Multi-language support
- Custom FFmpeg options
- Video preview/thumbnail

## [1.0.0] - 2024-04-14

### Added
- Initial desktop application release
- Modern tkinter-based GUI with card layout
- Smart video compression using FFmpeg
- Support for videos up to 10GB
- Intelligent size recommendations
- Quality impact warnings
- Real-time progress tracking
- Multiple output formats (MP4, MOV, WebM)
- Three quality presets (High, Balanced, Compact)
- Cross-platform support (Windows, macOS, Linux)
- Standalone operation (no browser needed)
- Privacy-first design (no data sent to servers)
- Cancel operation functionality
- Before/after size comparison
- One-click folder access
- Comprehensive error handling

### Technical
- FFmpeg integration via subprocess
- Multi-threaded UI for responsiveness
- Automatic bitrate calculation: `target_bitrate = (target_size * 8) / duration`
- H.264 (libx264) video codec with AAC audio
- CRF-based quality control (18, 23, 28)
- Progress monitoring via FFmpeg output parsing

### Documentation
- Comprehensive README with installation guides
- Detailed installation instructions for all platforms
- Contributing guidelines
- Troubleshooting guide
- Technical documentation

---

## Version History

### Pre-release
- Initial development
- Web-based prototype using FFmpeg.wasm
- Converted to desktop application for better performance and reliability

---

## Release Notes Format

Each version includes:
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

---

## Compatibility

| Version | Python | FFmpeg | Windows | macOS | Linux |
|---------|--------|--------|---------|-------|-------|
| 1.0.0 | 3.7+ | 4.0+ | ✅ 10/11 | ✅ 10.14+ | ✅ Ubuntu 18.04+ |

---

## Support

For help with specific versions:
- Check the [README](README.md)
- Visit [GitHub Issues](https://github.com/yourusername/compressvideo/issues)
- See [Troubleshooting Guide](INSTALL.md#troubleshooting)
