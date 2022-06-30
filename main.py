import pickle

class Vehiculo:
    marca = ""
    color = ""
    puertas = 0

    def __init__(self, marca, color, puertas):
        self.marca = marca
        self.color = color
        self.puertas = puertas
    
    def getMarca(self):
        return self.marca

f = open("datos.bin","rb")
v = pickle.load(f)
f.close()
print(v.getMarca())