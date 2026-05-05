class A:
    def func():
        print("abc")
    
    def new():
        print("xyz")


obj = A #object is obj
obj2 = A
obj.func()
obj2.new()