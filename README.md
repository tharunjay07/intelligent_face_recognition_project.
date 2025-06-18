# Face Matcher (Modular Python Project)

This project scans a folder of images to find faces that match a known reference face using `face_recognition` and `OpenCV`. Designed with a clean modular structure for clarity and extensibility.

## 📂 Project Structure

```
face_matcher/
│
├── main.py                 # Entry point
├── config.py               # Paths and settings
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
│
├── matcher/                # Core matching logic
│   ├── face_loader.py
│   ├── face_matcher.py
│   └── face_visualizer.py
│
├── utils/                  # Utility helpers
│   └── helpers.py
│
└── images/
    ├── known/              # Reference face image
    │   └── known_face.jpg
    └── search_folder/      # Images to search in
        ├── sample1.jpg
        └── sample2.jpg
```

## 🚀 Getting Started

1. Clone the repo or download the zip:
    ```bash
    git clone https://github.com/tharun/face-matcher.git
    cd face-matcher
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    ```bash
    python main.py
    ```

## 🧠 Features
- Modular codebase
- Visual face match results
- Easy to extend (add GUI, video support, logging, etc.)

## 📸 Screenshot

> Include a screenshot of face matching result

## 📜 License
MIT License
