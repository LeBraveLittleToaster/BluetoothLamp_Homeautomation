import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from utils.Config import Config


class Settings_Menu(Screen):
    def build(self):
        print("Building screen Settings menu...")
        pass


class Main_Menu(Screen):

    def __init__(self, appconfig: Config, **kwargs):
        super().__init__(**kwargs)
        self.appconfig: Config = appconfig
        print(type(appconfig))

    @staticmethod
    def build_grid_from_config(columns: int, appconfig: Config) -> GridLayout:
        layout = GridLayout(cols=columns)
        print(appconfig)
        for strip in appconfig.strips:
            layout.add_widget(Button(text=strip.name))
        layout.add_widget(Button(text="Settings"))
        return layout

    def build(self):
        print("Building screen Main menu...")
        layout = self.build_grid_from_config(2, self.appconfig)
        return layout


class BackendApp(App):

    def __init__(self, app_config: Config, **kwargs):
        super().__init__(**kwargs)
        self.app_config = app_config

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Main_Menu(self.app_config, name="main_menu"))
        screen_manager.add_widget(Settings_Menu(name="settings_menu"))
        print(screen_manager.current)
        return screen_manager


if __name__ == '__main__':
    with open('config.json') as config_json:
        config = Config(json.load(config_json))
        BackendApp(config).run()
