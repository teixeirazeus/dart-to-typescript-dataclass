from collections import namedtuple

AtributeInfo = namedtuple("AtributeInfo", ["name", "type"])


class EntitieInfo:
    def __init__(self, name, file):
        self.name = name
        self.file = file
        self.atributes = []

    def __str__(self):
        string = []
        string.append(self.name)
        string.append(self.file)
        for atribute in self.atributes:
            string.append(atribute.name + "|" + atribute.type)
        return "\n".join(string)
