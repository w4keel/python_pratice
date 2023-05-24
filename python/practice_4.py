user = []
while True:
    name = input("select a  new username: ")
    if name not in user:
      print("valid username!")
      user.append(name)
      print("your username is " + name)
      print (user)


    else:
        print ("invalid username")
        print (user)
  
