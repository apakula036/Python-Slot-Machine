import random #import random to use the random module 

MAX_LINES = 3 # all caps because its a constant 
MAX_BET = 100
MIN_BET = 1 

ROWS = 3 
COLS = 3

symbol_count = {  #create a dictionary to store the amount of symbols 
    "A": 2,
    "B": 4,
    "C": 6, 
    "D": 8
}
symbol_value = { 
    "A": 5,
    "B": 4,
    "C": 3, 
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols): # add the variables as parameters to pass into the function 
    #randomly select the symbols for the reels 
    all_symbols = [] # create a list and create a for loop to add symbols into the list 
    for symbol, symbol_count in symbols.items(): 
        for _ in range(symbol_count): # you can use an underscore for vaiables that you dont care about just to loop through something 
            all_symbols.append(symbol)

    columns = [] 
    for _ in range(cols): # generate a list of columns because we need to do all of this 3 times        underscore because we dont need a number or amount to iterate through it should be automatic by the way we have our code set here 
        column = []
        current_symbols = all_symbols[:] # copies the list over NEEDS the semicolon to create it as a seperate list and not a reference to the list 
        for _ in range(rows): #loop through number of values that we need to generate which is equal to the number of rows we have in our slot machine 
            value = random.choice(current_symbols) # value is random from the list 
            current_symbols.remove(value) # remove the value from our list 
            column.append(value) # add the value to our column 

        columns.append(column)

    return columns

def print_slot_machine(columns):
     #transposing 
     for row in range(len(columns[0])): #number of rows we have is each of our columns 
        for i, column in enumerate(columns): #now we're looping through all of the items in column 
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:  
                print(column[row], end="")

        print()

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

def spin(balance):
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
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) # splat operator to pass all lines to the print operator 
    return winnings - total_bet

def main(): #created the function main so we can just restart the whole game by just calling main 
    # get all the information from the user 
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        asnwer = input("Press enter to spin press Q to quit.")
        if asnwer == "Q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")


main()