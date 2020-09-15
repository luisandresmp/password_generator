import random
import string


def generator(universe):
    password = []
    
    for i in range(15):
        item = random.choice(universe)
        password.append(str(item)) 
    password = "".join(password)
    
    return password


def run():
    print('Generando contraseña....')
    letter_uppercase = list(string.ascii_uppercase)
    letter_lowercase = list(string.ascii_lowercase)
    number = list(range(10))
    universe = letter_lowercase + letter_uppercase + number
    password = generator(universe)
    print('Su nueva contraseña es : ' + ''.join(password))

if __name__ == "__main__":
    run()