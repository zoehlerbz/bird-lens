import cv2

class Contours:
    def __init__(self):
        pass

    def canny_edge(self, frame, threshold1: int = 100, threshold2: int = 200, L2gradient: bool = False):
        return cv2.Canny(frame, threshold1, threshold2, L2gradient)
    
    def find_contours(self, frame, mode: int = cv2.RETR_EXTERNAL, method: int = cv2.CHAIN_APPROX_SIMPLE):
        contours, _ = cv2.findContours(frame, mode, method)
        return contours
    
    def coordinates_contours(self, contours):
        return [cv2.boundingRect(contour) for contour in contours]

    def area_contours(self, contours):
        return [cv2.contourArea(contour) for contour in contours]
    
    def draw_contours(self, frame, coordinates):
        for x, y, w, h in coordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame