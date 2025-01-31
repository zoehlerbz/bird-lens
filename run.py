import os
from bird_lens.main import App

BASE_DIR = os.getcwd()
VIDEO_PATH = os.path.join(BASE_DIR, 'bird_lens', 'data', 'sample.mp4')  # VIDEO_PATH = -1 para usar a webcam/câmera

def main():
    app = App('Bird counter', VIDEO_PATH)
    app.run()

if __name__ == "__main__":
    main()