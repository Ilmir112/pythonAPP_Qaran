from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp




class QaranApp(MDApp):
    def build(self):
        menu_items = [{'text': 'Меню левое 1', 'viewclass': 'OneLineListItem', 'on_release': lambda x = 'меню левое 1': self.menu_callback(x),},
                      {'text': 'Меню левое 2', 'viewclass': 'OneLineListItem', 'on_release': lambda x = 'меню левое 2': self.menu_callback(x), },
                      {'text': 'Меню левое 1', 'viewclass': 'OneLineListItem', 'on_release': lambda x = 'меню левое 1': self.menu_callback(x), },]
        self.menu = MDDropdownMenu(items=menu_items, width_mult=2.5, )



        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        screen = Builder.load_file('qaran.kv')

        return screen


QaranApp().run()