"""
face_visualizer.py - Displays images with matched face rectangles.
"""
import cv2
import face_recognition

def visualize_match(image_path, face_location):
    image = face_recognition.load_image_file(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    top, right, bottom, left = face_location

    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(image, "Match", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (0, 255, 0), 2)

    cv2.imshow("Match Found", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
