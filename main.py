#this is a NoteBook
from USERS import actions

print("""

     Welcome to NoteBook!
|--------------------------|
| What do you wanna do?    |
|                          |
| 1.Log in                 |
| 2.Sign in                |
|--------------------------|

""")

wi = 0
try:
    welcome_input = int(input("Write your answer here: "))
    wi = welcome_input

except:
    print("\nWrite one number in range '1 - 2'\n")

    while True: 
        try:
            welcome_input = int(input("Write your answer here: "))

            if welcome_input == 1 or welcome_input == 2:
                wi = welcome_input
                break
            else:
                print("")
        except:
            print("")



do_it = actions.actions()

if wi == 1:
    do_it.log_in()

elif welcome_input == 2:
    do_it.sign_in()



