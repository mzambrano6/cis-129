#COFFEE SHOP
#CONSTANTS
COFFEE_PRICE = 5
MUFFIN_PRICE = 4
TEA_PRICE = 4
BAGEL_PRICE = 3
TAX_RATE = 0.06

#INPUT
num_coffees = int(input("Number of coffees?"))
num_muffins = int(input("Number of mufffins?"))
num_teas = int(input("Number of teas?"))
num_bagels = int(input("Number of bagels?"))

#CALCULATIONS
coffee_cost = num_coffees * COFFEE_PRICE
muffin_cost = num_muffins * MUFFIN_PRICE
tea_cost = num_teas * TEA_PRICE
bagel_cost = num_bagels * BAGEL_PRICE
subtotal = coffee_cost + muffin_cost + tea_cost + bagel_cost
tax = subtotal * TAX_RATE
total = subtotal + tax

#OUTPUT
print("\n***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${COFFEE_PRICE} each: ${coffee_cost:.2f}")
print(f"{num_muffins} Muffins at ${MUFFIN_PRICE} each: ${muffin_cost:.2f}")
print(f"{num_teas} Teas at ${TEA_PRICE} each: ${tea_cost:.2f}")
print(f"{num_bagels} Bagels at ${BAGEL_PRICE} each: ${bagel_cost:.2f}")
print(f"{(TAX_RATE * 100):.0f}% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")
print("Thank you for coming!! We hope to see you again!")
