import USERS.user as create_user
import NOTES.actions as n_actions
class actions:

    def log_in(self):
        
        print("Enter your credentials:\n")
        

        try:
            email = input("Enter your email: ")
            passwd = input("Enter your password: ")


            user = create_user.user('', '', email, passwd)
            login = user.log_in()

            if email == login[3]:
                print(f"\nWelcome {login[1]}, you have registered on {login[5]}")
                self.next_actions(login)

        except:
            print("wrong email or password!")

    def next_actions(self, user):
        
        print("""
        
        |--------------------------|
        | What do you wanna do?    |
        |                          |
        | 1. Create note           |
        | 2. Show note             |
        | 3. Delete note           |
        | 4. Exit                  | 
        |--------------------------|

        """)

        u_input = int(input("Write your answer here: "))

        do_it = n_actions.action_notes()

        
        if u_input == 1:
            do_it.create_note(user)
            self.next_actions(user)

        elif u_input == 2:
            do_it.show_note(user)
            self.next_actions(user)
        
        elif u_input == 3:
            do_it.delete_note(user)
            self.next_actions(user)

        elif u_input == 4:
            print(f"\nSee you later {user[1]}!")
            exit()


    




    def sign_in(self):

        print("Let's register you!\n")

        name = input("What's your name?: ")
        last_name = input("What's your last name?: ")
        email = input("What's your email?: ")
        passwd = input("What will be the password?: ")

        user = create_user.user(name, last_name, email, passwd)
        s_in = user.sign_in()


        if s_in[0] >= 1:
            print("\nsuccessfully registered user!")

        else:
            print("\nuser failed to register!")
