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
class BookButton(Button):
    pass
class FlpyApp(App):
    def build(self):
        view = MainView(orientation="vertical")
        view.add_widget(TopBar())
        ShelfView = AndTab()
        DifferentTabs = []
        for i in range(3):
            DifferentTabs.append(MyTab(text=str(i)))
            ShelfView.add_widget(DifferentTabs[i])
        view.add_widget(ShelfView)

        DifferentTabs[0].children[0].children[-1].add_widget(BookButton(background_normal="images.jpeg"))
        DifferentTabs[0].children[0].children[-1].add_widget(BookButton(background_normal="images.jpeg"))
        DifferentTabs[0].children[0].children[-1].add_widget(BookButton(background_normal="images.jpeg"))



        #view.children[0].add_widget(MyTab(text="yo"))
        print (ShelfView.children)
        return view






if __name__ == '__main__':
    #Window.clearcolor = get_color_from_hex('#101216')

    FlpyApp().run()



