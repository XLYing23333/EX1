import os

class Path:
    def __init__(self):
        self.UTILS = os.path.join(os.path.dirname(__file__))
        self.ROOT = os.path.dirname(self.UTILS)
        self.DATA = os.path.join(self.ROOT, 'data')
        self.PAGES = os.path.join(self.ROOT, 'pages')
        self.MODELS = os.path.join(self.ROOT,'models')
    
    def show_paths(self):
        print(f"UTILS: {self.UTILS}")
        print(f"PAGES: {self.PAGES}")
        print(f"MODELS: {self.MODELS}")
        print(f"DATA: {self.DATA}")
        print(f"PAGES: {self.PAGES}")

if __name__ == '__main__':
    path = Path()
    path.show_paths()