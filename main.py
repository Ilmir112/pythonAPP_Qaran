from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

class ContentNavigationDrawer(MDBoxLayout):
    pass

class QaranApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_file('qaran.kv')

        return screen


QaranApp().run()