class Animal:
    def __init__(self):
        self.name="life"

    def speak(self):
        print(f"{self.name} can make sound")


class dog(Animal):

    def __init__(self,name2):
        super().__init__()


        self.name2=name2
        

    def speak(self):
        print(f"{self.name} can bark,but {self.name2} can ")



obj=dog("bud")
obj.speak()

#we can inheritate constructore , non private attribute and method 