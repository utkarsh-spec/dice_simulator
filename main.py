import random

print("PRESS 'e' FOR EXIT\n")
while True:
    dice = input("PRESS 'f' KEY FOR ROLLING:\n")
    print(dice)
    if dice == 'f' and 'F':
        dice_result = random.randrange(1,7)
        print(f"DICE SHOWS: {dice_result}")
    elif dice == 'e':
        exit(1)
    else:
        print("ENTER PROPER INPUT")

