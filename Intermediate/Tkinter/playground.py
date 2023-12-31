#def add(*args):
#     for n in args:
#         print(n)
def add(*args):         #its a tuple we can also use index
    sum=0
    for n in args:
        sum+=n
    print(sum)

add(1,2,3,4,5)

def calculate(n,**kwargs):        #its a dictionary
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n+= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        # self.make=kw["make"]
        # self.model=kw["model"]
        self.make = kw.get("make")
        self.model=kw.get("model")
        self.color = kw.get("color")
        self.seat = kw.get("seat")

my_car=Car(make="Nissan")
print(my_car.model)








