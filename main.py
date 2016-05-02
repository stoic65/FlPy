from __future__ import division
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
from kivy.storage.jsonstore import JsonStore
import os.path
#from PyPDF2 import PdfFileReader
from kivy.uix.screenmanager import ScreenManager, Screen

#store.put('books',pdf=[],pdfi=[],code=[],codei=[],extra=[],extrai=[],all=[],alli=[])
import os
text='rahul'
store = JsonStore('books.json')
#store.put('name',something="This")



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


def shelfLoader(root):

    #Calculate here number of books in json store
    bookList = list(store.find())
    NumberOfBooks =  len(bookList) #store.count()#Assumedher

   # print NumberOfBooks
    ShelfView = AndTab()
    DifferentTabs = []
    for i in range((NumberOfBooks//12)+1):
        DifferentTabs.append(MyTab(text=str(i)))
        ShelfView.add_widget(DifferentTabs[i])

    root.add_widget(ShelfView)
    for i in range(NumberOfBooks):
        #print(bookList[i][1]["image"])
        DifferentTabs[i//12].children[0].children[-1-(i%12)//3].add_widget(BookButton(background_normal=bookList[i][1]["image"]))



   # print(root.children)


        #view.children[0].add_widget(MyTab(text="yo"))
   # print (ShelfView.children)


class TopBar(BoxLayout):

    def add_more(self):
        self.parent.remove_widget(self.parent.children[0])
        self.parent.add_widget(MyWidget())
    def back(self):
        self.parent.remove_widget(self.parent.children[0])
        shelfLoader(self.parent)



class FlpyApp(App):
    def build(self):
        view = MainView(orientation="vertical")
        view.add_widget(TopBar())
        shelfLoader(view)
        return view













class MyWidget(BoxLayout,Screen):

    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            file=filename[0].split('/')
            titleName,extention=file[-1].split('.')
            fullPath = "/".join(file)
            if(extention=='pdf'):
                store.put(fullPath,title=titleName,content="Unable to read",ext=extention,image=path+"/"+titleName+".jpg")
            elif(extention=='js' or extention=='css' or extention=='html' or extention=='c' or extention=='cpp' or extention=='py' or extention=='php'):
                store.put(fullPath,title=titleName,content=f.read(),ext=extention,image=extention+".jpg")
            elif(extention=='' or extention=='txt'):
                 store.put(fullPath,title=titleName,content=f.read(),ext=extention,image=path+"/"+titleName+".jpg")
        self.parent.children[-1].back()

    def viewbook(self,*arr):
        book=store.get('data')
       # print (book)




if __name__ == '__main__':
    #Window.clearcolor = get_color_from_hex('#101216')

    FlpyApp().run()



