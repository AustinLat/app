
import kivy
from plyer import gps
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(App):    
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        
        self.lbl1 = Label(text="Enter site name")
        layout.add_widget(self.lbl1)
        
        self.txt1 = TextInput(multiline=False)
        self.txt1.bind(text = self.on_text)
        layout.add_widget(self.txt1)
        
        return layout

    def on_start(self):
        gps.configure(on_location=self.on_gps_location)
        gps.start()

    def on_text(self, instance, value):
        self.site_name = value
        
    def buttonClicked(self, btn): 
        f = open("site_locations.txt","a+")
        f.write(f'{self.site_name} : {self.gps_location}\n')
        f.close()

    def on_gps_location(self, **kwargs):
        lat = kwargs['lat']
        lon = kwargs['lon']
        self.gps_location = f'{lat} {lon}'

    def on_stop(self):
        gps.stop()

# run app
if __name__ == "__main__":
    MyApp().run()


