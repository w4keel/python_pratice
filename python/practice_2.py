
price = 1000000

goodbuyer_credit= True

if goodbuyer_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
  
print(f"Down payment is ${int(down_payment)}")

name = input("select a username: ")
name1 = ('abc')

""" whileloop with one condition
while name == name1 :
    print("invalid username not available")
    name = input ("select another username: ")

else : 
    print("your username is " + name)
   """      

""" loop with multiple conditions
while len(name) < 3 or len(name) > 50 or name == name1 :
     print("invalid username not available")
     name = input ("select another username: ")

else if 
     print("your username is " + name)
"""


while True:
    if len(name) < 3 or len(name) > 50:
     print("invalid characters")
     name = input ("please select username between 3 to 50 characters: ")
    elif name == name1:
       print("invalid username not available")
       name = input ("select another username: ")
    else:
       print("valid username!")
       print("your username is " + name)
       exit()


