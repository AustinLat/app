import kivy

from plyer import gps
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MainWidget(GridLayout):
    pass

class MyApp(App): 
 
def build(self): 
        return MainWidget()

    def on_start(self):
        gps.configure(on_location=self.on_gps_location)
        gps.start()
        self.site_dict = {}
        with open("site_locations.txt", "r+") as r:
            datas = r.readlines()
            for line in datas:
                (key, val) = line.split()
                self.site_dict[key] = val 
        self.site_list = [key for key, value in self.site_dict.items()] 

    def text_capture(self):
        self.site_name = self.root.ids.tinput.text  
 
    def site_pop(self):
        self.site_dict = {}
        with open("site_locations.txt", "r+") as r:
            datas = r.readlines()
            for line in datas:
                (key, val) = line.split()
                self.site_dict[key] = val 
        self.site_list = [key for key, value in self.site_dict.items()] 
        for site in self.site_list:
            button = Button(text=site, height=100, size_hint_y=None)
            button.bind(on_press=self.gps_button) 
            self.root.ids.scroll.add_widget(button)

    def gps_button(self, instance):
        self.root.ids.my_custom_label.text = self.site_dict[instance.text] 
 
    def buttonClicked(self):
        f = open("site_locations.txt","a+")
        f.write(f'{self.site_name} {self.gps_location}\n')
        f.close()

    def on_gps_location(self, **kwargs):
        lat = kwargs['lat']
        lon = kwargs['lon']
        self.gps_location = f'{lat},{lon}'
 
    def on_stop(self):
        gps.stop()

if __name__ == "__main__":
    MyApp().run()
