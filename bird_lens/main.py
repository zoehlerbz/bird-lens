import cv2
from bird_lens.classes.reader import Reader
from bird_lens.classes.filter import Filter
from bird_lens.classes.edges import Edges
from bird_lens.classes.counter import Counter

class Window:
    def __init__(self, win, video_path):
        self.win = win
        self.reader = Reader(video_path)
        self.fps = self.reader.fps
        self.bird_counter = Counter()
        self.fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
    
    def show(self):
        for frame in self.reader:
            # Aplica os filtros no frame
            frame = Filter(frame)
            frame.convert_color()
            frame.threshold(90)
            frame.blur()
            frame.dilate()
            frame.erode()
            
            # Remove o fundo e desenha contornos
            bg_remover = Edges(frame.frame)
            bg_remover.remove_background(self.fgbg)
            bg_remover.draw_rectangles(frame.original)
            objects = bg_remover.count_objects()
            
            # Atualiza e desenha o contador de pássaros
            self.bird_counter.update(objects)
            self.bird_counter.draw_count(frame.original)
            
            # Exibe o resultado na janela
            cv2.imshow(self.win, frame.original)
            
            # Sai quando pressionar 'Esc' ou fechar a janela
            k = cv2.waitKey(self.fps) & 0xFF
            if k == 27 or cv2.getWindowProperty(self.win, cv2.WND_PROP_VISIBLE) < 1:
                break
        
        self.reader.cleaner()
        cv2.destroyAllWindows()

class App:
    def __init__(self, window, video_path):
        self.window = Window(window, video_path)
    
    def run(self):
        self.window.show()