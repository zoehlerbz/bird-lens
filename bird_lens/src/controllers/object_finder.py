import cv2
from collections import deque
from bird_lens.src.services.contours import Contours

class ObjectFinder:
    def __init__(self, frame):
        self.frame = frame
        self.contours = Contours()
    
    def draw_objects(self, frame):
        coordinates = self.contours.coordinates_contours(self.find_objects())
        return self.contours.draw_contours(frame, coordinates)
    
    def write_objects(self, frame):
        # Conta o número de objetos por frame
        count = self.count_objects()

        cv2.putText(frame, f'Count (frame): {count}', (20,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)
        
        return frame

    def count_objects(self):
        return len(self.find_objects())

    def find_objects(self):
        frame = self.contours.canny_edge(self.frame)
        contours = self.contours.find_contours(frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        return contours