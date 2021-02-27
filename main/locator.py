# This will be an app to mark site locations and later perhaps 
# add notes like gate codes and maybe even pictures.
#try:
#    from kivy.app import App
#except ImportError:
#    import pip._internal as pip
#    pip.main(['install', 'kivy'])
#    from kivy.app import App
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

class ButtonApp(App):
 
    def build(self): 
        return Button()

    def on_press_button(self):
        print('Recording site location')
        f = open("site_locations.txt","a+")
        f.write("Site name : GPS data\n")
        f.close()

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
