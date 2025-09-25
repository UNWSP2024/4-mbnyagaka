# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    total_tickets = 0  # keeps track of all tickets ordered

    while True:
        movie = input("Enter the movie name (or type 'done' to finish): ")
        if movie.lower() == "done":
            break
        tickets = int(input(f"How many tickets for '{movie}'? "))
        total_tickets += tickets

    # After the loop ends, show the total
    print("===================================")
    print(f"Total tickets ordered: {total_tickets}")
    print("Thank you for using Movie Tix!")
    ######################


if __name__ == '__main__':
    main()