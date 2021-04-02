class Mouse:
    def __init__(self, manufacturer, name, dpi, refresh_rate, weight, price):
        self.manufacturer = manufacturer
        self.name = name
        self.dpi = dpi
        self.refresh_rate = refresh_rate
        self.weight = weight
        self.price = price

    def is_ultra_light(self):
        if self.weight <= 70:
            return True
        else:
            return False
