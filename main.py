from utils.model import users
from utils.controller import get_user_info, add_users, remove_user


def main():
    while True:

        print("==========MENU==========")
        print("0 - zakończ program")
        print("1 - pokaż co u znajomych")
        print("2 - dodaj nowego znajomego")
        print("3 - usuń znajomego")
        print('========================')
        choice = input("wybierz opcje menu: ")
        if  choice == "0": break
        if  choice == "1": get_user_info(users)
        if choice == "2": add_users(users)
        if choice == "3": remove_user(users)

if __name__ == "__main__":
    main()



