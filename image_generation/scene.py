class Scene(object):
    def __init__(self, objects):
        self.objects = objects

class CLEVRColor(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def to_num(self):
        if self.name == "gray":
            return 1
        elif self.name == "red":
            return 2
        elif self.name == "blue":
            return 3
        elif self.name == "green":
            return 4
        elif self.name == "brown":
            return 5
        elif self.name == "purple":
            return 6
        elif self.name == "cyan":
            return 7
        elif self.name == "yellow":
            return 8

class CLEVRShape(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def to_num(self):
        if self.name == "cube":
            return 1
        elif self.name == "sphere":
            return 2
        elif self.name == "cylinder":
            return 3


class CLEVRSize(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def to_num(self):
        if self.name == "small":
            return 1
        elif self.name == "large":
            return 2

class CLEVRMaterial(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def to_num(self):
        if self.name == "rubber":
            return 1
        elif self.name == "metal":
            return 2

class CLEVRObject(object):
    def __init__(self, color, shape, size, material):
        self.color = color
        self.shape = shape
        self.size = size
        self.material = material

    def __eq__(self, other):
        return self.__str__() == other.__str__()
        #return self.color == other.color and self.shape == other.shape \
        #       and self.size == other.size and self.material == other.material

    def __str__(self):
        return "CLEVRObject(%s,%s,%s,%s)" % (str(self.color), str(self.shape), str(self.size), str(self.material))

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.to_num() <= other.to_num()

    def to_num(self):
        return 1000*self.size.to_num() + 100*self.shape.to_num() + 10*self.color.to_num() + self.material.to_num()