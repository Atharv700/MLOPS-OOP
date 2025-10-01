class talky:
    def __init__(self):
        self.username=""
        self.password=""
        self.login=False
        self.menu()

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
            pass
        elif user_input=="4":
            pass
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


obj=talky()
