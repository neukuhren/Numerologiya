from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class NumerologiyaApp(MDApp):
    def build(self):
        return MDLabel(text="Numerologiya", halign="center")


NumerologiyaApp().run()