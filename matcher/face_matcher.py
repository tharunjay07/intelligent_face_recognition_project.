"""
face_matcher.py - Compares faces and determines matches.
"""
import face_recognition

def match_faces_in_image(image_path, known_encoding, tolerance=0.5):
    try:
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        matches = []
        for face_encoding, face_location in zip(face_encodings, face_locations):
            distance = face_recognition.face_distance([known_encoding], face_encoding)[0]
            if distance <= tolerance:
                matches.append(face_location)
        return matches
    except Exception as e:
        print(f"Error matching faces in {image_path}: {e}")
        return []
