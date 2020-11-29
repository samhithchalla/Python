import string
import random

if __name__ == "__main__":
    
    len = int(input("Enter Password length:\n"))

    l1 = list(string.ascii_letters)
    
    l2 = list(string.digits)
    
    l3 = list(string.punctuation)
    
    l = []
    l.extend(l1)
    l.extend(l2)
    l.extend(l3)

    pas = "".join(random.sample(l, len))

    print(f"Your password is: \n{pas}")
