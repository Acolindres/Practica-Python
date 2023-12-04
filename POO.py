class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._encendido = False
        self._velocidad = 0

    def encender(self):
        if not self._encendido:
            print(f"{self._marca} {self._modelo}: El vehículo está encendido.")
            self._encendido = True
        else:
            print(f"{self._marca} {self._modelo}: El vehículo ya está encendido.")

    def apagar(self):
        if self._encendido:
            print(f"{self._marca} {self._modelo}: El vehículo está apagado.")
            self._encendido = False
            self._velocidad = 0
        else:
            print(f"{self._marca} {self._modelo}: El vehículo ya está apagado.")

    def acelerar(self, velocidad):
        try:
            velocidad = float(velocidad)
            if velocidad < 0:
                raise ValueError("La velocidad no puede ser negativa.")
            
            if self._encendido:
                self._velocidad += velocidad
                print(f"{self._marca} {self._modelo}: Acelerando a {velocidad} km/h. Velocidad actual: {self._velocidad} km/h.")
            else:
                print(f"{self._marca} {self._modelo}: El vehículo está apagado. Enciéndelo para acelerar.")
        except ValueError as ve:
            print(f"Error: {str(ve)}")

    def frenar(self, velocidad):
        try:
            velocidad = float(velocidad)
            if velocidad < 0:
                raise ValueError("La velocidad de frenado no puede ser negativa.")
            
            if self._encendido:
                if self._velocidad >= velocidad:
                    self._velocidad -= velocidad
                    print(f"{self._marca} {self._modelo}: Frenando a {velocidad} km/h. Velocidad actual: {self._velocidad} km/h.")
                else:
                    print(f"{self._marca} {self._modelo}: No puedes frenar más de lo que estás yendo.")
            else:
                print(f"{self._marca} {self._modelo}: El vehículo está apagado. Enciéndelo para frenar.")
        except ValueError as ve:
            print(f"Error: {str(ve)}")

# Crear instancias de la clase Vehiculo
auto = Vehiculo(marca="Toyota", modelo="Camry")
moto = Vehiculo(marca="Honda", modelo="CBR")

# Probar los métodos
auto.encender()
auto.acelerar(50)
auto.frenar(20)
auto.apagar()

moto.encender()
moto.acelerar(80)
moto.frenar(30)
moto.apagar()
