import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty, NumericProperty
from random import shuffle

df = pd.read_excel(r'vocab1-8.xlsx')
tuples = [tuple(x) for x in df.to_numpy()]
vocab_one_through_seven = []


def fill_list():
    for t in tuples:
        if t[0] < 8:
            vocab_one_through_seven.append(t)
    shuffle(vocab_one_through_seven)


fill_list()


class AroundTheWorld(BoxLayout):
    game_state = NumericProperty(0)
    word_showing = vocab_one_through_seven.pop()
    word_history = ListProperty()
    stem = StringProperty("Around the World")
    answer = StringProperty("Vocabulary 1-7")

    def change_game_state(self):
        if self.game_state > 1:
            self.game_state = 1
        else:
            self.game_state += 1
        self.display_word()
        print(self.game_state)

    def display_word(self):
        if self.game_state == 1:
            self.stem = self.word_showing[-2]
            self.answer = ""
        elif self.game_state == 2:
            self.stem = self.word_showing[-2]
            self.answer = self.word_showing[-1]
            self.pop_next_word()

    def pop_next_word(self):
        if len(vocab_one_through_seven) > 0:
            self.word_showing = vocab_one_through_seven.pop()
        else:
            fill_list()
            self.word_showing = vocab_one_through_seven.pop()



class AroundTheWorldApp(App):
    def build(self):
        Window.bind(on_key_down=self.key_down)
        Window.fullscreen = 'auto'
        return AroundTheWorld()

    def key_down(self, key, scancode=None, *_):
        if scancode == 281:  # PAGE_DOWN
            AroundTheWorld.change_game_state(self.root)


if __name__ == "__main__":
    AroundTheWorldApp().run()
