"""
Configuration module for FileOrganizer
Handles loading and saving user preferences
"""

import json
import os
from pathlib import Path


class Config:
    """Configuration manager for FileOrganizer"""
    
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.default_config = {
            "categories": {
                "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
                "documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
                "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
                "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
                "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
                "code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c"],
                "spreadsheets": [".xls", ".xlsx", ".csv", ".ods"]
            },
            "ignore_hidden": True,
            "ignore_patterns": [".git", ".DS_Store", "Thumbs.db"],
            "max_depth": -1
        }
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from file, create default if not exists"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                # Merge with defaults to ensure all keys exist
                config = self.default_config.copy()
                config.update(loaded_config)
                return config
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading config file: {e}")
                print("Using default configuration")
                return self.default_config.copy()
        else:
            return self.default_config.copy()
    
    def save_config(self):
        """Save current configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except IOError as e:
            print(f"Error saving config file: {e}")
            return False
    
    def get_categories(self):
        """Get file categories mapping"""
        return self.config.get("categories", {})
    
    def add_category(self, category_name, extensions):
        """Add or update a file category"""
        self.config["categories"][category_name] = extensions
    
    def get_ignore_patterns(self):
        """Get patterns to ignore during scanning"""
        return self.config.get("ignore_patterns", [])
    
    def should_ignore_hidden(self):
        """Check if hidden files should be ignored"""
        return self.config.get("ignore_hidden", True)
    
    def get_max_depth(self):
        """Get maximum directory depth to scan"""
        return self.config.get("max_depth", -1)