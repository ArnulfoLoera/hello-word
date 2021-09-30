import kivy
kivy.require('1.0.7')

from kivy.app import App


class PruebaApp(App):
    pass


if __name__ == '__main__':
    PruebaApp().run()


#File Test.kv

#:kivy 1.0

Button:
    text: 'Hello Desde Test.kv'
