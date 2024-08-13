import random

double_six = 0
test_numbers = 0

while True:
    test_numbers += 1
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    if dice_1 == 6 and dice_2 == 6:
        double_six += 1
    if double_six == 10:
        print(f"the dices were rolled {test_numbers} times to get double six for 10 times")
        break