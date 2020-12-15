# This will be an app to mark site locations and later perhaps 
# add notes like gate codes and maybe even pictures.

from kivy.app import App
from kivy.uix.button import Button


class ButtonApp(App):
 
    def build(self):
        return Button()

    def on_press_button(self):
        print('You pressed the button!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
