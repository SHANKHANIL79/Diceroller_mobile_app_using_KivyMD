from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton,MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
import random
Window.size=(393,600)
class DiceApp(MDApp):
    def Choose(self,args):
        outcome=[1,2,3,4,5,6]
        if self.state==0:
            result=random.choice(outcome)
            self.label.text=str(result)
        else:
            result=random.choice(outcome)
            self.label.text=str(result)

    def build(self):
        self.state=0
        self.theme_cls.primary_palette="DeepOrange"
        self.theme_cls.theme_style = "Dark"
        self.toolbar=MDTopAppBar(title="Press the button to Roll Your Dice")
        self.toolbar.pos_hint={"top":1}
        screen=MDScreen()
        screen.add_widget(self.toolbar)
        screen.add_widget(Image(source="diceroll.gif",pos_hint={"center_x":0.5,"center_y":0.75}))
        self.label=MDLabel(
            text="Result",
            halign="center",
            pos_hint={"center_x":0.5,"center_y":0.5},
            theme_text_color="Secondary",
            font_style="H1"
        )        
        screen.add_widget(MDFillRoundFlatButton(
            text="ROLL",
            font_size=60,
            pos_hint={"center_x":0.5,"center_y":0.1},
            on_press=self.Choose
        ))
        screen.add_widget(self.label)

        return screen
   

if __name__=="__main__":
    DiceApp().run()