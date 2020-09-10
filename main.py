# Application written fully by Pavel on 14-15.06.2016

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import  Button
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,  Screen,  FadeTransition
from kivy.core.window import Window

class LoginScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 4
        self.row_force_default=True
        self.row_default_height=40
        self.spacing=5
        self.padding=10
        self.size_hint=(.5, .5)
        self.pos_hint={'center_x': .5, 'center_y': .2}
    
        self.add_widget(Label(text='[color=000000]System[/color]', markup=True))
        self.add_widget(Label(text=""))
        self.add_widget(Label(text='[color=000000]Login[/color]', markup=True))
        self.username = TextInput( multiline= False )
        self.add_widget(self.username)
        
        self.add_widget(Label(text='[color=000000]Password[/color]', markup=True))
        self.password = TextInput( multiline= False, password = True )
        self.add_widget(self.password)
        
        btn1 = Button(text = '[color=000000]Continue[/color]',markup=True,  background_color=(0,0,255, 1), font_size=20, pos = (10, 10), pos_hint={'center_x': 0.8} )
        btn1.bind(on_press=self.OnButton)
        self.add_widget(btn1)
        
    #callback
    def OnButton(self, instance):
        # check correctness of login / password and change the color of the button
        if self.username.text == 'admin':
            instance.background_color = (0,255,0, 1)    
        elif self.password.text == 'abcd':
            instance.background_color = (0,255,0, 1)    
        else:
            instance.background_color = (255,0,0, 1) 
        #More functionality might be extended here as per request ( to be continued )
        #print('Username <%s> is' % self.username.text)
        #print('Password <%s> is' % self.password.text)
      
class TestApp(App):
    
    def build(self):
         Window.clearcolor = (49, 138, 138, 1)
#         self.root = get_main_window()
#         with self.root.canvas:
#            Color(rgba=(.5, .5, .5))
#            Rectangle(size=self.root.size, pos=self.root.pos)
#    
         return LoginScreen()

    def update_widg(self, app, value):
        #self.btn.text = 'Hello ()'.format(self.cout)
        self.b = self.br
        return self.b
        
if __name__ == "__main__":
    TestApp().run()
