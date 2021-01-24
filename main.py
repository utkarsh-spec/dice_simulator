import random
import turtle

dice_list_x = [00.00, 50.00, 100.00, 00.00, 50.00, 100.00]
dice_list_y = [00.00, 00.00, 00.00, 50.00, 50.00, 50.00]

count = 0

dice = input("PRESS 'f' KEY FOR ROLLING:\n")
if dice == 'f' and 'F':
    dice_result = random.randrange(1, 7)
    print(dice_result)

    for item in range(1, dice_result + 1):
        p1 = turtle.Turtle()
        p1.shape("circle")
        p1.color("green")
        p1.setposition(dice_list_x[count], dice_list_y[count])
        count = count + 1

else:
    print("ENTER PROPER INPUT")

display = turtle.Screen()
display.title("dice")
display.bgcolor("black")

display.mainloop()
