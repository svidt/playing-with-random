import random

def randint_roll():
    n = random.randint(1,20)
    print(str(n) + roll.__name__)

def input_roll():
    num2 = int(input("enter max. number: "), end = " ")
    n = random.randint(1, num2)
    print(n)

def randrange_roll():
    print(random.randrange(1,20))

def choice_list_roll():
    list = [1, 2, 3, 4, 5, 6]
    print(random.choice(list))

def choice_list_fixed_roll():
    random.seed(9)
    list = [1, 2, 3, 4, 5, 6]
    print(random.choice(list))

def random_char():
    string = "The quick brown fox jumps over the lazy dog"
    print(random.choice(string))

def random_shuffle_roll():
    list_shuffle = ['A', 'B', 'C', 'D', 'E', 'F']
    print(random.shuffle(list_shuffle))
