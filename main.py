#!/usr/bin/env python3
"""
FileOrganizer - A simple file organization tool
Author: LauraFergu
"""

import os
import sys
import argparse
from datetime import datetime


def main():
    """Main entry point for FileOrganizer"""
    parser = argparse.ArgumentParser(
        description="FileOrganizer - A smart file organization tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("directory", help="Directory to scan and organize")
    parser.add_argument("-v", "--verbose", action="store_true", 
                       help="Show detailed file information")
    parser.add_argument("-s", "--summary", action="store_true",
                       help="Show only category summary")
    parser.add_argument("--version", action="version", version="FileOrganizer v0.2.0")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist")
        return
    
    print(f"FileOrganizer v0.2.0")
    print(f"Scanning directory: {args.directory}")
    
    scan_files(args.directory, verbose=args.verbose, summary_only=args.summary)


def get_file_category(extension):
    """Categorize files based on extension"""
    categories = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
        'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
        'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
        'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.c'],
        'spreadsheets': ['.xls', '.xlsx', '.csv', '.ods']
    }
    
    for category, extensions in categories.items():
        if extension in extensions:
            return category
    
    return 'other'


def scan_files(directory, verbose=False, summary_only=False):
    """Scan directory and list all files with basic info"""
    file_count = 0
    categories = {}
    total_size = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                file_ext = os.path.splitext(file)[1].lower()
                category = get_file_category(file_ext)
                
                if category not in categories:
                    categories[category] = 0
                categories[category] += 1
                total_size += file_size
                
                if not summary_only:
                    if verbose:
                        print(f"File: {file}")
                        print(f"  Path: {file_path}")
                        print(f"  Size: {file_size} bytes")
                        print(f"  Extension: {file_ext if file_ext else 'No extension'}")
                        print(f"  Category: {category}")
                        print("---")
                    else:
                        print(f"{file} [{category}]")
                
                file_count += 1
                
            except (OSError, IOError) as e:
                if not summary_only:
                    print(f"Error accessing file {file_path}: {e}")
    
    print(f"\nScan Results:")
    print(f"Total files: {file_count}")
    print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.1f} MB)")
    print(f"\nFiles by category:")
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count} files")
    

if __name__ == "__main__":
    main()