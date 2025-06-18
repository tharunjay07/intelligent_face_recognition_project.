"""
face_loader.py - Responsible for loading and encoding the known face.
"""
import face_recognition

def load_face_encoding(image_path):
    try:
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if not encodings:
            raise ValueError("No face found in known image.")
        return encodings[0]
    except Exception as e:
        raise RuntimeError(f"Error loading known image: {e}")
