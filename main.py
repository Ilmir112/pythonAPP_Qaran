import button as button
from kivy.core.text import LabelBase
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (350, 600)

import random
import dataloader as dt
class SelectGameButton(Button):
    bg_color = ListProperty([1, 1, 1, 0])

class OptionButton(Button):
    bg_color = ListProperty([1, 1, 1, 1])

question = []
question_list = dt.data_from_csv(question)
class QaranApp(MDApp):

    selected_game = ''
    right_answer = ''

    def build(self):
        global screen_manager
        screen_manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('select_game.kv'))
        screen_manager.add_widget(Builder.load_file('quiz.kv'))
        #screen_manager.add_widget(Builder.load_file('final_score.kv'))
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
            screen_manager.get_screen('quiz').ids[f'option{i}'].text = f'{answer_list[i - 1]}'

        screen_manager.current ='quiz'

    def get_id(self, instance):
        print(instance.parent.parent.parent)

    def quiz(self, option, instance):
        print(option, self.get_id(instance))

    def next_question(self):
        pass

if __name__ == '__main__':
    QaranApp().run()