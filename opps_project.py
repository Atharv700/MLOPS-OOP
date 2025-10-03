class talky:

    __user_id=1

    def __init__(self):
        self.username=""
        self.id=talky.__user_id
        talky.__user_id +=1
        self.__name="Default user" #hidden attribute
        self.password=""
        self.login=False
        #self.menu()

    def getter(self):
        return self.__name
    
    def setter(self,value):
        self.__name=value

    def menu(self):
        user_input=input("""Welocome to talky || how would you like to proceed?
                         1. Enter 1 to signup
                         2. Enter 2 to signin
                         3. Enter 3 to write a post
                         4. Enter 4 th send a message to friend
                         5. Enter any other key to exit""")
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.post()
        elif user_input=="4":
            self.message()
        else:
            exit()
    
    def signup(self):
        user=input("Enter your email as username")
        pws=input("Enter you password")
        self.username=user
        self.password=pws
        print("You are signup successfully here ")
        self.menu()

    def signin(self):
        if self.username=="" or self.password=="":
            print("You havent signup yet , please signup first and then proceed")
            self.menu()
        else :
            us=input("Please enter your username")
            ps=input("Please enter your password")
            if(us==self.username and ps==self.password):
                print("You have signin successfully , you can now post and message")
                self.login=True
                self.menu()
            else:
                print("Please enter the Right credentials")

    def post(self):
        if self.login==True:
            txt=input("Write the message you want to post")
            print(f"The following message is posted successfully{txt}")
        else :
            print("Please fiest signin first to post the message \n")
        self.menu()

    def message(self):
        if self.login==True:
            txt=input("Enter the message you want to send")
            friend=input("Enter the name of the friend")

            print(f"the message is successfully send to the {friend}")

        else:
            print("To send the Message you have to signin first")

        self.menu()


user1=talky()
user2=talky()
user3=talky()

print(user1.id)
print(user2.id)
print(user3.id)

# function vs message (in function we give the obj as the argument)
# magic method -
# self -> use to pass the object itself 
# can create attribute and function outside the class 
# encapsulation : self.__attribute while accessing obj._classname__attribute and inside class can be access like self.__attribute

# static attribute : commom to all objects define outside the __init__() method  