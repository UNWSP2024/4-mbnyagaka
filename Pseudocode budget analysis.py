Start

Initialize budget = 0.0
Initialize total = 0.0
Initialize spent = 1.0
Initialize difference = 0.0

Display "Enter the amount you have budgeted for this month:"
    Input budget

WHILE spent is not equal to 0
     Display "Enter an expense (0 to finish):"
     Input spent
     Add spent to total
END WHILE

    Set difference = budget - total

    Display "Your total expenses: " + total

IF difference > 0 THEN
    Display "You are UNDER budget by " + difference
ELSE IF difference < 0 THEN
    Display "You are OVER budget by " + absolute value of difference
ELSE
    Display "You are EXACTLY on budget."
END IF

Stop