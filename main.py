import imp
from kivymd.app import MDApp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty

Config.set("graphics", "width","300")
Config.set("graphics", "height","620")

class LegpieceDesign(MDBoxLayout):
    pass

class TitleBarButton(ButtonBehavior, MDBoxLayout):
    text = StringProperty("")
    icon = StringProperty()

class DisplayCard(MDBoxLayout):
    value = StringProperty()
    text = StringProperty()
    pass

class LegpieceApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return LegpieceDesign()


if __name__ == "__main__":
    LegpieceApp().run()