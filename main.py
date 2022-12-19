import pickle

class Vehiculo:
    tipo = ""
    marca = ""
    ruedas = 0

    def __init__(self, tipo, marca, ruedas):
        self.tipo = tipo
        self.marca = marca
        self.ruedas = ruedas

    def getTipo(self):
        return self.tipo

    def getMarca(self):
        return self.marca

    def getRuedas(self):
        return self.ruedas

v = Vehiculo("Auto", "VW", 4)
# print("Tipo: ", v.getTipo(), "\nMarca: ", v.getMarca(),
#       "\nNo. Ruedas: ", v.getRuedas())

f = open('vehiculo.pickle', 'wb')
pickle.dump(print("Tipo: ", v.getTipo(), "\nMarca: ", v.getMarca(),
      "\nNo. Ruedas: ", v.getRuedas()), f)
f.close()

f = open('vehiculo.pickle', 'rb')
vehiculo = pickle.load(f)
f.close()