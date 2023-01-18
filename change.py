def changeCounter(cents):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    if cents == 0:
        print('0')

    quarters = cents // 25
    cents = cents - (quarters *25)

    dimes = cents // 10
    cents = cents - (dimes *10)

    nickles = cents // 5
    cents = cents - (nickles *5)

    pennies = cents

    print(quarters)
    print(dimes)
    print(nickles)
    print(pennies)




changeCounter(63)
