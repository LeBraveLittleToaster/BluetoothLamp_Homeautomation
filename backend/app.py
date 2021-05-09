import argparse
import json
from typing import Optional

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.slider import Slider

from utils.Config import Config
from utils.StripManager import StripManager, StripValue
from utils.runnerconfig import RunnerConfig

Builder.load_file("screens.kv")

parser = argparse.ArgumentParser()
parser.add_argument("port", help="port the server is running on (http)",
                    type=int)
parser.add_argument("mqtt_ip", help="mqtt server ip", type=str)
parser.add_argument("mqtt_port", help="mqtt server port", type=int)
parser.add_argument("mqtt_username", help="mqtt username", type=str)
parser.add_argument("mqtt_password", help="mqtt password", type=str)
p_args = parser.parse_args()

runner_config = RunnerConfig(p_args.port, p_args.mqtt_ip, p_args.mqtt_port, p_args.mqtt_username, p_args.mqtt_password)



def get_id(instance):
    for widget_id, widget in instance.parent.ids.items():
        if widget.__self__ == instance:
            return widget_id


class StripDetailScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_dragging = False

    def on_pre_enter(self, *args):
        strip_value: StripValue = strip_manager.get_or_add_strip_value_by_id(strip_manager.selected_id)
        self.ids.slider_hue.value = strip_value.hue
        self.ids.slider_brightness.value = strip_value.brightness
        self.ids.slider_speed.value = strip_value.speed

    def update_strip_value(self):
        print("Updating")
        strip_manager.set_strip_value(
            strip_manager.selected_id,
            self.ids.slider_hue.value,
            self.ids.slider_brightness.value,
            self.ids.slider_speed.value
        )

    def on_slider_up(self, instance: Slider):
        if self.is_dragging:
            self.is_dragging = False
            self.update_strip_value()

    def on_slider_down(self, instance: Slider):
        self.is_dragging = True


class DashboardScreen(Screen):

    def __init__(self, app_config: Config, **kw):
        super().__init__(**kw)
        self.app_config = app_config
        Clock.schedule_once(self.create_dashboard_grid)

    def create_dashboard_grid(self, instance):
        grid: GridLayout = self.ids.dashboard_grid
        for strip in self.app_config.strips:
            btn = Button(text=strip.name)
            btn.bind(on_press=self.on_strip_clicked)
            btn.id = strip.strip_id
            grid.add_widget(btn, len(self.children))

    def on_strip_clicked(self, instance: Button):
        print(instance.id)
        strip_manager.select_id(instance.id)
        self.manager.current = "strip_detail_screen"

    def on_settings_clicked(self, instance: Button):
        self.manager.current = "settings_screen"


class SettingsScreen(Screen):
    def __init__(self, app_config: Config, **kw):
        super().__init__(**kw)
        self.app_config = app_config


class BackendApp(App):
    def __init__(self, app_config: Config, **kwargs):
        super().__init__(**kwargs)
        self.app_config = app_config

    def build(self):
        screen_manager = ScreenManager(transition=WipeTransition())
        screen_manager.add_widget(DashboardScreen(self.app_config, name='dashboard_screen'))
        screen_manager.add_widget(StripDetailScreen(name='strip_detail_screen'))
        screen_manager.add_widget(SettingsScreen(self.app_config, name='settings_screen'))
        return screen_manager


if __name__ == '__main__':
    with open('config.json') as config_json:
        config = Config(json.load(config_json))
        global strip_manager
        strip_manager = StripManager(config.strips, runner_config)
        strip_manager.connect()
        BackendApp(config).run()
