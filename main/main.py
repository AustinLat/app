import kivy

from plyer import gps
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class MyApp(App): 
    def build(self):
        #layout = BoxLayout(padding=10, orientation='vertical', row_default_height='48pd', row_force_default=True, spacing=10)
        
        layoutgrid = GridLayout(cols=1, size_hint_y=None, height= self.minimum_height)
  
        self.txt1 = TextInput(multiline=False)
        self.txt1.bind(text = self.on_text)
        layoutgrid.add_widget(self.txt1) 

        self.btn1 = Button(text="OK")
        self.btn1.bind(on_press=self.buttonClicked)
        layoutgrid.add_widget(self.btn1)

        #self.scroll = ScrollView(size=self.size)
        #layout.add_widget(self.scroll)
 
        return layout

    def on_start(self):
        gps.configure(on_location=self.on_gps_location)
        gps.start()
        self.site_dict = {}
        with open("site_locations.txt", "r") as r:
            datas = r.readlines()
            for line in datas:
                (key, val) = line.split()
                self.site_dict[key] = val  
        self.site_list = [key for key, value in self.site_dict.items()]

    #def dict_lister(self, **kwargs):
        #site_list = [key for key, value in self.site_dict.items()]
        #for site in site_list:
        #    btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
        #    btn.bind(on_release=lambda btn: self.drop.select(btn.text))
        #    drop.add_widget(btn)
        
    def on_text(self, instance, value):
        self.site_name = value
 
    def buttonClicked(self, btn):
        f = open("site_locations.t:xt","a+")
        f.write(f'{self.site_name} {self.gps_location}\n')
        f.close()

    def on_gps_location(self, **kwargs):
        lat = kwargs['lat']
        lon = kwargs['lon']
        #lat = '{lat}'.format(**kwargs)
        #lon = '{lon}'.forman(**kwargs)
        self.gps_location = f'{lat},{lon}'
 
    def on_stop(self):
        gps.stop()


if __name__ == "__main__":
    MyApp().run()
