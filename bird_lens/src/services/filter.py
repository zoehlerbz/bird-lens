import cv2

class Filter:
    def __init__(self, frame):
        self.frame = frame
    
    def resize(self, width: int = 640, height: int = 480):
        self.frame = cv2.resize(self.frame, (width, height))
        return self

    def average_blur(self, kernel_size: int = 5):
        self.frame = cv2.blur(self.frame, (kernel_size, kernel_size))
        return self

    def bilateral_blur(self, d: int = 9, sigma_color: int = 75, sigma_space: int = 75):
        self.frame = cv2.bilateralFilter(self.frame, d, sigma_color, sigma_space)
        return self
    
    def gaussian_blur(self, kernel_size: int = 5, sigma_x: int = 0):
        self.frame = cv2.GaussianBlur(self.frame, (kernel_size, kernel_size), sigma_x)
        return self
    
    def median_blur(self, kernel_size: int = 5):
        self.frame = cv2.medianBlur(self.frame, kernel_size)
        return self
    
    def dilate(self, kernel_size: int = 5):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        self.frame = cv2.dilate(self.frame, kernel)
        return self
    
    def erode(self, kernel_size: int = 5):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        self.frame = cv2.erode(self.frame, kernel)
        return self
    
    def threshold(self, threshold: int = 127, max_value: int = 255, threshold_type: int = cv2.THRESH_BINARY):
        _, frame = cv2.threshold(self.frame, threshold, max_value, threshold_type)
        self.frame = frame
        return self
    
    def threshold_adaptive(self, max_value: int = 255, adaptive_method: int = cv2.ADAPTIVE_THRESH_MEAN_C, threshold_type: int = cv2.THRESH_BINARY, block_size: int = 11, c: int = 2):
        self.frame = cv2.adaptiveThreshold(self.frame, max_value, adaptive_method, threshold_type, block_size, c)
        return self
    
    def color(self, color_space: int = cv2.COLOR_BGR2GRAY):
        self.frame = cv2.cvtColor(self.frame, color_space)
        return self