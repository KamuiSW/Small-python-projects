Account_Name = ''
Account_Passwd = ''

def Pass():
    YorN = input('Is it a new account? (y or n) ')
    if YorN == 'y':
        global Account_Name
        global Account_Passwd
        Account_Name = input('Username: ')
        Account_Passwd = input('Password: ')
        print('Account created!')
        
    elif YorN == 'n':
        input_username = input('Username: ')
        if input_username == Account_Name:
            input_password = input('Password: ')
            if input_password == Account_Passwd:
                print('logged in!')
            else:
                print('Wrong password!')
        elif input_username != Account_Name:
            print('Username does not exist')

while True:
    Pass()
