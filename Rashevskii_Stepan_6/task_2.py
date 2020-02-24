class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, weight, thickness):
        return self._length * self._width * weight * thickness


asphalt_weight = Road(5000, 20)
print(asphalt_weight.weight(25, 5))
