# Lab 5 
# Mizaiel Zambrano
# 3/25/2024
# The program calcualtes th total number of bottles collected over seven days and 
# the total payout based on the number of bottles

# Declare Variables
keep_going = "y"

while keep_going == "y":
    total_bottles = 0
    counter = 1
    today_bottles = 0
    total_payout = 0


    # Code 
    NBR_OF_Days = 7
    counter = 1
    while counter <= NBR_OF_Days:
        today_bottles = int(input(f"Enter number of bottles for day #{counter}: "))
        total_bottles += today_bottles
        counter += 1

    # Code to calculate total_payout
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

    # Code to print the number of total bottles and total payout
    print("\n")
    print("The total number of bottles collected is ", total_bottles)
    print(f"The total paid out is $ {total_payout:.1f}\n")

    keep_going = input("Do you want to enter another weeks worth of data? (Enter y or n): ")
    print("\n")