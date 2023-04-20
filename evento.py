#Diego Garcia
class evento():
    def __init__(self, id: int = 0, nombre: str = "Nombre", tiempoEvento: int = "0", lugar: str = "Lugar"):
      self.id=id
      self.nombre=nombre
      self.tiempoEvento = tiempoEvento
      self.lugar = lugar

    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, value) -> str:
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value) -> str:
        self._nombre = value

    @property
    def tiempoEvento(self) -> str:
        return self._tiempoEvento
    
    @tiempoEvento.setter
    def tiempoEvento(self, value) -> str:
        self._tiempoEvento = value

    @property
    def lugar(self) -> str:
        return self._lugar
    
    @lugar.setter
    def lugar(self, value) -> str:
        self._lugar = value

    def __str__(self):
      return f"Evento {self.id}: {self.nombre}, {self.tiempoEvento} dias, {self.lugar}"
      
    def equals(self, other):
      if isinstance(other, evento):
        return self.id == other.id and self.nombre == other.nombre and self.tiempoEvento == other.tiempoEvento and self.lugar == other.lugar
        return False

