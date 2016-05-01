from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import time
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.androidtabs import *
from kivy.uix.button import Button


class MyTab(BoxLayout,AndroidTabsBase):
    pass
class MainView(BoxLayout):
    pass
class Shelf(BoxLayout):
    pass
class TopBar(BoxLayout):
    pass


class FlpyApp(App):
    def build(self):
        view = MainView()
        return view





class MyTab():
    pass
if __name__ == '__main__':
    #Window.clearcolor = get_color_from_hex('#101216')

    FlpyApp().run()



