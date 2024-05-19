from views import (print_main_menu)

def run_app():

    while True:
        print_main_menu()
        user_choice = int(input("Zadej volbu: "))

        if user_choice == 1:
            print("seznam knih")
        elif user_choice == 2:
            print("pujčit knihu číslo ")
        elif user_choice == 3:
            pass
        elif user_choice == 0:
            exit()
        else:
            print("taková volba neexistuje")

run_app()