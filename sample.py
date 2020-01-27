class Base(object): 
  
    # Constructor 
    def __init__(self, x): 
        self.x = x
        print(self.x)
  
class Derived(Base): 
    # Constructor 
    def __init__(self, x, y): 
        Base.__init__(self,10) 
        self.y = self.x
        print(self.y)
  
    def printXY(self): 
       
       # print(self.x, self.y) will also work 
       print(self.y) 
  
  
# Driver Code 

b=Derived(20,10)
b.printXY()  
