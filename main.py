"""
main.py - Entry point of the Face Matcher application.
"""

from config import KNOWN_IMAGE_PATH, SEARCH_FOLDER_PATH, MATCH_TOLERANCE
from matcher.face_loader import load_face_encoding
from matcher.face_matcher import match_faces_in_image
from matcher.face_visualizer import visualize_match
from utils.helpers import get_all_image_files
import os

def run_face_matching():
    print("Loading the known face...")
    known_encoding = load_face_encoding(KNOWN_IMAGE_PATH)

    print(f"Searching in folder: {SEARCH_FOLDER_PATH}")
    search_images = get_all_image_files(SEARCH_FOLDER_PATH)

    for img_file in search_images:
        img_path = os.path.join(SEARCH_FOLDER_PATH, img_file)
        print(f"Analyzing: {img_file}")

        matches = match_faces_in_image(img_path, known_encoding, MATCH_TOLERANCE)
        if matches:
            print(f"Match found in {img_file}!")
            for face_location in matches:
                visualize_match(img_path, face_location)
        else:
            print(f"No match found in {img_file}.")

if __name__ == "__main__":
    run_face_matching()
