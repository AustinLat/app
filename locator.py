# This will be an app to mark site locations and later perhaps 
# add notes like gate codes and maybe even pictures.

from kivy.app import App
from kivy.uic.label import Label

class Locator(App):
    
    def location(self):
        label = Label(text = 'Hello',
                      size_hint=(.5, .5},
                      pos_hint={'center_x': .5, 'center_y': .5})
        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()
