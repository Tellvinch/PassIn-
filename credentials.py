from user import user


class Credentials:
    """
        Class that generates new instances of credentials
        """

    def password():
        name = input("Save password for?? Answer with facebook,instagram etc:")
        print(f'Cool you want to save your {name} passsword')
        crepass = input(f'Enter your {name} password:')
        print(
            f'Are you sure you want to save {crepass} as your {name} password?')
        print("1.Yes,save password.")
        print("2.No,delete")
        option = int(input())
        if option == 1:
                print(f'All done! .Your password is safe now')
                # {user.new_username}
        else:
                print("Moved to trash!")
        print("Do you want to see what you have saved?")
        print("1.Yes please")
        print("2.Not now")
        view = int(input()) 
        if view == 1:
                print("Name       -     Password")
                print(f'{name}      -     {crepass}')
                # {user.new_username}
        else:
                print("Moved to trash!")    

    password()
