"""
File organization module for FileOrganizer
Handles moving and organizing files based on categories
"""

import os
import shutil
from pathlib import Path


class FileOrganizer:
    """Handles file organization operations"""
    
    def __init__(self, config):
        self.config = config
        
    def organize_files(self, source_dir, target_dir, dry_run=False):
        """
        Organize files from source to target directory by category
        
        Args:
            source_dir: Source directory to scan
            target_dir: Target directory to organize files into
            dry_run: If True, only show what would be moved without actually moving
        """
        if not os.path.exists(source_dir):
            raise ValueError(f"Source directory does not exist: {source_dir}")
            
        # Create target directory if it doesn't exist
        if not dry_run and not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        moved_files = {}
        errors = []
        
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(root, file)
                
                # Skip if it's in the target directory already
                if os.path.commonpath([source_path, target_dir]) == target_dir:
                    continue
                    
                try:
                    result = self._organize_single_file(
                        source_path, target_dir, dry_run
                    )
                    
                    if result:
                        category, dest_path = result
                        if category not in moved_files:
                            moved_files[category] = []
                        moved_files[category].append({
                            'source': source_path,
                            'destination': dest_path,
                            'size': os.path.getsize(source_path) if os.path.exists(source_path) else 0
                        })
                        
                except Exception as e:
                    errors.append(f"Error processing {source_path}: {e}")
                    
        return moved_files, errors
    
    def _organize_single_file(self, file_path, target_dir, dry_run=False):
        """Organize a single file"""
        file_name = os.path.basename(file_path)
        file_ext = os.path.splitext(file_name)[1].lower()
        
        # Determine category
        category = self._get_file_category(file_ext)
        
        # Create category directory
        category_dir = os.path.join(target_dir, category)
        if not dry_run and not os.path.exists(category_dir):
            os.makedirs(category_dir)
            
        # Generate destination path
        dest_path = os.path.join(category_dir, file_name)
        
        # Handle filename conflicts
        counter = 1
        base_name, ext = os.path.splitext(file_name)
        while os.path.exists(dest_path):
            new_name = f"{base_name}_{counter}{ext}"
            dest_path = os.path.join(category_dir, new_name)
            counter += 1
            
        if not dry_run:
            shutil.move(file_path, dest_path)
            
        return category, dest_path
    
    def _get_file_category(self, extension):
        """Get file category from extension"""
        categories = self.config.get_categories()
        
        for category, extensions in categories.items():
            if extension in extensions:
                return category
                
        return 'other'
    
    def create_directory_structure(self, base_dir, dry_run=False):
        """Create organized directory structure"""
        categories = self.config.get_categories().keys()
        created_dirs = []
        
        for category in categories:
            category_path = os.path.join(base_dir, category)
            if not os.path.exists(category_path):
                if not dry_run:
                    os.makedirs(category_path)
                created_dirs.append(category_path)
                
        # Also create 'other' directory
        other_path = os.path.join(base_dir, 'other')
        if not os.path.exists(other_path):
            if not dry_run:
                os.makedirs(other_path)
            created_dirs.append(other_path)
            
        return created_dirs