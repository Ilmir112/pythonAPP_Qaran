from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, NoTransition, TransitionBase

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty, ListProperty
from kivymd.app import MDApp


import dataloader as dt
import random

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


question = []
firstanswer = []
secondanswer = []
thirdanswer = []
fourthanswer = []
rightanswer = []


question_list = dt.data_from_csv(question, firstanswer, secondanswer, thirdanswer, fourthanswer, rightanswer)

class SignButton(Button):
    bg_color = ListProperty([1, 1, 1, 0])

class OptionButton(Button):
    bg_color = ListProperty([1, 1, 1, 0])

class QaranApp(MDApp):

    selected_sign = ''
    def build(self):
        global screen_manager
        screen_manager = ScreenManager(transition = NoTransition())
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('select_sign.kv'))
        screen_manager.add_widget(Builder.load_file('quiz.kv'))
        # screen_manager.add_widget(Builder.load_file('final_score.kv'))

        menu_items = [{'text': 'Меню левое 1', 'viewclass': 'OneLineListItem', 'on_release': lambda x = 'меню левое 1': self.menu_callback(x),},
                      {'text': 'Меню левое 2', 'viewclass': 'OneLineListItem', 'on_release': lambda x = 'меню левое 2': self.menu_callback(x), },
                      {'text': 'Меню левое 1', 'viewclass': 'OneLineListItem', 'on_release': lambda x = 'меню левое 1': self.menu_callback(x), },]
        self.menu = MDDropdownMenu(items=menu_items, width_mult=2.5, )
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        return screen_manager

    def select_sign(self, sign):
       self.selected_sign = sign

       question1 = random.choice(question)
       get_answer1 = random.choice(firstanswer)
       get_answer2 = random.choice(secondanswer)
       get_answer3 = random.choice(thirdanswer)
       get_answer4 = random.choice(fourthanswer)

       screen_manager.get_screen('quiz').ids.question.text = f'{question1}'
       screen_manager.get_screen('quiz').ids.answer1.text = f'{get_answer1}'
       screen_manager.get_screen('quiz').ids.answer2.text = f'{get_answer2}'
       screen_manager.get_screen('quiz').ids.answer3.text = f'{get_answer3}'
       screen_manager.get_screen('quiz').ids.answer4.text = f'{get_answer4}'

       screen_manager.current = 'quiz'




QaranApp().run()