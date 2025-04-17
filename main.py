#!/usr/bin/env python3
"""
FileOrganizer - A simple file organization tool
Author: LauraFergu
"""

import os
import sys
from datetime import datetime


def main():
    """Main entry point for FileOrganizer"""
    print("FileOrganizer v0.1.0")
    print("Smart file organization tool")
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <directory>")
        return
    
    target_dir = sys.argv[1]
    
    if not os.path.exists(target_dir):
        print(f"Error: Directory '{target_dir}' does not exist")
        return
    
    print(f"Scanning directory: {target_dir}")
    
    scan_files(target_dir)


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


def scan_files(directory):
    """Scan directory and list all files with basic info"""
    file_count = 0
    categories = {}
    
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
                
                print(f"File: {file}")
                print(f"  Path: {file_path}")
                print(f"  Size: {file_size} bytes")
                print(f"  Extension: {file_ext if file_ext else 'No extension'}")
                print(f"  Category: {category}")
                print("---")
                
                file_count += 1
                
            except (OSError, IOError) as e:
                print(f"Error accessing file {file_path}: {e}")
    
    print(f"\nTotal files scanned: {file_count}")
    print("\nFiles by category:")
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count} files")
    

if __name__ == "__main__":
    main()