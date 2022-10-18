import random #import random to use the random module 

MAX_LINES = 3 # all caps because its a constant 
MAX_BET = 100
MIN_BET = 1 

ROWS = 3 
COLS = 3

symbol_count = {  #create a dictionary to store the symbols 
    "A": 2,
    "B": 4,
    "C": 6, 
    "D": 8
}


# get the amount that they want to bet 
def deposit():
    while True: 
        amount = input("What would you like to deposit? $")
        if amount.isdigit():  # negatives wont work here 
            amount = int(amount)  # convert to a integer after the check otherwise itll fail before
            if amount > 0:
                print("You entered $" + str(amount) + " into the machine.") # give the user feedback on what just happened
                break  # exit 
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number greater than 0.")

    return amount


# get the number of lines the user wants to bet on 
def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():  # negatives wont work here 
            lines = int(lines)  # convert to a integer after the check otherwise itll fail before
            if 1 <= lines <= MAX_LINES:
                print("You entered " + str(lines) + " lines.") # give the user feedback on what just happened
                break  # exit 
            else:
                print("Enter a valid amount of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():  # negatives wont work here 
            amount = int(amount)  # convert to a integer after the check otherwise itll fail before
            if MIN_BET <= amount <= MAX_BET:
                print("You entered $" + str(amount) + " into the machine.") # give the user feedback on what just happened
                break  # exit  
            else:
                print(f"Amount must be between  ${MIN_BET} - ${MAX_BET}.") # f statements automatically convert the variable to a string if possible f(  {var} {var}  )
        else:
            print("Please enter a number.")

    return amount



def main(): #created the function main so we can just restart the whole game by just calling main 
    # get all the information from the user 
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}.")
        else:
            break

    #tell the user what is happening 
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    print(balance, lines, bet )
    print(f"${balance} current balance, {lines} lines betting on, and {bet} current bet.")


main()