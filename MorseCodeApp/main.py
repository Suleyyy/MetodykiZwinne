from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MorseCodeWidget(GridLayout):
    pass

class MorseCodeApp(App):
    def build(self):
        return MorseCodeWidget()

if __name__ == '__main__':
    MorseCodeApp().run()
