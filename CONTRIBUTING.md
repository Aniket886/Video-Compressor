# Contributing to CompressVideo

Thank you for your interest in contributing to CompressVideo! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to:
- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Respect different viewpoints and experiences

## Getting Started

### Prerequisites
- Python 3.7 or later
- FFmpeg installed on your system
- Git

### Fork the Repository

1. Go to the project page on GitHub
2. Click the "Fork" button (top right)
3. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/compressvideo.git
   cd compressvideo
   ```

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please:
1. Check if the bug already exists in the issues
2. Try to reproduce with the latest version
3. Collect relevant information

When creating a bug report, include:
- **Title**: Clear and descriptive
- **Environment**: OS, Python version, FFmpeg version
- **Steps to reproduce**: Numbered list
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happened
- **Screenshots**: If applicable
- **Logs**: Error messages or console output

### Suggesting Features

Feature suggestions are welcome! Please:
1. Check if the feature already exists
2. Explain why this feature would be useful
3. Provide examples of how it would work
4. Consider implementation complexity

### Contributing Code

#### Good First Issues

Look for issues labeled:
- `good first issue`
- `help wanted`
- `documentation`

#### Areas Needing Help

- [ ] Better error handling
- [ ] Additional video format support
- [ ] UI improvements
- [ ] Performance optimizations
- [ ] Test coverage
- [ ] Documentation translations

## Development Setup

### Setting Up Development Environment

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Install development dependencies**:
   ```bash
   pip install -r requirements-dev.txt  # If available
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

### Project Structure

```
compressvideo/
├── main.py              # Main application
├── run.bat              # Windows launcher
├── run.sh               # Unix launcher
├── requirements.txt     # Dependencies
├── README.md            # Main documentation
├── CONTRIBUTING.md      # This file
└── .gitignore          # Git ignore rules
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_main.py

# Run with coverage
python -m pytest tests/ --cov=main
```

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line length**: 100 characters maximum
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Grouped as standard library, third-party, local
- **Docstrings**: Google style

Example:
```python
def calculate_bitrate(file_size: int, duration: float, target_size: float) -> dict:
    """Calculate optimal bitrate for target file size.
    
    Args:
        file_size: Original file size in bytes
        duration: Video duration in seconds
        target_size: Target file size in MB
        
    Returns:
        Dictionary containing video and audio bitrates
        
    Example:
        >>> calculate_bitrate(104857600, 60.0, 25.0)
        {'video': 3138000, 'audio': 165000}
    """
    target_bits = target_size * 8 * 1024 * 1024
    total_bitrate = target_bits / duration
    
    return {
        'video': int(total_bitrate * 0.95),
        'audio': int(total_bitrate * 0.05)
    }
```

### UI Guidelines

When modifying the UI:
- Use the existing color scheme (defined in `COLORS` dict)
- Follow tkinter best practices
- Ensure responsive layout
- Test on different screen sizes
- Maintain accessibility standards

### Commit Messages

Use clear, descriptive commit messages:

```
type: Short description (50 chars or less)

Longer explanation if needed (wrap at 72 chars).
Can include multiple paragraphs.

- Bullet points are okay
- Reference issues: Fixes #123
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style (formatting, semicolons, etc)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding tests
- `chore`: Build process, dependency updates, etc

Examples:
```
feat: Add batch compression support

Allows users to compress multiple files at once.
Files are processed sequentially to avoid memory issues.

Fixes #45
```

```
fix: Handle videos with unknown duration

Use estimated 5-minute duration when metadata extraction fails.
Prevents division by zero in bitrate calculation.

Closes #67
```

## Pull Request Process

### Before Submitting

1. **Update your fork**:
   ```bash
   git remote add upstream https://github.com/original/compressvideo.git
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test your changes**:
   - Run the application
   - Test on different video formats
   - Check error handling
   - Verify UI responsiveness

3. **Update documentation**:
   - Update README.md if needed
   - Add docstrings to new functions
   - Update CHANGELOG.md if available

### Submitting

1. **Push to your fork**:
   ```bash
   git push origin feature-branch-name
   ```

2. **Create Pull Request**:
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill in the template

3. **PR Description should include**:
   - What changes were made
   - Why the changes were made
   - How to test the changes
   - Screenshots (for UI changes)
   - Related issue numbers

### Review Process

1. Maintainers will review your PR
2. Automated tests must pass
3. Address requested changes
4. Once approved, maintainers will merge

### After Merge

Your contribution will be:
- Merged into the main branch
- Included in the next release
- Credited in the release notes
- Added to the contributors list

## Questions?

Feel free to:
- Open an issue with the "question" label
- Join discussions on GitHub
- Contact maintainers

Thank you for contributing! 🎉
