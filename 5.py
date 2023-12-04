import random
import string

def gen_passwd(leght):
    character=string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(leght) )
    return password
leght = int(input("podaj dlugosc hasla :"))
password = gen_passwd(leght)
print (password) 