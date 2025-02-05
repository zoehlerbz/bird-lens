import cv2
import os

class Reader:
    def __init__(self, video_path):
        self.video = cv2.VideoCapture(video_path)

        if not os.path.exists(video_path):
            raise FileNotFoundError(f"\nArquivo não encontrado: '{video_path}'")

        if not self.video.isOpened():
            raise ValueError(f"\nErro ao abrir vídeo/câmera: '{video_path}'")

    def get_fps(self):
        return int(self.video.get(cv2.CAP_PROP_FPS))

    def reader(self):
        ret, frame = self.video.read()
        if not ret:
            return None
        return frame
    
    def __iter__(self):
        return self

    def __next__(self):
        frame = self.reader()
        if frame is None:
            self.video.release()
            raise StopIteration
        return frame
    
    def cleaner(self):
        self.video.release()
        cv2.destroyAllWindows()

    def __del__(self):
        self.cleaner()