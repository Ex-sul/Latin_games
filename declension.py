from latin import LatinNoun
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from random import shuffle


def shuffle_list(noun_obj):
    noun_list = noun_obj.declined_list[:]
    shuffle(noun_list)
    return noun_list

def make_parsing_round_set(noun_obj):
    list_to_shuffle = []
    poppable_set = set()
    for declined_list in noun_obj.declined_list[:]:
        list_to_shuffle.append(declined_list[2])
    shuffle(list_to_shuffle)
    for e in list_to_shuffle:
        poppable_set.add(e)
    return poppable_set

def find_all_matches(noun_selected_parsing, noun_obj):
    matches = []
    for t in noun_obj.declined_list:
        if t[2] == noun_selected_parsing:
            matches.append(t)
    return matches

class DeclensionGame(BoxLayout, FloatLayout):
    round = NumericProperty(1)
    round_name = StringProperty("Declining")
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

    # lexical_entry, transl_sg, transl_pl
    noun1 = ["rosa, rosae, f., rose", "rose", "roses"]
    noun2 = ["amicus, amici, m., friend", "friend", "friends"]
    noun3 = ["labor, laboris, m., labor, work", "labor", "labors"]

    # create class objects and shuffled lists
    noun1_obj = LatinNoun(*noun1)
    noun2_obj = LatinNoun(*noun2)
    noun3_obj = LatinNoun(*noun3)

    noun1_shuffled = shuffle_list(noun1_obj)
    noun2_shuffled = shuffle_list(noun2_obj)
    noun3_shuffled = shuffle_list(noun3_obj)

    # pop initial nouns
    noun1_selected = noun1_shuffled.pop()
    noun2_selected = noun2_shuffled.pop()
    noun3_selected = noun3_shuffled.pop()

    # things for parsing round
    noun1_set = make_parsing_round_set(noun1_obj)
    noun2_set = make_parsing_round_set(noun2_obj)
    noun3_set = make_parsing_round_set(noun3_obj)

    noun1_selected_parsing = noun1_set.pop()
    noun2_selected_parsing = noun2_set.pop()
    noun3_selected_parsing = noun3_set.pop()

    noun1_possibs = find_all_matches(noun1_selected_parsing, noun1_obj)
    noun2_possibs = find_all_matches(noun2_selected_parsing, noun2_obj)
    noun3_possibs = find_all_matches(noun3_selected_parsing, noun3_obj)

    def display_possibles(self, noun_possibs):
        possibilities = []
        for p in noun_possibs:
            possibilities.append("{} {}\n".format(p[0], p[1]))
        return "".join(possibilities)

    def change_round(self):
        # change round
        if self.round > 2:
            self.round = 1
        else:
            self.round += 1
        # change round name
        if self.round == 1:
            self.round_name = "Declining"
        elif self.round == 2:
            self.round_name = "Parsing"
        else:
            self.round_name = "Translation"

    def revert_game_state(self):
        if self.game_state >= 1:
            self.game_state -= 1
        self.show_words()

    def change_game_state(self):
        if self.game_state > 5:
            self.game_state = 1
            # get new word (Rounds 1 & 3)
            if self.round != 2:
                if len(self.noun1_shuffled) == 0:
                    self.noun1_shuffled = shuffle_list(self.noun1_obj)
                if len(self.noun2_shuffled) == 0:
                    self.noun2_shuffled = shuffle_list(self.noun2_obj)
                if len(self.noun3_shuffled) == 0:
                    self.noun3_shuffled = shuffle_list(self.noun3_obj)
                self.noun1_selected = self.noun1_shuffled.pop()
                self.noun2_selected = self.noun2_shuffled.pop()
                self.noun3_selected = self.noun3_shuffled.pop()

            # get new word (Round 2)
            else:
                if len(self.noun1_set) == 0:
                    self.noun1_set = make_parsing_round_set(self.noun1_obj)
                if len(self.noun2_set) == 0:
                    self.noun2_set = make_parsing_round_set(self.noun2_obj)
                if len(self.noun3_set) == 0:
                    self.noun3_set = make_parsing_round_set(self.noun3_obj)
                self.noun1_selected_parsing = self.noun1_set.pop()
                self.noun2_selected_parsing = self.noun2_set.pop()
                self.noun3_selected_parsing = self.noun3_set.pop()
                self.noun1_possibs = find_all_matches(self.noun1_selected_parsing, self.noun1_obj)
                self.noun2_possibs = find_all_matches(self.noun2_selected_parsing, self.noun2_obj)
                self.noun3_possibs = find_all_matches(self.noun3_selected_parsing, self.noun3_obj)
        else:  # advance game state
            self.game_state += 1
        self.show_words()

    def show_words(self):
        # SELECT THE INDEX BASED ON ROUND
        # Round 1: Declining
        if self.round == 1:
            self.stem1 = f"{self.noun1_selected[0]} {self.noun1_selected[1]}"
            self.stem2 = f"{self.noun2_selected[0]} {self.noun2_selected[1]}"
            self.stem3 = f"{self.noun3_selected[0]} {self.noun3_selected[1]}"
            self.answer1 = self.noun1_selected[2]
            self.answer2 = self.noun2_selected[2]
            self.answer3 = self.noun3_selected[2]

        # Round 2: Parsing
        elif self.round == 2:
            self.stem1 = self.noun1_selected_parsing
            self.stem2 = self.noun2_selected_parsing
            self.stem3 = self.noun3_selected_parsing
            self.answer1 = self.display_possibles(self.noun1_possibs)
            self.answer2 = self.display_possibles(self.noun2_possibs)
            self.answer3 = self.display_possibles(self.noun3_possibs)

        # Round 3: Translation
        else:  # self.round == 3:
            self.stem1 = f"[size=70]{self.noun1_selected[2]}[/size], " \
                         f"\n[size=50]{self.noun1_selected[0]} " \
                         f"{self.noun1_selected[1]}[/size]\n"
            self.stem2 = f"[size=70]{self.noun2_selected[2]}[/size], " \
                         f"\n[size=50]{self.noun2_selected[0]} " \
                         f"{self.noun2_selected[1]}[/size]\n"
            self.stem3 = f"[size=70]{self.noun3_selected[2]}[/size], " \
                         f"\n[size=50]{self.noun3_selected[0]} " \
                         f"{self.noun3_selected[1]}[/size]\n"
            self.answer1 = self.noun1_selected[-1]
            self.answer2 = self.noun2_selected[-1]
            self.answer3 = self.noun3_selected[-1]

        # SHOW WORDS
        if self.round != 2:
            if self.game_state == 0:
                self.word1_showing = ""
                self.word2_showing = ""
                self.word3_showing = ""
            # Show First Word
            elif self.game_state == 1:
                self.word1_showing = self.stem1
                self.word2_showing = ""
                self.word3_showing = ""
            elif self.game_state == 2:
                self.word1_showing = "{}\n[size=70]{}[/size]".format(self.stem1, self.answer1)
                self.word2_showing = ""
                self.word3_showing = ""
            # Show Second Word
            elif self.game_state == 3:
                self.word2_showing = self.stem2
                self.word3_showing = ""
            elif self.game_state == 4:
                self.word2_showing = "{}\n[size=70]{}[/size]".format(self.stem2, self.answer2)
                self.word3_showing = ""
            # Show Third Word
            elif self.game_state == 5:
                self.word3_showing = self.stem3
            elif self.game_state == 6:
                self.word3_showing = "{}\n[size=70]{}[/size]".format(self.stem3, self.answer3)
        else:
            if self.game_state == 0:
                self.word1_showing = ""
                self.word2_showing = ""
                self.word3_showing = ""
                # Show First Word
            elif self.game_state == 1:
                self.word1_showing = "[size=70]{}[/size]".format(self.stem1)
                self.word2_showing = ""
                self.word3_showing = ""
            elif self.game_state == 2:
                self.word1_showing = "[size=70]{}[/size]\n{}".format(self.stem1, self.answer1)
                self.word2_showing = ""
                self.word3_showing = ""
                # Show Second Word
            elif self.game_state == 3:
                self.word2_showing = "[size=70]{}[/size]".format(self.stem2)
                self.word3_showing = ""
            elif self.game_state == 4:
                self.word2_showing = "[size=70]{}[/size]\n{}".format(self.stem2, self.answer2)
                self.word3_showing = ""
                # Show Third Word
            elif self.game_state == 5:
                self.word3_showing = "[size=70]{}[/size]".format(self.stem3)
            elif self.game_state == 6:
                self.word3_showing = "[size=70]{}[/size]\n{}".format(self.stem3, self.answer3)


class DeclensionApp(App):
    def build(self):
        Window.bind(on_key_down=self.key_down)
        Window.fullscreen = 'auto'
        return DeclensionGame()

    def key_down(self, key, scancode=None, *_):
        if scancode == 281:  # PAGE_DOWN
            DeclensionGame.change_game_state(self.root)
        elif scancode == 98:  # B
            DeclensionGame.change_round(self.root)


if __name__ == "__main__":
    DeclensionApp().run()