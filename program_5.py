# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    budget = float(input("Enter the amount you have budgeted for this month: $"))
    while spent != 0:
        spent = float(input("Enter an expense (0 to finish): $"))
        total += spent
    difference = budget - total

    print("\n==============================")
    print(f"Your total expenses: ${total:.2f}")

    if difference > 0:
        print(f"You are UNDER budget by ${difference:.2f}. Good job!")
    elif difference < 0:
        print(f"You are OVER budget by ${abs(difference):.2f}. Be careful!")
    else:
        print("You are EXACTLY on budget!")
    ######################


if __name__ == '__main__':
    main()