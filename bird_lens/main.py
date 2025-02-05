import cv2
from bird_lens.models.reader import Reader

class App:
    def __init__(self, path):
        self.path = path

    def run(self):
        reader = Reader(self.path)
        for frame in reader:
            cv2.imshow('BirdLens', frame)
            
            # Sai quando pressionar 'Esc' ou fechar a janela
            k = cv2.waitKey(reader.get_fps()) & 0xFF
            if k == 27 or cv2.getWindowProperty('BirdLens', cv2.WND_PROP_VISIBLE) < 1:
                break
        
        reader.cleaner()
        cv2.destroyAllWindows()