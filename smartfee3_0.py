import kivy
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import matplotlib.pyplot as plt
import numpy as np
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.graphics import Color, Rectangle
from kivy.graphics.vertex_instructions import RoundedRectangle 

class loginScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.loginlayout=FloatLayout(size=(720,1568))
        
        self.username=TextInput(
        hint_text="please input your user name",pos=(110,1075),size_hint=(None,None),size=(500,50))
        
        
        self.loginintrolbl=Label(
        text="Sign in to  your Account",
        size_hint=(None,None),size=(500,50),
        pos=(110,1250)
        
        )
        
        self.useremail=TextInput(
        hint_text="Email",
        size_hint=(None,None),size=(400,50),
        pos=(160,975)
        )
        
        self.userpassword=TextInput(
        hint_text="Your password ",
        size_hint=(None,None),
        size=(300,100),
        pos=(210,850)
        )
        
        self.userconfirmedpass=TextInput(
        hint_text="Recheck your password ",
        size_hint=(None,None),
        size=(300,100),
        pos=(210,730)
        )
        
        self.signinbtt=Button(
        size_hint=(None,None),
        text="Sign in",
        size=(200,50),
        pos=(260,575),
        background_normal="",
        background_color=(0,0,0,0)
        )
        
        self.signinbtt.bind(
        on_press=self.Login
        )
        
        with self.signinbtt.canvas.before:
            Color(0,0,0,1)
            RoundedRectangle(
            size=self.signinbtt.size,
            pos=self.signinbtt.pos,
            radius=[15]    
            
            
            )
            
        
        
        self.add_widget(
          self.loginlayout
        )
        
        self.loginlayout.add_widget(
          self.username
        )
        
        self.loginlayout.add_widget(
          self.loginintrolbl
        )
        
        self.loginlayout.add_widget(
        self.useremail
        )
        
        self.loginlayout.add_widget(
        self.userpassword
        )
        
        self.loginlayout.add_widget(
        self.userconfirmedpass
        )
        
        self.loginlayout.add_widget(
        self.signinbtt
        )
        
        
        
        
        
        with self.loginlayout.canvas.before:
            Color(255,242,0,1)
            Rectangle(
            size=self.loginlayout.size
            
            
            )
            
    def Login(self,instance):
        if self.userpassword.text == self.userconfirmedpass.text and self.username.text and self.useremail.text and self.userpassword.text and self.userconfirmedpass.text:
            self.manager.current="dashboard"
            
        else:
            self.error1=Label(
            text="\nplease enter valid words and\nmake sure your password\nand confirmed password are the same",
            size_hint=(None,None),
            size=(50,50),
            pos=(335,175)
            )
            
            self.loginlayout.add_widget(
            self.error1
            )
            Clock.schedule_once(
            self.clear_error1,
            5
            )
            
    def clear_error1(self,instance):
            self.loginlayout.remove_widget(
            self.error1
            )
            
class dashboardScreen(Screen):
        
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            
            self.dashlayout=GridLayout(
            cols=1,
            size_hint=(None,None ),
            size=(720,1200)
            )
            
            self.dashsublayout=FloatLayout(
            size=(720,200),
            pos=(0,1200),
            size_hint=(None,None)
            )
            
            self.dashsublayout1=GridLayout(
            cols=1,
            size=(720,400),
            pos=(0,200),
            size_hint=(None,None)
            )
            
            self.dashlayout.add_widget(
            self.dashsublayout
            )
            self.add_widget(self.dashlayout)
            self.avmoneyl=Label(
            text='Your available money is:'
            )
            
            self.totalincomel=Label(
            text="Total income:"
            )
            
            self.totalspendingl=Label(
            text="total spendings:"
            )
            
            self.currentsavingsl=Label(
            text="current savings:"
            )
            
            self.currentsavingsgoall=Label(
            text="current savings goal:"
            )
            
            self.recenttransacl=Label(
            text="Recent transactions:"
            )
            
            self.ispl=Label(
            text="important spending insights:"
            )
            
            
            self.moneytransacbtt=Button(
            text="Add income"
            )
            
            self.moneytransacbtt.bind(
            on_press=self.go_income
            )
            
            self.Analyticsbtt=Button(
            text="Analytics"
            )
            
            self.savinggoalsbtt=Button(
            text="Savings goals"
            )
            
            self.insightsbtt=Button(
            text="insights"
            )
            
            self.addexpensebtt=Button(
            text="Add expense"
            )
            
            self.addexpensebtt.bind(
            on_press=self.go_expense
            )
            
            self.dashlayout.add_widget(
            self.avmoneyl
            )
            
            self.dashlayout.add_widget(
            self.totalincomel
            )
            
            self.dashlayout.add_widget(
            self.totalspendingl
            )
            
            self.dashlayout.add_widget(
            self.currentsavingsl
            )
            
            self.dashlayout.add_widget(
            self.currentsavingsgoall
            )
            
            self.dashlayout.add_widget(
            self.recenttransacl
            )
            
            self.dashlayout.add_widget(
            self.ispl
            )
            
            self.dashlayout.add_widget(
            self.dashsublayout1
            )
            
            self.dashsublayout1.add_widget(
            self.moneytransacbtt
            )
            
            self.dashsublayout1.add_widget(
            self.Analyticsbtt
            )
            
            self.dashsublayout1.add_widget(
            self.savinggoalsbtt
            )
            
            self.dashsublayout1.add_widget(
            self.insightsbtt
            )
            
            self.dashsublayout1.add_widget(
            self.addexpensebtt
            )
            
            
            with self.dashsublayout.canvas.before:
                Color(0,1,0,0.5)
                Rectangle(
                size=self.dashsublayout.size,
                pos=self.dashsublayout.pos
                )
                
            with self.dashlayout.canvas.before:
                Color(0.831,0.686,0.216,1)
                Rectangle(
                size=self.dashlayout.size,
                pos=self.dashlayout.pos
                )
                
        def go_income(self,instance):
            self.manager.current="income"
        def go_expense(self,instance):
            self.manager.current ="expense"
        def on_enter(self):
            expnse=self.manager.get_screen("expense")
            
            self.totalspendingl.text=f"Total expense: {expnse.expense}"
            login=self.manager.get_screen(
            "login"
            )
            
            
            
            incom=self.manager.get_screen(
            "income"
            )
            
            self.totalmoney=incom.income - expnse.expense
            self.totalincomel.text=f"Total income: {incom.income}"
            self.avmoneyl.text=f"Your available money is: {self.totalmoney}"
        
            
            
            self.dashintrolbl=Label(
            text= f"Hi, {login.username.text}",
            size_hint=(None,None),
            pos=(100,1300)
            )
            
            
            
            self.dashsublayout.add_widget(
            self.dashintrolbl
            )
            
class incomeScreen(Screen):
            def __init__(self,**kwargs):
                super().__init__(**kwargs)
                
                self.incomelayout=FloatLayout(
                size=(720,1568)
                )
                
                self.incomet=TextInput(
                size_hint=(None,None),
                size=(500,50),
                pos=(110,1075),
                background_normal=" ",
                background_color=(0,0,0,1),
                foreground_color=(1,1,1,1)
                
                )
                
                self.incomebtt=Button(
                text="save",
                size_hint=(None,None),
                size=(200,50),
                pos=(260,575),
                background_normal=" ",
                background_color=(0,0,0,0)
                
                
                )
                
                self.add_widget(
                self.incomelayout
                )
                
                self.incomelayout.add_widget(
                self.incomet
                )
                
                self.incomelayout.add_widget(
                self.incomebtt
                
                )
                
                self.incomeintrolbl=Label(
                text=
                "INPUT YOUR INCOME",
                size_hint=(None,None),
                size=(500,50),
                pos=(110,1475)
                )
                
                self.incomelayout.add_widget(
                self.incomeintrolbl
                )
                
                self.incomebtt.bind(
                on_press=self.save_income
                )
                
                self.backbtt1_0=Button(
                text="go back",
                size_hint=(None,None),
                size=(150,50),
                pos=(565,1475)
                )
                
                self.incomelayout.add_widget(
                self.backbtt1_0
                )
                self.compli1_0=Label(
                        text=" "
                        )
                self.incomelayout.add_widget(self.compli1_0)
                self.backbtt1_0.bind(
                on_press=self.go_back1
                )
                
                self.income=0.0
                #with self.incomet.canvas.before:
                    #Color(0.410,0.445,0.555,1),
                    #RoundedRectangle(
                    #size=self.incomet.size,
                    #pos=self.incomet.pos,
                    #radius=[20]
                    
                    
                    
                
                with self.incomebtt.canvas.before:
                    Color(0.227,0.525,1,1),
                    Rectangle(
                    size=self.incomebtt.size,
                    pos=self.incomebtt.pos
                    )
                
                with self.incomelayout.canvas.before:
                    Color(0.043,0.775,0.0769,1),
                    Rectangle(
                    size=self.incomelayout.size
                    )
            def go_back1(self,instance):
                self.manager.current="dashboard"
            def removecompli(self,instance):
                
                self.compli1_0.text=" "
                
                
                
            def save_income(self,instance):
                
                    try:
                        amount=float(
                        self.incomet.text.strip()
                        )
                    
                        self.compli1_0.text="saved successfully"
                        
                        
                        
                        self.income += amount
                        
                        
                        Clock.schedule_once(
                        self.removecompli,3
                        )
                    
                    
                    
                    except ValueError:
                        self.compli1_0.text="Please enter a valid number"
                        Clock.schedule_once(
                        self.removecompli,3
                        )
                    
                    
                    
                    
                
                        
                        
class expenseScreen(Screen):
            def __init__(self,**kwargs):
                super().__init__(**kwargs)
                self.expenselayout=FloatLayout(
                size=(720,1568)
                )
                
                self.expenset=TextInput(
                size_hint=(None,None),
                size=(500,50),
                pos=(110,1075),
                background_normal=" ",
                background_color=(0,0,0,1),
                foreground_color=(1,1,1,1)
                
                )
                
                self.expensebtt=Button(
                text="save",
                size_hint=(None,None),
                size=(200,50),
                pos=(260,575),
                background_normal=" ",
                background_color=(0,0,0,0)
                
                
                )
                
                self.add_widget(
                self.expenselayout
                )
                
                self.expenselayout.add_widget(
                self.expenset
                )
                
                self.expenselayout.add_widget(
                self.expensebtt
                
                )
                
                self.expenseintrolbl=Label(
                text=
                "INPUT YOUR EXPENSE",
                size_hint=(None,None),
                size=(500,50),
                pos=(110,1475)
                )
                
                self.expenselayout.add_widget(
                self.expenseintrolbl
                )
                
                self.expensebtt.bind(
                on_press=self.save_expense
                )
                
                self.backbtt1_2=Button(
                text="go back",
                size_hint=(None,None),
                size=(150,50),
                pos=(565,1475)
                )
                
                self.expenselayout.add_widget(
                self.backbtt1_2
                )
                
                self.backbtt1_2.bind(
                on_press=self.go_back2
                )
                
                self.expense=0.0
                self.compli1_2=Label(
                        text=""
                )
                self.expenselayout.add_widget(self.compli1_2)
                #with self.incomet.canvas.before:
                    #Color(0.410,0.445,0.555,1),
                    #RoundedRectangle(
                    #size=self.incomet.size,
                    #pos=self.incomet.pos,
                    #radius=[20]
                    
                    
                    
                
                with self.expensebtt.canvas.before:
                    Color(0.227,0.525,1,1),
                    Rectangle(
                    size=self.expensebtt.size,
                    pos=self.expensebtt.pos
                    )
                
                with self.expenselayout.canvas.before:
                    Color(0.043,0.075,0.369,1),
                    Rectangle(
                    size=self.expenselayout.size
                    )
            def go_back2(self,instance):
                self.manager.current="dashboard"
            def removecompli1(self,instance):
                
                self.compli1_2.text=" "
                
                
                
                
                
            def save_expense(self,instance):
                
                    try:
                        amount=float(
                        self.expenset.text.strip()
                        )
                        
                        self.expense +=amount
                    
                        self.compli1_2.text=" saved successfully"
                        Clock.schedule_once(
                        self.removecompli1,5
                        )
                        
                        
                         
                        
                        
                        
                    
                    
                    
                    except ValueError:
                        self.compli1_2.text="Please enter a valid number"
                    
                    
                    
                    
                
                        
                        Clock.schedule_once(
                        self.removecompli1,5
                        )
                        
        
        
                
                
                
        
        
                    
                        
                
                
                
                
                
                
            

            
            
            
            
        
            
            
            
        
        
        
        
        
class SmartFeeApp(App):
    def build (self):
        sm=ScreenManager()
        
        sm.add_widget(loginScreen(name="login"
        ))
        
        sm.add_widget(
        dashboardScreen(name="dashboard")
        )
        
        sm.add_widget(
        incomeScreen(name="income")
        
        )
        
        sm.add_widget(
        expenseScreen(name="expense")
        )
        
        return sm 
        
SmartFeeApp().run()