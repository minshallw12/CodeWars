class Taxicab:
    
    def __init__(self, xco, yco):
        self._x-coordinate = xco
        self._y-coordinate = yco
        self._odometer = 0

    def get_x(self):
        return self._x-coordinate

    def get_y(self):
        """ get y coordinate"""
        return self._y-coordinate
    
    def get_odometer(self):
        """ get x odometer"""
        return self._odometer

    def move_x(self, units):
        """ move x units"""
        self._x-coordinate += units
        self._odometer += abs(units)

    def move_y(self, units):
        """ move y units"""
        self._y-coordinate += units
        self._odometer += abs(units)

cab = Taxicab(5,-8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.get_odometer())
print(cab.get_x())
print(cab.get_y())