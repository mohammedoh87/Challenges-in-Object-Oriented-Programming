class A:
    def __init__(self, a):
        self.a = a
    
    def __lt__(self, other):
        if (self.a < other.a):
            return "ob1 is less than ob2"
        else:
            return "ob1 is greater than ob2"
    
    def __eq__(self, other):
        if (self.a == other.a):
            return "ob1 is equal to ob2"
        else:
            return "ob1 is not equal to ob2"
        
ob1 = A(23)
ob2 = A(5)
print(ob1 < ob2)
print(ob1 == ob2)