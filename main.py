from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from latin import LatinRegularVerb, SumLatinIrregularVerb, PossumLatinIrregularVerb
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from random import shuffle


def shuffle_list(word_obj):
    try:
        shuffled_list = [word_obj.pres_act_inf, word_obj.imp_sg, word_obj.imp_pl]
    except:
        shuffled_list = [word_obj.pres_act_inf]
    shuffled_list.extend(word_obj.pres_tense)
    shuffled_list.extend(word_obj.fut_tense)
    shuffled_list.extend(word_obj.imperf_tense)
    shuffle(shuffled_list)
    return shuffled_list


class ConjugationGame(BoxLayout):
    round = NumericProperty(1)
    game_state = NumericProperty(0)
    word1_showing = StringProperty("")
    word2_showing = StringProperty("")
    stem1 = StringProperty("")
    stem2 = StringProperty("")
    answer1 = StringProperty("")
    answer2 = StringProperty("")

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
    # word1 = LatinRegularVerb(*verb1)
    # word2 = LatinRegularVerb(*verb2)
    word1 = SumLatinIrregularVerb()
    word2 = PossumLatinIrregularVerb()

    word1_shuffled_list = shuffle_list(word1)
    word2_shuffled_list = shuffle_list(word2)

    # POP WORDS FROM SHUFFLED LISTS
    word1_selected = word1_shuffled_list.pop()
    word2_selected = word2_shuffled_list.pop()

    def change_round(self):
        # CHANGE ROUND
        if self.round > 3:
            self.round = 1
        else:
            self.round += 1

    def change_game_state(self):
        if self.game_state > 3:
            self.game_state = 1
            # CHECK LIST 1, REFRESH IF NECESSARY
            if len(self.word1_shuffled_list) > 0:
                self.word1_selected = self.word1_shuffled_list.pop()
            else:
                self.word1_shuffled_list = shuffle_list(self.word1)
                self.word1_selected = self.word1_shuffled_list.pop()
            # CHECK LIST 2, REFRESH IF NECESSARY
            if len(self.word2_shuffled_list) > 0:
                self.word2_selected = self.word2_shuffled_list.pop()
            else:
                self.word2_shuffled_list = shuffle_list(self.word2)
                self.word2_selected = self.word2_shuffled_list.pop()
        else:  # advance game state
            self.game_state += 1

        # DECIDE WHICH ASPECT TO SHOW

        #  Round 1: Translation
        if self.round == 1:
            self.stem1 = self.word1_selected[-2]
            self.stem2 = self.word2_selected[-2]
            self.answer1 = self.word1_selected[-1]
            self.answer2 = self.word2_selected[-1]

        # Round 2: Parsing
        elif self.round == 2:
            self.stem1 = self.word1_selected[-2]
            self.stem2 = self.word2_selected[-2]
            # REMOVE "PERSON" FROM ANSWER1 IF INFINITIVE OR IMPERATIVE
            if self.word1_selected[0] != "infinitive" and self.word1_selected[0] != "imperative":
                self.answer1 = self.word1_selected[0] + "\n" + \
                               self.word1_selected[1] + " person \n" + \
                               self.word1_selected[2]
            else:  # is infinitive or imperative
                self.answer1 = self.word1_selected[0] + "\n" + \
                               self.word1_selected[2]
            # REMOVE "PERSON" FROM ANSWER2 IF INFINITIVE OR IMPERATIVE
            if self.word2_selected[0] != "infinitive" and self.word2_selected[0] != "imperative":
                self.answer2 = self.word2_selected[0] + "\n" + \
                               self.word2_selected[1] + " person \n" + \
                               self.word2_selected[2]
            else:  # is infinitive or imperative
                self.answer2 = self.word2_selected[0] + "\n" + \
                               self.word2_selected[2]


        # Round 3: Parsing
        else:  # self.round == 3: CONJUGATION
            # REMOVE "PERSON" FROM ANSWER1 IF INFINITIVE OR IMPERATIVE
            if self.word1_selected[0] != "infinitive" and self.word1_selected[0] != "imperative":
                self.stem1 = self.word1_selected[0] + "\n" + \
                               self.word1_selected[1] + " person \n" + \
                               self.word1_selected[2]
            else:  # is infinitive or imperative
                self.stem1 = self.word1_selected[0] + "\n" + \
                               self.word1_selected[2]
            # REMOVE "PERSON" FROM ANSWER2 IF INFINITIVE OR IMPERATIVE
            if self.word2_selected[0] != "infinitive" and self.word2_selected[0] != "imperative":
                self.stem2 = self.word2_selected[0] + "\n" + \
                               self.word2_selected[1] + " person \n" + \
                               self.word2_selected[2]
            else:  # is infinitive or imperative
                self.stem2 = self.word2_selected[0] + "\n" + \
                               self.word2_selected[2]
            self.answer1 = self.word1_selected[-2]
            self.answer2 = self.word2_selected[-2]

        # DECIDE WHICH WORD TO SHOW
        if self.round != 3:
            if self.game_state == 0:
                self.word1_showing = ""
                self.word2_showing = ""
            elif self.game_state == 1:
                self.word1_showing = self.stem1
                self.word2_showing = ""
            elif self.game_state == 2:
                self.word1_showing = "{}\n[size=50]{}[/size]".format(self.stem1, self.answer1)
                self.word2_showing = ""
            elif self.game_state == 3:
                self.word1_showing = ""
                self.word2_showing = self.stem2
            elif self.game_state == 4:
                self.word1_showing = ""
                self.word2_showing = "{}\n[size=50]{}[/size]".format(self.stem2, self.answer2)
        else:  # round 4
            if self.game_state == 0:
                self.word1_showing = ""
                self.word2_showing = ""
            elif self.game_state == 1:
                self.word1_showing = "[size=50]{}[/size]\n".format(self.stem1)
                self.word2_showing = ""
            elif self.game_state == 2:
                self.word1_showing = "[size=50]{}[/size]\n{}".format(self.stem1, self.answer1)
                self.word2_showing = ""
            elif self.game_state == 3:
                self.word1_showing = ""
                self.word2_showing = "[size=50]{}[/size]\n".format(self.stem2)
            elif self.game_state == 4:
                self.word1_showing = ""
                self.word2_showing = "[size=50]{}[/size]\n{}".format(self.stem2, self.answer2)


class ConjugationApp(App):
    def build(self):
        Window.bind(on_key_down=self.key_down)
        # Window.bind(on_key_up=self.key_up)
        return ConjugationGame()

    def key_down(self, key, scancode=None, *_):
        if scancode == 281:  # PAGE_DOWN
            print("PAGE_DOWN pressed")
            ConjugationGame.change_game_state(self.root)
        elif scancode == 280:  # PAGE_UP
            print("PAGE_UP pressed")
        elif scancode == 98:  # B
            print("B pressed")
            ConjugationGame.change_round(self.root)
        else:
            print("\nKey: {} (scancode {}) pressed".format(_[1], scancode))

    # def key_up(self, key, scancode=None, *_):
    #     if scancode == 281:  # PAGE_DOWN
    #         print("PAGE_DOWN released")
    #     elif scancode == 280:  # PAGE_UP
    #         print("PAGE_UP released")
    #     elif scancode == 98:  # B
    #         print("B released")
    #     else:
    #         print("\nKey: {} (scancode {}) released".format(_, scancode))


if __name__ == "__main__":
    ConjugationApp().run()
