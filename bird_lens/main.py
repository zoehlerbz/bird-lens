import cv2
from bird_lens.src.controllers.reader import Reader
from bird_lens.src.controllers.calibrator import Calibrator
from bird_lens.src.services.filter import Filter

class App:
    def __init__(self, path, calibration_path):
        self.path = path
        self.calibration_path = calibration_path

    def run(self):
        reader = Reader(self.path)
        calibrator = Calibrator(self.calibration_path).compute_background()

        for frame in reader:

            diff = cv2.absdiff(calibrator, frame)

            frame = Filter().resize(frame)
            cv2.imshow('BirdLens', frame)
            cv2.imshow('BirdLens - diff', Filter().resize(diff))
            
            # Sai quando pressionar 'Esc' ou fechar a janela
            k = cv2.waitKey(reader.get_fps()) & 0xFF
            if k == 27 or cv2.getWindowProperty('BirdLens', cv2.WND_PROP_VISIBLE) < 1:
                break
        
        reader.cleaner()
        cv2.destroyAllWindows()