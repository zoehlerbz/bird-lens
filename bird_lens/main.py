import cv2 as cv

IMG_PATH = 'data/raw/bird.jpg'

class Window:
    """Create a window with an image."""
    def __init__(self, win, img):
        self.win = win
        self.img = img
        cv.imshow(win, img)


class App:
    def __init__(self):
        img = cv.imread(IMG_PATH)
        Window('image', img)
        
    def run(self):
        """Run the main event loop."""
        k = 0
        while True:
            k = cv.waitKey(1)  # Espera 1 ms por uma tecla
            if k == -1:  # Caso nenhuma tecla tenha sido pressionada
                # Verifica se a janela foi fechada
                if cv.getWindowProperty('image', cv.WND_PROP_VISIBLE) < 1:
                    break
                continue
            elif k == 27:  # Sai do loop se a tecla 'ESC' for pressionada
                break
        
        cv.destroyAllWindows()