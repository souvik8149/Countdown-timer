"""
Countdown Timer ⏱️
-----------------
A beginner-friendly Python command-line countdown timer.

Features:
- Input validation
- Dynamic countdown display
- Beep sound when time is up
- Option to set another timer
"""


import time
import winsound

def countdown_timer():
    """
    Countdown Timer ⏱️

    - Asks user to enter seconds for countdown
    - Validates input (must be positive number)
    - Displays time remaining every second
    - Plays a beep sound when timer ends
    - Option to set another timer after it ends
    """

    print("-" * 40)
    print("   Welcome to Countdown Timer ⏱️")
    print("-" * 40)

#outer loop
    while True:

    # ask user for time
        while True:
            try:
                seconds = int(input("Enter the seconds: "))
                if seconds > 0:
                    break
                else:
                    print("Please enter a positive number!")
            except ValueError:
                print("Invalid input... Enter a number")

        print(f"Timer started for {seconds} seconds")
        print("\n")
    
    #logic , loop for countdown
        number = seconds
        for remaining in range(seconds , 0 ,-1):
            print(f"Time remaining {remaining} seconds ⏱️")
            time.sleep(1)

        
    #Ending message
        print("⏱️ Timer Ended!")
        winsound.Beep(400,700)
        print("-" * 40)
        
    #haven't added 
        while True:
            again_timer = input("Want to set another Timer yes/no : ").lower()
            if again_timer in ["yes" , "no"]:
                break
            print("Invalid choice , choose yes/no")
        
        if again_timer == "no":
            print("-" * 40)
            print("  👋Bye , Take care of your time!")
            print("-" * 40)
            break
        print("-" * 40)
        continue


        
if __name__ == "__main__":
    countdown_timer()
