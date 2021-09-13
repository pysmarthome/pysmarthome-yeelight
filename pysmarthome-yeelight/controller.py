from pysmarthome import Model, RgbLampController, hex_to_rgb
import yeelight

class YeelightController(RgbLampController):
    model_class = Model.extends(RgbLampController.model_class, name='YeelightsModel')


    def on_load(self, addr='', **data):
        self.dev = yeelight.Bulb(addr)
        super().on_load(**data)


    def on(self):
        return True if self.dev.turn_on() == 'ok' else False


    def off(self):
        return True if self.dev.turn_off() == 'ok' else False


    def toggle(self):
        return True if self.dev.toggle() == 'ok' else False


    def get_brightness(self):
        properties = self.dev.get_properties()
        return int(properties['current_brightness'])


    def set_brightness(self, val):
        self.dev.set_brightness(int(val))


    def set_color(self, color):
        if type(color) == str:
            color = hex_to_rgb(color)
        self.dev.set_rgb(*color)


    def get_color(self):
        properties = self.dev.get_properties()
        rgb = properties['rgb']
        return f'#{rgb}'


    def get_power(self):
        properties = self.dev.get_properties()
        return properties['power']
