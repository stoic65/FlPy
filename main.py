from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import time
from kivy.uix.boxlayout import BoxLayout
class FlpyApp(App):
    pass
class Shelf(BoxLayout):
    pass

if __name__ == '__main__':
    #Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name='Roboto',
        fn_regular='Roboto-Thin.ttf',
        fn_bold='Roboto-Medium.ttf')
    FlpyApp().run()
    


