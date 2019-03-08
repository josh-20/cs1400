import pattern
def main():

    # Setup pattern
    pattern.setup()

    # Play again loop
    playAgain = True

    while playAgain:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))

        # If they choose 'Rectangle Patterns'
        if mode == 1:
            #### Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("Enter an x,y values: "))
            width = int(input("Enter a width: "))
            height = int(input("Enter a height: "))
            offset = int(input("Enter an offset number: "))
            count = int(input("Enter number of shapes:"))
            rotation = int(input("Enter Number of Degrees you want it to rotate: "))


            #### End Add Inputs Statement(s) ####


            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            radius = int(input("Enter a radius value:"))
            centerX, centerY = eval(input("Enter an x,y values: "))
            offset = int(input("Enter an offset number: "))
            count = int(input("Enter number of shapes:"))
            rotation = int(input("Enter degree of rotation:"))

            #### End Add Inputs Statement(s) ####

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count,rotation)

        '''# If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####

            #### End Add Inputs Statement(s) ####
            if num == "":
                pattern.drawSuperPattern()
            else:
                pattern.drawSuperPattern(num)

        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

        #### Add Statement(s) to clear drawings and play again ####

        #### End Add Inputs Statement(s) ####

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()
'''

main()
