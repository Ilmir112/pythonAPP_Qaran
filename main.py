from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class QaranApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")



QaranApp().run()


