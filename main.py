import random
import string


def get_random_string(length=256):
    # choose from all lowercase letter
    letters = string.ascii_letters + string.digits + "%$#@.,;:_'(){}-+=`~"
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


count = input("count: ")
length = input("length: ")
for i in range(int(count)):
    print(get_random_string(int(length)))
