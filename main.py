#!/usr/bin/env python3
"""
FileOrganizer - A simple file organization tool
Author: LauraFergu
"""

import os
import sys


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


def scan_files(directory):
    """Scan directory and list all files with basic info"""
    file_count = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                file_ext = os.path.splitext(file)[1].lower()
                
                print(f"File: {file}")
                print(f"  Path: {file_path}")
                print(f"  Size: {file_size} bytes")
                print(f"  Extension: {file_ext if file_ext else 'No extension'}")
                print("---")
                
                file_count += 1
                
            except (OSError, IOError) as e:
                print(f"Error accessing file {file_path}: {e}")
    
    print(f"\nTotal files scanned: {file_count}")
    

if __name__ == "__main__":
    main()