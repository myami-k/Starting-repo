

def get_prime_number(prompt: int):
    for test in range(2, prompt):
        if prompt % test == 0:
            return False
    return True


is_prime = []
for number in range(1, 1001):
    if get_prime_number(number):
        is_prime.append(number)
with open("prime_numbers.txt", "w") as fp:
    fp.write(str(is_prime))
