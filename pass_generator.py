import random
password="ABCDEFGHIJKLMNOPORSTUVXYZ1234567890abcdefghijklmnopqurstuvwxyz,./-_=+\|<>*$#@^&!?"
length_password=int(input("Enter The Length Of Password: "))
a="".join(random.sample(password,length_password))
print(f"Your Password is:{a}")