# This will be an app to mark site locations and later perhaps 
# add notes like gate codes and maybe even pictures.

from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
 
    def build(self):
        return Label(text='Hello',
                size_hint= (.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5})

if __name__ == '__main__':
    app = MainApp()
    app.run()
