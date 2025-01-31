import cv2

class Filter:
    def __init__(self, frame):
        # Dimensões do frame
        if frame.shape[1] > 800 and frame.shape[0] > 600:
            width = frame.shape[1] // 2
            height = frame.shape[0] // 2
        else:
            width = frame.shape[1]
            height = frame.shape[0]

        self.original = self.resize(frame, width, height)  # Frame original
        self.fg_frame = self.resize(frame, width, height)  # Frame com o fundo removido
        self.frame = self.resize(frame, width, height)  # Frame manipulado

    def resize(self, frame, width, height):
        return cv2.resize(frame, (width, height))
    
    def blur(self, kernel_size=(3, 3), sigma_x=3):
        self.frame = cv2.GaussianBlur(self.frame, kernel_size, sigma_x)
        return self.frame

    def threshold(self, threshold_value=80):
        _, self.frame = cv2.threshold(self.frame, threshold_value, 255, cv2.THRESH_BINARY)
        return self.frame

    def dilate(self, kernel=None, iterations=1):
        self.frame = cv2.dilate(self.frame, kernel, iterations=iterations)
        return self.frame

    def erode(self, kernel=None, iterations=1):
        self.frame = cv2.erode(self.frame, kernel, iterations=iterations)
        return self.frame
    
    def convert_color(self, frame=None, color_space=cv2.COLOR_BGR2GRAY):
        if frame is not None:
            frame = cv2.cvtColor(self.frame, color_space)
            return frame

        self.frame = cv2.cvtColor(self.frame, color_space)
        return self.frame
