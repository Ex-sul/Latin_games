from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from latin import LatinRegularVerb
from kivy.core.window import Window
from random import shuffle


def shuffle_list(word_obj):
    shuffled_list = [word_obj.pres_act_inf, word_obj.imp_sg, word_obj.imp_pl]
    shuffled_list.extend(word_obj.pres_tense)
    shuffled_list.extend(word_obj.fut_tense)
    shuffled_list.extend(word_obj.imperf_tense)
    shuffle(shuffled_list)
    return shuffled_list


class ConjugationGame(BoxLayout):
    round = 1
    game_state = 0

    # FIRST VERB
    verb1_lex = "laudo, laudāre, laudavi, laudatum, to praise"
    verb1_trans = "praise"
    verb1_trans_3rd = "praises"
    verb1_trans_imperf = "praising"
    verb1 = [verb1_lex, verb1_trans, verb1_trans_3rd, verb1_trans_imperf]

    # SECOND VERB
    verb2_lex = "habeo, habēre, habui, habitum, to have"
    verb2_trans = "have"
    verb2_trans_3rd = "has"
    verb2_trans_imperf = "having"
    verb2 = [verb2_lex, verb2_trans, verb2_trans_3rd, verb2_trans_imperf]

    # CREATE CLASS OBJECTS
    word1 = LatinRegularVerb(*verb1)
    word2 = LatinRegularVerb(*verb2)

    word1_shuffled_list = shuffle_list(word1)
    word2_shuffled_list = shuffle_list(word2)

    # POP WORDS FROM SHUFFLED LISTS
    word1_selected = word1_shuffled_list.pop()
    word2_selected = word2_shuffled_list.pop()

    word1_showing = word1_selected[-2]
    word2_showing = word2_selected[-2]


class ConjugationApp(App):
    def build(self):
        Window.bind(on_key_down=self.key_down)
        Window.bind(on_key_up=self.key_up)
        return ConjugationGame()

    def key_down(self, key, scancode=None, *_):
        if scancode == 281:  # PAGE_DOWN
            print("PAGE_DOWN pressed")
        elif scancode == 280:  # PAGE_UP
            print("PAGE_UP pressed")
        elif scancode == 98:  # B
            print("B pressed")
        else:
            print("\nKey: {} (scancode {}) pressed".format(_[1], scancode))

    def key_up(self, key, scancode=None, *_):
        if scancode == 281:  # PAGE_DOWN
            print("PAGE_DOWN released")
        elif scancode == 280:  # PAGE_UP
            print("PAGE_UP released")
        elif scancode == 98:  # B
            print("B released")
        else:
            print("\nKey: {} (scancode {}) released".format(_, scancode))


if __name__ == "__main__":
    ConjugationApp().run()
