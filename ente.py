#Jorge
class ente():
  def __init__(self, id: int = 0, nombre: str = "nombre"):
    self.id = id
    self.nombre = nombre
    
  @property
  def id(self) -> int:
    return self._id
    
  @id.setter
  def id(self, value) -> int:
    self._id = value

  @property
  def nombre(self) -> str:
    return self._nombre
    
  @nombre.setter
  def nombre(self, value) -> str:
    self._nombre = value

  #We define the function that will allow us to print each of the attributes
  def __str__(self):
      return f"Ente: {self.id}, {self.nombre}"

  #The equals function is created to make the comparison between two objects.
  def equals(self, other):
    if isinstance(other, ente):
      return self.id == other.id and self.nombre == other.nombre
    return False