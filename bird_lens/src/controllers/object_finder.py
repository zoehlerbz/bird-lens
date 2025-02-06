import cv2
from bird_lens.src.services.contours import Contours

class ObjectFinder:
    def __init__(self, frame):
        self.frame = frame
        self.contours = Contours()
    
    def draw_objects(self, frame):
        return self.contours.draw_contours(frame, self.find_objects())
    
    def find_objects(self):
        frame = self.contours.canny_edge(self.frame)
        contours = self.contours.find_contours(frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        coordinates = self.contours.coordinates_contours(contours)
        return coordinates