import os
from bird_lens.main import App

BASEDIR = os.getcwd()
PATH = os.path.join(BASEDIR, 'bird_lens', 'data', 'sample3.mp4')
CALIBRATION = os.path.join(BASEDIR, 'bird_lens', 'data', 'calibration3.mp4')

def main():
    app = App(PATH, CALIBRATION)
    app.run()

if __name__ == '__main__':
    main()