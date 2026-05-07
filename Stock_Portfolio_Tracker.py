# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("===================================")
print("     STOCK PORTFOLIO TRACKER      ")
print("===================================")

# Number of stocks user wants to enter
n = int(input("How many stocks do you want to add? "))

# Input stock details
for i in range(n):

    stock_name = input("\nEnter stock name: ").upper()

    # Check if stock exists
    if stock_name not in stock_prices:
        print(" Stock not available in database.")
        continue

    quantity = int(input("Enter quantity: "))

    # Store in portfolio
    portfolio[stock_name] = quantity

# Calculate total investment
print("\n========== PORTFOLIO SUMMARY ==========")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(f"{stock} -> Quantity: {quantity}, "
          f"Price: ${price}, "
          f"Investment: ${investment}")

print("\n---------------------------------------")
print("Total Investment Value = $", total_investment)
print("---------------------------------------")

# Optional: Save result to a text file
save = input("\nDo you want to save the report? (yes/no): ").lower()

if save == "yes":

    file = open("portfolio_report.txt", "w")

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=========================\n")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock} -> Quantity: {quantity}, "
            f"Price: ${price}, "
            f"Investment: ${investment}\n"
        )

    file.write("\nTotal Investment Value = $" + str(total_investment))

    file.close()

    print(" Report saved as 'portfolio_report.txt'")

else:
    print("Report not saved.")

print("\nThank You for Using Portfolio Tracker!")