# Frequently Asked Questions (FAQ)

## General Questions

### What is CompressVideo?

CompressVideo is a free, open-source desktop application for compressing video files. It uses FFmpeg to reduce file size while maintaining quality, with an easy-to-use graphical interface.

### Is it really free?

Yes! CompressVideo is completely free and open-source under the MIT License. You can use it for personal or commercial projects without any restrictions.

### Do I need internet to use it?

No. Once installed, CompressVideo works completely offline. All video processing is done locally on your computer.

### Is my data private?

Absolutely. CompressVideo processes everything locally. Your videos never leave your computer, and no data is sent to any server.

---

## Installation & Setup

### Do I need to install Python?

Python comes pre-installed on macOS and most Linux distributions. On Windows, you may need to install it if you haven't already. See [INSTALL.md](INSTALL.md) for details.

### What is FFmpeg and why do I need it?

FFmpeg is a powerful command-line tool for processing video and audio. CompressVideo is essentially a user-friendly interface for FFmpeg - it handles all the actual compression work. Without FFmpeg, the app can't process videos.

### Can I use this on my phone or tablet?

Not currently. CompressVideo is a desktop application for Windows, macOS, and Linux computers. Mobile support may be added in the future.

### How much disk space do I need?

You need approximately 2x the size of your largest video:
- Original video file
- Temporary processing space
- Output compressed file

For example, to compress a 5GB video, ensure you have at least 10-15GB free space.

---

## Usage Questions

### How much can I compress a video?

It depends on the video:
- **Mild compression**: 20-30% size reduction with minimal quality loss
- **Moderate compression**: 50-60% size reduction with slight quality loss
- **Heavy compression**: 70-80% size reduction with noticeable quality loss

The app shows recommendations based on your specific video.

### Will compressed video work on my phone/TV?

Yes! Compressed videos use standard MP4 format with H.264 codec, which works on virtually all devices:
- iPhones and Android phones
- Smart TVs
- Web browsers
- Video editing software
- Social media platforms

### Can I compress multiple videos at once?

Not in the current version. You'll need to compress videos one at a time. Batch processing is planned for a future update.

### Can I cancel compression halfway?

Yes! Click the "Cancel" button during compression. Note that the partially compressed file will be deleted.

### Why is compression taking so long?

Compression time depends on:
- **Video length**: Longer videos take more time
- **Original size**: Larger files take longer
- **Your computer**: Faster CPUs compress quicker
- **Target size**: More compression = more time

As a rough estimate: 1 minute of video takes about 30 seconds to compress on a modern computer.

### Can I pause and resume compression?

No, once you cancel, you must start over. This feature may be added in the future.

---

## Technical Questions

### What's the maximum file size?

Theoretically up to 10GB, but practical limits depend on your computer's RAM:
- **4GB RAM**: Up to 2GB files
- **8GB RAM**: Up to 5GB files
- **16GB+ RAM**: Up to 10GB files

### What video formats are supported?

**Input**: MP4, MOV, AVI, MKV, WebM, FLV, WMV
**Output**: MP4 (recommended), MOV, WebM

### Why use CRF values?

CRF (Constant Rate Factor) controls quality:
- Lower CRF = Better quality, larger file
- Higher CRF = Smaller file, lower quality
- CRF 23 is the sweet spot for most uses

### Can I use HEVC (H.265) instead of H.264?

Not currently. H.264 is used for maximum compatibility. H.265 support may be added in the future.

### Can I adjust audio settings?

The app automatically handles audio:
- Codec: AAC
- Bitrate: Calculated based on target size (typically 128kbps)
- Sample rate: Maintained from original

Advanced audio controls may be added later.

### Why does my antivirus flag the app?

Some antivirus software may flag Python scripts or new executables. This is a false positive. The app:
- Contains no malware
- Doesn't modify system files
- Only accesses files you select
- Is completely open-source

If concerned, you can review the source code in `main.py`.

---

## Troubleshooting

### "FFmpeg not found" error

**Solution**:
1. Install FFmpeg following the instructions in [INSTALL.md](INSTALL.md)
2. Restart your computer
3. Or place `ffmpeg.exe` in the same folder as `main.py`

### Video won't compress

**Try these**:
1. Check if the video plays correctly
2. Try a different output format
3. Use "High" quality preset
4. Ensure you have enough disk space
5. Close other applications

### Output video is corrupted

**Solutions**:
1. Try playing with VLC Media Player (most compatible)
2. Use MP4 output format
3. Increase target size
4. Check if original file is corrupted

### App crashes during compression

**Common causes**:
1. **Out of memory**: Close other apps, use smaller videos
2. **Disk full**: Free up disk space (need 2x video size)
3. **Corrupted video**: Try different source file
4. **FFmpeg error**: Update FFmpeg to latest version

### Quality looks worse than expected

**Tips**:
1. Increase target size
2. Use "High" quality preset
3. Check original video quality
4. Remember: some formats compress better than others

### Audio is missing in output

**Solutions**:
1. Check "Keep Original" format
2. Ensure original has audio (play it first)
3. Try MP4 output format
4. Report as bug if persists

---

## Comparison with Other Tools

### vs Online Video Compressors

| Feature | CompressVideo | Online Tools |
|---------|---------------|--------------|
| Privacy | ✅ Local processing | ❌ Uploads to server |
| File size limit | 10GB | Usually 100MB-1GB |
| Speed | Fast (local) | Depends on internet |
| Cost | Free | Often have paid tiers |
| Quality | Configurable | Limited options |
| Ads | None | Usually present |

### vs HandBrake

| Feature | CompressVideo | HandBrake |
|---------|---------------|-----------|
| Ease of use | ✅ Simple GUI | More complex |
| Advanced options | Basic | Extensive |
| Learning curve | Low | Higher |
| Batch processing | No | Yes |
| Presets | Simple | Many |

### vs Adobe Media Encoder

| Feature | CompressVideo | Adobe Media Encoder |
|---------|---------------|---------------------|
| Price | Free | Paid subscription |
| Learning curve | Low | High |
| Integration | Standalone | Adobe ecosystem |
| Advanced features | Basic | Professional |

---

## Future Plans

### Will there be batch processing?

Yes! This is planned for version 1.1.

### Will there be hardware acceleration?

Yes! Support for NVIDIA NVENC and Intel QuickSync is planned.

### Can I request features?

Yes. Open an issue on GitHub with the "feature request" label.

### How can I contribute?

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome:
- Bug reports
- Feature suggestions
- Code contributions
- Documentation improvements

---

## Still Have Questions?

- **Check the docs**: [README.md](README.md) | [INSTALL.md](INSTALL.md) | [CONTRIBUTING.md](CONTRIBUTING.md)
- **Ask a question**: [GitHub Discussions](https://github.com/Aniket886/Video-Compressor/discussions)
- **Report a bug**: [GitHub Issues](https://github.com/Aniket886/Video-Compressor/issues)

---

*Last updated: April 2024*
