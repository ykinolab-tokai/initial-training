class Datamanage:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
delta = Datamanage(x = 2, y = 3, z = 4)
Datamanage.add.x(delta)
print(Datamanage.sum())
Datamanage.add.y(delta)
print(Datamanage.sum())
Datamanage.add.z(delta)
print(Datamanage.sum())