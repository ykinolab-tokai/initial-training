class DataManager():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def add_x(self, delta):
        self.x += delta
        
    def add_y(self, delta):
        self.y = delta
        
    def add_z(self, delta):
        self.y = delta
        
    def sum(self, ):
        return self.x + self.y + self.z
    
    
    
data_manager = DataManager(2, 3, 5)
print(data_manager.sum())  # => 10
data_manager.add_x(4)      # => data_manager.x の値が 2 から 6 に更新される
print(data_manager.sum())  # => 14
data_manager.add_y(0)      # => data_manager.y の値が 3 から 3 に更新される
print(data_manager.sum())  # => 14
data_manager.add_z(-9)     # => data_manager.z の値が 5 から -4 に更新される
print(data_manager.sum())  # => 5