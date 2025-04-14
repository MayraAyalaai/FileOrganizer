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
    # TODO: Implement file scanning logic
    

if __name__ == "__main__":
    main()