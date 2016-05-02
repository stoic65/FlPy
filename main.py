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

store = JsonStore('book1.json')
#store.put('books',pdf=[],pdfi=[],code=[],codei=[],extra=[],extrai=[],all=[],alli=[])
import os
text='rahul'
store = JsonStore('books.json')
store.put('name',something="This")
class TopBar(BoxLayout):
    def add_more(self):
        self.parent.remove_widget(self.parent.children[0])
        self.parent.add_widget(MyWidget())




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
        print(view.children)


        #view.children[0].add_widget(MyTab(text="yo"))
        print (ShelfView.children)
        return view




class MyWidget(BoxLayout,Screen):

    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            file=filename[0].split('/')
            extention=file[-1].split('.')
            if(extention[1]=='pdf'):
                self.pdfView(filename)
                self.allSelected(filename)
            elif(extention[1]=='js' or extention[1]=='css' or extention[1]=='html' or extention[1]=='c' or extention[1]=='cpp' or extention[1]=='py' or extention[1]=='php'):
                store.put('data',content=f.read())
                self.codSelected(filename)
                self.allSelected(filename)
            elif(extention[1]=='' or extention[1]=='txt'):
                 store.put('data',content=f.read())
                 self.extraSelected(filename)
                 self.allSelected(filename)
            else:
            	   pass

    def pdfSelected(self, *ar):
        book=store.get('books')
        file=ar[0][0][0]
        temp=file.split('.')
        imagepath=temp[0]+".jpg"
        if(file in book['pdf']):
            pass
        else:
            book['pdf'].insert(0,file)
            book['pdfi'].insert(0,imagepath)
            store.put('books',pdf=book['pdf'],pdfi=book['pdfi'],code=book['code'],codei=book['codei'],extra=book['extra'],extrai=book['extrai'],all=book['all'],alli=book['alli'])


    def codSelected(self, *ar):
        book=store.get('books')
        file=ar[0][0]
        temp=file.split('.')
        imagepath=temp[0]+".jpg"
        if(file in book['code']):
            pass
        else:
            book['code'].insert(0,file)
            book['codei'].insert(0,imagepath)
            store.put('books',pdf=book['pdf'],pdfi=book['pdfi'],code=book['code'],codei=book['codei'],extra=book['extra'],extrai=book['extrai'],all=book['all'],alli=book['alli'])

    def allSelected(self, *ar):
        book=store.get('books')
        file=ar[0][0]
        temp=file.split('.')
        imagepath=temp[0]+".jpg"
        if(file in book['all']):
            pass
        else:
            book['all'].insert(0,file)
            book['alli'].insert(0,imagepath)
            store.put('books',pdf=book['pdf'],pdfi=book['pdfi'],code=book['code'],codei=book['codei'],extra=book['extra'],extrai=book['extrai'],all=book['all'],alli=book['alli'])


    def extraSelected(self, *ar):
        book=store.get('books')
        file=ar[0][0]
        temp=file.split('.')
        imagepath=temp[0]+".jpg"
        if(file in book['extra']):
            pass
        else:
            book['extra'].insert(0,file)
            book['extrai'].insert(0,imagepath)
            store.put('books',pdf=book['pdf'],pdfi=book['pdfi'],code=book['code'],codei=book['codei'],extra=book['extra'],extrai=book['extrai'],all=book['all'],alli=book['alli'])

    def pdfView(self,*ar):
        self.pdfSelected(ar)
        fh = open(ar[0][0], "rb")
        input = PdfFileReader(fh)
        page=input.getPage(1)
        store.put('data',content=page.extractText())

    def viewbook(self,*arr):
        book=store.get('data')
        print (book)




if __name__ == '__main__':
    #Window.clearcolor = get_color_from_hex('#101216')

    FlpyApp().run()



