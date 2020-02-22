from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from latin import LatinRegularVerb
from kivy.core.window import Window
from random import shuffle


class ConjugationGame(BoxLayout):
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

    # CREATE SHUFFLED LISTS
    shuffled_list1 = []
    shuffled_list1.append(word1.pres_act_inf)
    shuffled_list1.append(word1.imp_sg)
    shuffled_list1.append(word1.imp_pl)
    shuffled_list1.extend(word1.pres_tense)
    shuffled_list1.extend(word1.fut_tense)
    shuffled_list1.extend(word1.imperf_tense)
    shuffle(shuffled_list1)

    shuffled_list2 = []
    shuffled_list2.append(word2.pres_act_inf)
    shuffled_list2.append(word2.imp_sg)
    shuffled_list2.append(word2.imp_pl)
    shuffled_list2.extend(word2.pres_tense)
    shuffled_list2.extend(word2.fut_tense)
    shuffled_list2.extend(word2.imperf_tense)
    shuffle(shuffled_list2)




class ConjugationApp(App):
    def build(self):
        Window.bind(on_key_down=self.key_down)
        Window.bind(on_key_up=self.key_up)
        return ConjugationGame()

    def key_down(self, key, scancode=None, *_):
        if scancode == 281:  # PAGE_DOWN
            print("PAGE_DOWN down")
        elif scancode == 280:  #PAGE_UP
            print("PAGE_UP down")
        elif scancode == 98:  # B
            print("B down")
        else:
            print("\nKey: {} (scancode {}) down".format(_[1], scancode))

    def key_up(self, key, scancode=None, *_):
        if scancode == 281:  # PAGE_DOWN
            print("PAGE_DOWN up")
        elif scancode == 280:  #PAGE_UP
            print("PAGE_UP up")
        elif scancode == 98:  # B
            print("B up")
        else:
            print("\nKey: {} (scancode {}) up".format(_, scancode))




if __name__ == "__main__":
    ConjugationApp().run()