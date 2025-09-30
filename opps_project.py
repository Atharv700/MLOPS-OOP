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
            pass
        elif user_input=="2":
            pass
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

obj=talky()