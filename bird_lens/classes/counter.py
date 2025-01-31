import cv2
import numpy as np

class Counter:
    def __init__(self, fps=30):
        self.fps = fps
        self.contour_counts = []

    def update(self, num_contours):
        self.contour_counts.append(num_contours)

    def get_average(self):
        if len(self.contour_counts) >= self.fps:
            avg_birds = int(np.mean(self.contour_counts[-self.fps:]))  # Média dos últimos x frames (1 segundo)
            return avg_birds
        return None

    def draw_count(self, frame):
        avg_birds = self.get_average()
        if avg_birds is not None:
            text = f"Birds: {avg_birds}"
            cv2.putText(frame, text, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        return frame