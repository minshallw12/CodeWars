class Point:

    def __init__(self, xcor, ycor):
        self._xcoor = xcor
        self._ycoor = ycor

    def get_x(self):
        return self._xcoor

    def get_y(self):
        return self._ycoor

    def distance_to(self, point_obj):
        distanceX = self.get_x() - point_obj.get_x()
        distanceY = self.get_y() - point_obj.get_y()
        distance = ((distanceX**2) + (distanceY**2)) ** 0.5
        return distance

class LineSegment:

    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint1 = endpoint_1
        self._endpoint2 = endpoint_2

    def get_endpoint_1(self):
        return self._endpoint1

    def get_endpoint_2(self):
        return self._endpoint2
    
    def length(self):
        return self.get_endpoint_1().distance_to(self.get_endpoint_2())

    def slope(self):
        slope = (self.get_endpoint_1().get_y() - self.get_endpoint_2().get_y())/(self.get_endpoint_1().get_x() - self.get_endpoint_2().get_x())
        return slope

    def is_parallel_to(self, line_obj):
        slope1 = self.slope()
        slope2 = line_obj.slope()
        if abs(slope1 - slope2) < 0.000001:
            return True
        return False


point_1 = Point(7,4)
point_2 = Point(-6,18)
print(point_1.distance_to(point_2))
line_seg_1 = LineSegment(point_1,point_2)
print(line_seg_1.length())
print(line_seg_1.slope())


point_3 = Point(-2,2)
point_4 = Point(24, 12)
line_seg_2 = LineSegment(point_3,point_4)
print(line_seg_2.slope())
print(line_seg_1.is_parallel_to(line_seg_2))