from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle
import asyncio
import time
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.pagelayout import PageLayout
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.graphics import Color
from kivy.graphics import Canvas
import json

class VaihdeVelho(App):
    pass

class UIXmanager(ScreenManager):
    def __init__(self, **kwargs):
        """ADD STUFF HERE, IF YOU WANT THEM TO HAPPEN STRAIGHT AWAY WHEN THE GAME OPENS."""
        super().__init__(**kwargs)
        #Lisää tähän

class LoadScreen(Screen):
    pass

class StartScreen(Screen):
    pass

class StartScreenLayout(AnchorLayout):
    def switch_to_game_screen(self):
        self.parent.parent.current = 'game_screen'
    pass

class GameScreen(Screen):
    pass

class GameScreenLayout(AnchorLayout):
    pass

VaihdeVelho().run()