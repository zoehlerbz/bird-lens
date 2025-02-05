import cv2

class Filter:
    def __init__(self):
        pass
    
    def resize(self, frame, width: int = 640, height: int = 480):
        return cv2.resize(frame, (width, height))

    def average_blur(self, frame, kernel_size: int = 5):
        return cv2.blur(frame, (kernel_size, kernel_size))

    def bilateral_blur(self, frame, d: int = 9, sigma_color: int = 75, sigma_space: int = 75):
        return cv2.bilateralFilter(frame, d, sigma_color, sigma_space)
    
    def gaussian_blur(self, frame, kernel_size: int = 5, sigma_x: int = 0):
        return cv2.GaussianBlur(frame, (kernel_size, kernel_size), sigma_x)
    
    def median_blur(self, frame, kernel_size: int = 5):
        return cv2.medianBlur(frame, kernel_size)
    
    def dilate(self, frame, kernel_size: int = 5):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        return cv2.dilate(frame, kernel)
    
    def erode(self, frame, kernel_size: int = 5):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        return cv2.erode(frame, kernel)
    
    def threshold(self, frame, threshold: int = 127, max_value: int = 255, threshold_type: int = cv2.THRESH_BINARY):
        _, frame = cv2.threshold(frame, threshold, max_value, threshold_type)
        return frame
    
    def threshold_adaptive(self, frame, max_value: int = 255, adaptive_method: int = cv2.ADAPTIVE_THRESH_MEAN_C, threshold_type: int = cv2.THRESH_BINARY, block_size: int = 11, c: int = 2):
        return cv2.adaptiveThreshold(frame, max_value, adaptive_method, threshold_type, block_size, c)
    
    def color(self, frame, color_space: int = cv2.COLOR_BGR2GRAY):
        return cv2.cvtColor(frame, color_space)