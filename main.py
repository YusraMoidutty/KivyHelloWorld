import kivy

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        lbl = Label(text="Happy Birthday Shiva Mol")
        return lbl


label = MyApp()
label.run()
