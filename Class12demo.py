print("Hello World")
import kivymd
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

class DemoApp(App):
    def build(self):
        return Button(text="Hello World!")
    
MyApp().run()