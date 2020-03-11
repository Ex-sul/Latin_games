from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from latin import LatinRegularVerb, SumLatinIrregularVerb, PossumLatinIrregularVerb
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from latin_settings import settings_json
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


class ConjugationGame(BoxLayout, FloatLayout):
    round = NumericProperty(1)
    round_name = StringProperty("Translation")
    game_state = NumericProperty(0)
    word1_showing = StringProperty("")
    word2_showing = StringProperty("")
    word3_showing = StringProperty("")
    stem1 = StringProperty("")
    stem2 = StringProperty("")
    stem3 = StringProperty("")
    answer1 = StringProperty("")
    answer2 = StringProperty("")
    answer3 = StringProperty("")

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
    # word2 = LatinRegularVerb(*verb2)
    word2 = SumLatinIrregularVerb()
    word3 = PossumLatinIrregularVerb()

    word1_shuffled_list = shuffle_list(word1)
    word2_shuffled_list = shuffle_list(word2)
    word3_shuffled_list = shuffle_list(word3)

    # POP WORDS FROM SHUFFLED LISTS
    word1_selected = word1_shuffled_list.pop()
    word2_selected = word2_shuffled_list.pop()
    word3_selected = word3_shuffled_list.pop()

    def change_round(self):
        # CHANGE ROUND
        if self.round > 2:
            self.round = 1
        else:
            self.round += 1
        # CHANGE ROUND NAME
        if self.round == 1:
            self.round_name = "Translation"
        elif self.round == 2:
            self.round_name = "Parsing"
        else:
            self.round_name = "Conjugation"

    def revert_game_state(self):
        if self.game_state >= 1:
            self.game_state -= 1
        self.show_words()

    def change_game_state(self):
        if self.game_state > 5:
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
            # CHECK LIST 3, REFRESH IF NECESSARY
            if len(self.word3_shuffled_list) > 0:
                self.word3_selected = self.word3_shuffled_list.pop()
            else:
                self.word3_shuffled_list = shuffle_list(self.word3)
                self.word3_selected = self.word3_shuffled_list.pop()
        else:  # advance game state
            self.game_state += 1
        self.show_words()

    def show_words(self):
        #  Round 1: Translation
        if self.round == 1:
            self.stem1 = self.word1_selected[-2]
            self.stem2 = self.word2_selected[-2]
            self.stem3 = self.word3_selected[-2]
            self.answer1 = self.word1_selected[-1]
            self.answer2 = self.word2_selected[-1]
            self.answer3 = self.word3_selected[-1]

        # Round 2: Parsing
        elif self.round == 2:
            self.stem1 = self.word1_selected[-2]
            self.stem2 = self.word2_selected[-2]
            self.stem3 = self.word3_selected[-2]
            # REMOVE "PERSON" FROM ANSWER 1 IF INFINITIVE OR IMPERATIVE
            if self.word1_selected[0] != "infinitive" and self.word1_selected[0] != "imperative":
                self.answer1 = self.word1_selected[0] + "\n" + \
                               self.word1_selected[1] + " person \n" + \
                               self.word1_selected[2]
            else:  # is infinitive or imperative
                self.answer1 = self.word1_selected[0] + "\n" + \
                               self.word1_selected[2]
            # REMOVE "PERSON" FROM ANSWER 2 IF INFINITIVE OR IMPERATIVE
            if self.word2_selected[0] != "infinitive" and self.word2_selected[0] != "imperative":
                self.answer2 = self.word2_selected[0] + "\n" + \
                               self.word2_selected[1] + " person \n" + \
                               self.word2_selected[2]
            else:  # is infinitive or imperative
                self.answer2 = self.word2_selected[0] + "\n" + \
                               self.word2_selected[2]
            # REMOVE "PERSON" FROM ANSWER 3 IF INFINITIVE OR IMPERATIVE
            if self.word3_selected[0] != "infinitive" and self.word3_selected[0] != "imperative":
                self.answer3 = self.word3_selected[0] + "\n" + \
                               self.word3_selected[1] + " person \n" + \
                               self.word3_selected[2]
            else:  # is infinitive or imperative
                self.answer3 = self.word3_selected[0] + "\n" + \
                               self.word3_selected[2]

        # Round 3: Parsing
        else:  # self.round == 3: CONJUGATION
            # REMOVE "PERSON" FROM ANSWER 1 IF INFINITIVE OR IMPERATIVE
            if self.word1_selected[0] != "infinitive" and self.word1_selected[0] != "imperative":
                self.stem1 = self.word1_selected[0] + "\n" + \
                               self.word1_selected[1] + " person \n" + \
                               self.word1_selected[2]
            else:  # is infinitive or imperative
                self.stem1 = self.word1_selected[0] + "\n" + \
                               self.word1_selected[2]
            # REMOVE "PERSON" FROM ANSWER 2 IF INFINITIVE OR IMPERATIVE
            if self.word2_selected[0] != "infinitive" and self.word2_selected[0] != "imperative":
                self.stem2 = self.word2_selected[0] + "\n" + \
                               self.word2_selected[1] + " person \n" + \
                               self.word2_selected[2]
            else:  # is infinitive or imperative
                self.stem2 = self.word2_selected[0] + "\n" + \
                               self.word2_selected[2]
            # REMOVE "PERSON" FROM ANSWER 3 IF INFINITIVE OR IMPERATIVE
            if self.word3_selected[0] != "infinitive" and self.word3_selected[0] != "imperative":
                self.stem3 = self.word3_selected[0] + "\n" + \
                               self.word3_selected[1] + " person \n" + \
                               self.word3_selected[2]
            else:  # is infinitive or imperative
                self.stem3 = self.word3_selected[0] + "\n" + \
                               self.word3_selected[2]
            self.answer1 = self.word1_selected[-2]
            self.answer2 = self.word2_selected[-2]
            self.answer3 = self.word3_selected[-2]

        # DECIDE WHICH WORD TO SHOW ####################################################################################
        if self.round != 3:
            if self.game_state == 0:
                self.word1_showing = ""
                self.word2_showing = ""
                self.word3_showing = ""
            elif self.game_state == 1:
                self.word1_showing = self.stem1
                self.word2_showing = ""
                self.word3_showing = ""
            elif self.game_state == 2:
                self.word1_showing = "{}\n[size=50]{}[/size]".format(self.stem1, self.answer1)
                self.word2_showing = ""
                self.word3_showing = ""
            elif self.game_state == 3:
                self.word1_showing = ""
                self.word2_showing = self.stem2
                self.word3_showing = ""
            elif self.game_state == 4:
                self.word1_showing = ""
                self.word2_showing = "{}\n[size=50]{}[/size]".format(self.stem2, self.answer2)
                self.word3_showing = ""
            elif self.game_state == 5:
                self.word1_showing = ""
                self.word2_showing = ""
                self.word3_showing = self.stem3
            elif self.game_state == 6:
                self.word1_showing = ""
                self.word2_showing = ""
                self.word3_showing = "{}\n[size=50]{}[/size]".format(self.stem3, self.answer3)
        else:  # round 3
            if self.game_state == 0:
                self.word1_showing = ""
                self.word2_showing = ""
                self.word3_showing = ""
            elif self.game_state == 1:
                self.word1_showing = " \n[size=50]{}[/size]".format(self.stem1)
                self.word2_showing = ""
                self.word3_showing = ""
            elif self.game_state == 2:
                self.word1_showing = "{}\n[size=50]{}[/size]".format(self.answer1, self.stem1)
                self.word2_showing = ""
                self.word3_showing = ""
            elif self.game_state == 3:
                self.word1_showing = ""
                self.word2_showing = " \n[size=50]{}[/size]".format(self.stem2)
                self.word3_showing = ""
            elif self.game_state == 4:
                self.word1_showing = ""
                self.word2_showing = "{}\n[size=50]{}[/size]".format(self.answer2, self.stem2)
                self.word3_showing = ""
            elif self.game_state == 5:
                self.word1_showing = ""
                self.word2_showing = ""
                self.word3_showing = " \n[size=50]{}[/size]".format(self.stem3)
            elif self.game_state == 6:
                self.word1_showing = ""
                self.word2_showing = ""
                self.word3_showing = "{}\n[size=50]{}[/size]".format(self.answer3, self.stem3)
                pass


class ConjugationApp(App):
    def build(self):
        self.use_kivy_settings = False
        Window.bind(on_key_down=self.key_down)
        # Window.bind(on_key_up=self.key_up)
        Window.fullscreen = 'auto'
        return ConjugationGame()

    def key_down(self, key, scancode=None, *_):
        if scancode == 281:  # PAGE_DOWN
            print("PAGE_DOWN pressed")
            ConjugationGame.change_game_state(self.root)
        elif scancode == 280:  # PAGE_UP
            print("PAGE_UP pressed")
            ConjugationGame.revert_game_state(self.root)
        elif scancode == 98:  # B
            print("B pressed")
            ConjugationGame.change_round(self.root)
        elif scancode == 115:  # S
            App.open_settings(self)
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

    def build_config(self, config):
        config.setdefaults('General Settings', {
            'Game Mode': 'Present System',
            'Number of Words to Display': "Two",
            'firstword': 'laudo, laudāre, laudavi, laudatum, to praise',
            'secondword': 'habeo, habēre, habui, habitum, to have',
            'thirdword': 'disco, discere, didici, to learn'
        })

    def build_settings(self, settings):
        settings.add_json_panel('General Settings',
                                self.config,
                                data=settings_json)


if __name__ == "__main__":
    ConjugationApp().run()
