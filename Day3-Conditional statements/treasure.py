print("""
       ____________
   ___/ ___________\
  / ___/           _____
 / /              (____ \
| |  E V 1 L           \ \
| |      1 N 5 1 D E    ) )
 \ \__               __/ /           __
  \__ \_____________/ __/        ___/  \
     \_______________/       ___/       \_
                         ___/             \
                     ___/   __/            \
                 ___/   __  \__/\           \
             ___/    __/        _\      ___/|
        ____/    __     \      /    ___/ _  (
       /        \ /_     \      ___/ _   \\ |
       |\  __    \  /       ___/ _   \\  _H_/
       | \/  \    \/    ___/ _   \\  _H_/ Y
       |`|  _/      ___/ _   \\  _H_/ Y   !   MEPH.
        \|_|\   ___/ _   \\  _H_/ Y   !   !
        !  | \_/ _   \\  _H_/ Y   !   !
        !  \` |  \\  _H_/ Y   !   !
            \`|  _H_/ Y   !   !
             \|_/ Y   !   !
                  !   !
                  !



Welcome to treasure island
Your mission is to find the treasure.

""")

cross_road=input("You're at a crossroad.Where do you want to go?'left' or 'right': ").lower()
if cross_road=="left":
    swim=input("Do you want to swim or wait: ").lower()
    if swim=="wait":
        door=input("Which door would you like to choose red,blue or yellow: ").lower()

        if door=="yellow":
            print("You win")
        else:
            print("Game over")    
    else:
        print("Game over")    
else:
    print("Game over")    
