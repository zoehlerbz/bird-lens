import cv2
import numpy as np
from bird_lens.classes.filter import Filter

class Edges(Filter):
    def __init__(self, frame):
        super().__init__(frame)
    
    def define_background(self, fgbg):
        fg_mask = fgbg.apply(self.frame)
        return fg_mask
    
    def remove_background(self, fgbg):
        mask = self.define_background(fgbg)
        self.fg_frame = cv2.bitwise_and(self.frame, self.frame, mask=mask)
        return self.fg_frame
    
    def detect_contours(self, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE):
        if len(self.fg_frame.shape) == 3:  # Se for colorida (3 canais)
            self.fg_frame = self.convert_color(self.fg_frame, cv2.COLOR_BGR2GRAY)

        contours, _ = cv2.findContours(self.fg_frame, mode, method)
        return contours
    
    def draw_contours(self, frame, color=(0, 255, 0), thickness=3):
        contours = self.detect_contours()
        cv2.drawContours(frame, contours, -1, color, thickness)
        return frame
    
    def draw_rectangles(self, frame, color=(0, 255, 0), thickness=3):
        contours = self.detect_contours()
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, thickness)
        return frame
    
    def count_objects(self):
        contours = self.detect_contours()
        return len(contours)