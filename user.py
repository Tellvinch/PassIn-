class Credentials:
    """
        Class that generates new instances of credentials
        """

    def login(self, username, password):
        while True:
            self.username = username
            self.password = password
            break

        username=input("Please enter your password : ")
        password=input("Please enter your username: ")



    login()

def cook():
  print("Welcome to PassIn.What do you want to do?")
  print("1.Create an account")
  print("2.Sign into an existing account ")
  choice =int(input(">"))
  if choice == 1 :
     new_username=input("Enter an name you would like to use: ")
     new_password=input("Enter a password to use to login: ")
     print(f'All done! {new_username}.You can now save your passwords in PassIn-') 

  else:
     username=input("Enter your username:")
     password=input("Enter a password:")
     print(f'Your username is {username} and password  {password}')
  
  

cook()  
