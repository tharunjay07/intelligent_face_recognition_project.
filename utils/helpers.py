"""
helpers.py - Utility functions.
"""
import os

def get_all_image_files(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Search directory not found: {directory}")
    return [f for f in os.listdir(directory)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
