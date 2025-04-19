# FileOrganizer

A smart file organization tool that helps you automatically organize and categorize files on your computer.

## Features

- ✅ Scan directories recursively for all files
- ✅ Categorize files by type (images, documents, videos, audio, etc.)
- ✅ Display file statistics and total size
- ✅ Command-line interface with multiple output modes
- ⏳ Auto-organization features (coming soon)
- ⏳ Configuration file support (coming soon)

## Usage

```bash
# Basic usage - scan a directory
python main.py /path/to/directory

# Show detailed information for each file
python main.py /path/to/directory --verbose

# Show only category summary
python main.py /path/to/directory --summary

# Show version
python main.py --version
```

## File Categories

The tool automatically categorizes files into:
- **Images**: jpg, png, gif, svg, webp, etc.
- **Documents**: pdf, doc, docx, txt, rtf, etc.
- **Videos**: mp4, avi, mkv, mov, etc.
- **Audio**: mp3, wav, flac, aac, etc.
- **Archives**: zip, rar, 7z, tar, gz
- **Code**: py, js, html, css, java, etc.
- **Spreadsheets**: xls, xlsx, csv, ods
- **Other**: unrecognized file types

## Requirements

- Python 3.6+
- No external dependencies

## Development

This is a personal project for learning file management automation. Currently focused on scanning and categorization features.