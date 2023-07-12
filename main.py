import button as button
from kivy.core.text import LabelBase
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
# from kivy.core.window import Window
# Window.size = (350, 600)

import random
import dataloader as dt
class SelectGameButton(Button):
    bg_color = ListProperty([1, 1, 1, 0])

class AnswerButton(Button):
    bg_color = ListProperty([1, 1, 1, 1])

question = []
question_list = dt.data_from_csv(question)
class QaranApp(MDApp):

    selected_game = ''
    right_answer = ''
    correct = 0
    wrong = 0
    success_rate = 0


    def build(self):
        global screen_manager
        screen_manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('select_game.kv'))
        screen_manager.add_widget(Builder.load_file('quiz.kv'))
        screen_manager.add_widget(Builder.load_file('final_score.kv'))
        return screen_manager

    def select_game(self, game):
        self.selected_game = game
        question_random = random.choice(question)
        guestion1 = question_random[0]
        self.right_answer = question_random[1]
        answer_list = [self.right_answer]

        while len(answer_list) != 6:
            answer_random = random.choice(question)[1]
            if answer_random not in answer_list:
                answer_list.append(answer_random)

        random.shuffle(answer_list)

        screen_manager.get_screen('quiz').ids.question.text = f'{guestion1}'

        for i in range(1, 7):
            screen_manager.get_screen('quiz').ids[f'answer{i}'].text = f'{answer_list[i - 1]}'

        screen_manager.current ='quiz'

    answer_dict = {}
    def get_id(self, instance):
        for id, widget in instance.parent.parent.parent.ids.items():
            if widget.__self__ == instance:
                return id

    def quiz(self, answer, instance):
        if answer == self.right_answer:
            self.correct += 1
            screen_manager.get_screen('quiz').ids[self.get_id(instance)].bg_color = (0, 1, 0, 1)
            answer_id_list = ['answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6']
            answer_id_list.remove(self.get_id(instance))
            for i in range(0, 3):
                screen_manager.get_screen('quiz').ids[f'{answer_id_list[i]}'].disabled = True


        else:
            self.wrong += 1
            screen_manager.get_screen('quiz').ids[self.get_id(instance)].bg_color = (1, 0, 0, 0)
            for i in range(1, 7):
                if screen_manager.get_screen('quiz').ids[f'answer{i}'].text == self.right_answer:
                    screen_manager.get_screen('quiz').ids[f'answer{i}'].bg_color = (0, 1, 0, 1)
                else:
                    screen_manager.get_screen('quiz').ids[f'answer{i}'].disabled = True
            screen_manager.get_screen('quiz').ids[self.get_id(instance)].bg_color = (1, 0, 1, 0)
            screen_manager.get_screen('quiz').ids[self.get_id(instance)].disabled_color = (1, 1, 1, 1)
        screen_manager.get_screen('quiz').ids.correct_answer.text == f'верно {self.correct}'
        screen_manager.get_screen('quiz').ids.wrong_answer.text == f'верно {self.wrong}'
        # screen_manager.get_screen('quiz').correct.text = f'{self.wrong_answer} верно'

    def next_question(self):
        self.select_game(self.selected_game)

        for i in range(1, 7):
            screen_manager.get_screen('quiz').ids[f'answer{i}'].disabled = False
            screen_manager.get_screen('quiz').ids[f'answer{i}'].bg_color = (40/255, 6/255, 109/255, 1)
            screen_manager.get_screen('quiz').ids[f'answer{i}'].disabled_color = (1, 1, 1, 0.3)

    def replay(self):
        self.correct = 0
        self.wrong = 0
        screen_manager.current = 'main'
        print('новая игра')
    def final_score(self):
        if self.correct == 0 and self.wrong == 0:
            screen_manager.correct = 'main'
        else:
            for i in range(1, 7):
                screen_manager.get_screen('quiz').ids[f'answer{i}'].disabled = False
                screen_manager.get_screen('quiz').ids[f'answer{i}'].bg_color = (40 / 255, 6 / 255, 109 / 255, 1)
                screen_manager.get_screen('quiz').ids[f'answer{i}'].disabled_color = (1, 1, 1, 0.3)
            success_rate = round((self.correct/(self.correct+self.wrong)) * 100)
            screen_manager.get_screen('final_score').correct.text = f'{self.correct} - Верно'
            screen_manager.get_screen('final_score').wrong.text = f'{self.wrong} - Неверно'
            screen_manager.get_screen('final_score').success_rate.text = f'{success_rate}% верных ответов'

            screen_manager.current = 'final_score'


if __name__ == '__main__':
    QaranApp().run()