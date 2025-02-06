import cv2
import os

class Calibrator:
    def __init__(self, calibration_path: str, alpha: float = 0.05):
        if not os.path.exists(calibration_path):
            raise FileNotFoundError(f"\nArquivo não encontrado: '{calibration_path}'")
        if isinstance(calibration_path, int):
            raise ValueError(f"\nO arquivo de calibração não pode ser uma câmera: '{calibration_path}'")
        self.calibration_path = calibration_path
        
        self.alpha = alpha
        self.fundo = None
    
    def compute_background(self):
        calibration = cv2.VideoCapture(self.calibration_path)
        if not calibration.isOpened():
            raise ValueError(f"Erro ao abrir o vídeo de calibração: {self.calibration_path}")
        
        while True:
            ret, frame = calibration.read()
            if not ret:
                break
                        
            if self.fundo is None:
                self.fundo = frame.astype("float")
            else:
                cv2.accumulateWeighted(frame, self.fundo, self.alpha)
        
        calibration.release()
        return cv2.convertScaleAbs(self.fundo)