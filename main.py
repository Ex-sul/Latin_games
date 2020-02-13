from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ConjugationGame(BoxLayout):
    pass


class ConjugationApp(App):
    def build(self):
        return ConjugationGame()


if __name__ == "__main__":
    ConjugationApp().run()