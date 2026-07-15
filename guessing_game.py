import random

def guess_num():
    random_number = random.randint(1, 10)
    atempts = 0
    try:
        while True:
            user = int(input("Try to guess a number: "))

            if random_number > user:
                print("Your number is slighter than random")
                atempts += 1
            elif random_number < user:
                print("Your number is greater than random")
                atempts += 1
            else:
                atempts += 1
                return f"\nYou guessed it right after {atempts} atempt(s)\n"
            
    except ValueError:
        return "It is not a number"
    

print(guess_num())