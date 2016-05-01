from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import time
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.androidtabs import *
from kivy.uix.button import Button
from kivy.lang import Builder

class TopBar(BoxLayout):
    pass
class MyTab(BoxLayout,AndroidTabsBase):
    pass
class MainView(BoxLayout):
    pass
class Shelf(BoxLayout):
    pass
class AndTab(AndroidTabs):
    pass


class FlpyApp(App):
    def build(self):
        view = MainView(orientation="vertical")
        view.add_widget(TopBar())
        ShelfView = AndTab()
        for i in range(5):
            ShelfView.add_widget(MyTab(text=str(i)))
        view.add_widget(ShelfView)

        return view






if __name__ == '__main__':
    #Window.clearcolor = get_color_from_hex('#101216')

    FlpyApp().run()



