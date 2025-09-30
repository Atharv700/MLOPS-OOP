class employee:
    #agic method 
    def __init__(self):
        self.id=123
        self.salary=12000
        self.desination="DS"

    def travel(self,dest):
        print(f'I am travelling to {dest}')

sam=employee()

print(type(sam))
