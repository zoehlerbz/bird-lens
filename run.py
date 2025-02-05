import os
from bird_lens.main import App

BASEDIR = os.getcwd()
PATH = os.path.join(BASEDIR, 'bird_lens', 'data', 'sample.mp4')

def main():
    app = App(PATH)
    app.run()

if __name__ == '__main__':
    main()