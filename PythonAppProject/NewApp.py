import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ChildApp(GridLayout):
    def __init__(self):  # **kwargs is used to add unlimited arguments
        super(ChildApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Student Mark'))
        self.s_mark = TextInput()
        self.add_widget(self.s_mark)

        self.add_widget(Label(text='Student Gender'))
        self.s_gen = TextInput()
        self.add_widget(self.s_gen)


class parentApp(App):
    def build(self):
        return ChildApp()


if __name__ == '--main__':
    parentApp().run()
