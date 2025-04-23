#!/usr/bin/env python3
"""
FileOrganizer - A simple file organization tool
Author: LauraFergu
"""

import os
import sys
import argparse
from datetime import datetime
from config import Config
from organizer import FileOrganizer


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
    parser.add_argument("-c", "--config", default="config.json",
                       help="Path to configuration file")
    parser.add_argument("-o", "--organize", metavar="TARGET_DIR",
                       help="Organize files into TARGET_DIR by category")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be organized without moving files")
    parser.add_argument("--version", action="version", version="FileOrganizer v0.4.0")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist")
        return
    
    # Load configuration
    config = Config(args.config)
    
    print(f"FileOrganizer v0.4.0")
    
    if args.organize:
        # Organization mode
        print(f"{'[DRY RUN] ' if args.dry_run else ''}Organizing files from: {args.directory}")
        print(f"Target directory: {args.organize}")
        
        organizer = FileOrganizer(config)
        try:
            moved_files, errors = organizer.organize_files(
                args.directory, args.organize, dry_run=args.dry_run
            )
            
            # Display results
            total_moved = sum(len(files) for files in moved_files.values())
            print(f"\n{'Would organize' if args.dry_run else 'Organized'} {total_moved} files:")
            
            for category, files in moved_files.items():
                print(f"\n{category.upper()} ({len(files)} files):")
                for file_info in files[:5]:  # Show first 5 files
                    print(f"  {os.path.basename(file_info['source'])}")
                if len(files) > 5:
                    print(f"  ... and {len(files) - 5} more files")
            
            if errors:
                print(f"\nErrors encountered: {len(errors)}")
                for error in errors[:3]:  # Show first 3 errors
                    print(f"  {error}")
                if len(errors) > 3:
                    print(f"  ... and {len(errors) - 3} more errors")
                    
        except Exception as e:
            print(f"Error during organization: {e}")
    else:
        # Scanning mode
        print(f"Scanning directory: {args.directory}")
        scan_files(args.directory, config, verbose=args.verbose, summary_only=args.summary)


def get_file_category(extension, config):
    """Categorize files based on extension using config"""
    categories = config.get_categories()
    
    for category, extensions in categories.items():
        if extension in extensions:
            return category
    
    return 'other'


def scan_files(directory, config, verbose=False, summary_only=False):
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
                category = get_file_category(file_ext, config)
                
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