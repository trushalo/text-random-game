from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout


Builder.load_file('kivy.kv')

kivy_comment_1 = 'Stuff'
kivy_comment_2 = 'Test'
kivy_comment_3 = 'Whats'
kivy_comment_4 = 'Happening'
kivy_comment_5 = 'Here'

comments = [kivy_comment_5, kivy_comment_4, kivy_comment_3, kivy_comment_2, kivy_comment_1]

class KivyApp(App):
    def build(self):
        return GridLayout()


class MyGridLayout(GridLayout):
    pass


if __name__ == '__main__':
    KivyApp().run()
