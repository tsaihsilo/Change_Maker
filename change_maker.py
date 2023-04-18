print("Welcome to the vending machine change maker program")
print("Change maker initialized.")

stock = {"nickels": 25, "dimes": 25, "quarters": 25, "ones": 0, "fives": 0}

s = True
while True:
    print("Stock contains: " + 
        "\n   " + str(stock["nickels"]) + " nickels" + 
        "\n   " + str(stock["dimes"]) + " dimes" +
        "\n   " + str(stock["quarters"]) + " quarters" +
        "\n   " + str(stock["ones"]) + " ones" +
        "\n   " + str(stock["fives"]) + " fives")

    price = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
    if price == 'q':
        s = False
    else:
        while True:
            if float(price.is_integer()):
                legit_price = int(float(price) * 100) % 5
                if legit_price == 0:
                    break
                else:
                    print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
                    price = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
            else:
                print("Invalid purchase price. Try again\n")
                price = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")

            if price != float(price):
               print("Invalid purchase price. Try again\n")
               print("Invalid purchase price. Try again\n")
            else:
               legit_price = int(float(price) * 100) % 5
               if legit_price == 0:
                   break
               else:
                   print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
                   price = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
                
    if s == False:
        total = (stock["nickels"] * 5 + 
        stock["dimes"] * 10 + 
        stock["quarters"] * 25 + 
        stock["ones"] * 100 +
        stock["fives"] * 500)

        if int(total // 100) > 0:
            total_final = "Total: " + str(int(total // 100)) + " dollars and " + str(int(total % 100)) + " cents"
        else:
            if int(total % 100) > 0:
                total_final = "Total: " + str(int(total % 100)) + " cents"

        print(total_final)
        break

    print("\nMenu for deposits:" +
      "\n  " + "'n' - deposit a nickel" +
      "\n  " + "'d' - deposit a dime" +
      "\n  " + "'q' - deposit a quarter" +
      "\n  " + "'o' - deposit a one dollar bill" +
      "\n  " + "'f' - deposit a five dollar bill" +
      "\n  " + "'c' - cancel the purchase\n")

    price_h = float(price) * 100
    
    if price_h % 100 < 0:
        #fixme
        break
    else:
        if int(price_h // 100) > 0:
            payment = "Payment due: " + str(int(price_h // 100)) + " dollars and " + str(int(price_h % 100)) + " cents"
        else:
            if int(price_h % 100) > 0:
                payment = "Payment due: " + str(int(price_h % 100)) + " cents"

        print(payment)

    deposit = input("Indicate your deposit: ")
    
    count_5 = 0
    count_10 = 0
    count_25 = 0
    count_100 = 0
    count_500 = 0
    
    price1 = price_h
    v = True
    while price_h > 0:
        if deposit == "n":
            count_5 += 1
            price1 = price1 - 5
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "d":
            count_10 += 1
            price1 = price1 - 10
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "q":
            count_25 += 1
            price1 = price1 - 25
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "o":
            count_100 += 1
            price1 = price1 - 100  
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "f":
            count_500 += 1
            price1 = price1 - 500
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "c":
            v = False
            break
        else:
            print("Illegal selection: " + deposit)
            if price1 < 0:
                v = True
                break
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
                
            deposit = input("Indicate your deposit: ")
            continue
    print()
    
    if v == True:
        z = abs(price1)
    if v == False:
        z = price_h - price1 


    if z >= 25:
        q = z // 25
        remain_q = z % 25
        if q <= stock["quarters"]:
            print(f"Please take the change below.")
            print(f"   {int(q)} quarters") 
            stock["quarters"] = stock["quarters"] - q
            move_q = remain_q
        else: 
            print(f"Please take the change below.")
            print("   " + str(int(stock["quarters"])) + " quarters")
            change_q = q - stock["quarters"] 
            move_q = change_q * 25 + remain_q

        if move_q >= 10:
            d = move_q // 10
            remain_d = move_q % 10
            if d <= stock["dimes"]:
                print(f"   {int(d)} dimes") 
                stock["dimes"] = stock["dimes"] - d
                move_d = remain_d
            else: 
                print(str(int(stock["dimes"])) + " dimes")
                change_d = d - stock["dimes"] 
                move_d = change_d * 10 + remain_d

            if move_d >= 5:
                n = move_d // 5
                if n <= stock["nickels"]:
                    print(f"   {int(n)} nickels") 
                    stock["nickels"] = stock["nickels"] - n
                else: 
                    print(f"Machine is out of change.")
                    print(f"See store manager for remaining refund.")
                    print(f"Amount due is: {int(n * 5)}")
        elif move_q >= 5:
            n = move_q // 5
            if n <= stock["nickels"]:
                print(f"   {int(n)} nickels") 
                stock["nickels"] = stock["nickels"] - n
            else: 
                print(f"Machine is out of change.")
                print(f"See store manager for remaining refund.")
                print(f"Amount due is: {int(n * 5)}")
                
    elif z >= 10:
        d = z // 10
        remain_d = z % 10
        if d <= stock["dimes"]:
            print(f"Please take the change below.")
            print(f"   {int(d)} dimes") 
            stock["dimes"] = stock["dimes"] - d
            move_d = remain_d
        else: 
            print(f"Please take the change below.")
            print("   " + str(int(stock["dimes"])) + " dimes")
            change_d = d - stock["dimes"] 
            move_d = change_d * 10 + remain_d

        if move_d >= 5:
            n = move_d // 5
            if n <= stock["nickels"]:
                print(f"   {int(n)} nickels") 
                stock["nickels"] = stock["nickels"] - n
            else: 
                print(f"Machine is out of change.")
                print(f"See store manager for remaining refund.")
                print(f"Amount due is: {int(n * 5)}")

    elif z >= 5:
        n = z // 5
        if n <= stock["nickels"]:
                print(f"Please take the change below.")
                print(f"   {int(n)} nickels") 
                stock["nickels"] = stock["nickels"] - n
        else: 
            print(f"Machine is out of change.")
            print(f"See store manager for remaining refund.")
            print(f"Amount due is: {int(n * 5)}")
        
    else:
        print(f"Please take the change below.")
        print(f"  No change due.")

    print()

    stock["nickels"] = int(stock["nickels"] + count_5)
    stock["dimes"] = int(stock["dimes"] + count_10)
    stock["quarters"] = int(stock["quarters"] + count_25)
    stock["ones"] = int(stock["ones"] + count_100)
    stock["fives"] = int(stock["fives"] + count_500)

