from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from latin import LatinRegularVerb
from kivy.uix.widget import Widget



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
    pass

    # ON_KEY EVENTS
    pass



class ConjugationApp(App):
    def build(self):
        return ConjugationGame()


if __name__ == "__main__":
    ConjugationApp().run()