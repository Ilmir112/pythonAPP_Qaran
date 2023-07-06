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

question_list = dt.data_from_csv(question)


class SignButton(Button):
    bg_color = ListProperty([1, 0, 1, 0])


class OptionButton(Button):
    bg_color = ListProperty([1, 1, 1, 0])


class QaranApp(MDApp):
    selected_game = ''

    def build(self):
        global screen_manager
        screen_manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('select_game.kv'))
        screen_manager.add_widget(Builder.load_file('quiz.kv'))
        # screen_manager.add_widget(Builder.load_file('final_score.kv'))

        menu_items = [{'text': 'Меню левое 1', 'viewclass': 'OneLineListItem',
                       'on_release': lambda x='меню левое 1': self.menu_callback(x), },
                      {'text': 'Меню левое 2', 'viewclass': 'OneLineListItem',
                       'on_release': lambda x='меню левое 2': self.menu_callback(x), },
                      {'text': 'Меню левое 1', 'viewclass': 'OneLineListItem',
                       'on_release': lambda x='меню левое 1': self.menu_callback(x), }, ]
        self.menu = MDDropdownMenu(items=menu_items, width_mult=2.5, )
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        return screen_manager

    def select_game(self, game):
        self.selected_game = game

        question_random = random.choice(question)
        guestion1 = question_random[0]
        self.right_answer = question_random[1]
        answer_list = [self.right_answer]

        while len(answer_list) != 4:
            answer_random = random.choice(question)[1]
            if answer_random not in answer_list:
                answer_list.append(answer_random)

        random.shuffle(answer_list)

        screen_manager.get_screen('quiz').ids.question.text = f'{guestion1}'

        for i in range(1, 5):
            screen_manager.get_screen('quiz').ids[f'answer{i}'].text = f'{answer_list[i - 1]}'

        screen_manager.correct = 'quiz'

    def get_id(self, instance):
        for id, widget in instance.parent.parent.parent.items():
            if widget.__self__ == instance:
                return id

    def quiz(self, answer, instance):


        if answer == self.right_answer:
            screen_manager.get_screen('quiz').ids[self.get_id(instance)].bg_color = (0, 1, 0, 1)

    def next_question(self):
        pass


QaranApp().run()
