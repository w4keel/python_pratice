
user = []
name = input("select a username: ")
while True:
    if len(name) < 3 or len(name) > 50:
     print("invalid characters")
     name = input ("please select username between 3 to 50 characters: ")
    elif name == user:
       print("invalid username not available")
       name = input ("select another username: ")
    else:
       user.append(name)
       print("valid username!")
       print("your username is " + name)
       break

print (user)
'''
if name!= user:
   print("invalid username not available")
else:
    user.append(name)

    '''
'''
name = input("select a  new username: ")   
while True:
    if name == user:
     print("invalid username not available")
     print (user)
     name = input ("please select a different username: ")
    else:
       user.append(name)
       print("valid username!")
       print("your username is " + name)
       break
'''
while True:
    name = input("select a  new username: ")
    if name not in user:
      print("valid username!")
      user.append(name)
      print("your username is " + name)
      print (user)


    else:
        print ("invalid username")
        name = input("select a new name ")
        user.append(name)
        print("your username is " + name)
        print (user)
