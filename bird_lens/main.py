import cv2
from bird_lens.src.controllers.reader import Reader
from bird_lens.src.controllers.calibrator import Calibrator
from bird_lens.src.controllers.object_finder import ObjectFinder
from bird_lens.src.services.filter import Filter

class App:
    def __init__(self, path, calibration_path):
        self.path = path
        self.calibration_path = calibration_path

    def run(self):
        reader = Reader(self.path)
        calibrator = Calibrator(self.calibration_path).compute_background()

        for frame in reader:
            fps = reader.get_fps()

            # Diferença entre o frame atual e o frame de calibração
            diff = cv2.absdiff(calibrator, frame)

            # Filtra a imagem
            filter = Filter(diff)
            filter.color()
            filter.average_blur()
            filter.dilate()
            filter.erode()
            filter.threshold(threshold=110)

            # Encontra os contornos e áreas dos objetos e delimita os objetos
            finder = ObjectFinder(filter.frame)
            finder.draw_objects(frame)
            finder.write_objects(frame)

            frame = Filter(frame)
            frame.resize()

            cv2.imshow('BirdLens', frame.frame)
            
            # Sai quando pressionar 'Esc' ou fechar a janela
            k = cv2.waitKey(fps) & 0xFF
            if k == 27 or cv2.getWindowProperty('BirdLens', cv2.WND_PROP_VISIBLE) < 1:
                break
        
        reader.cleaner()