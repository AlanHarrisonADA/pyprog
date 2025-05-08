while True:
    try:
        band = input("type of ticket: s/a/o ")
        ticket_prices = {'s':5, 'a':10, 'o':7.5}
        price = ticket_prices[band]
        print(price)
        #     print("£5")
        # elif type == "a":
        #     print("£10")
        # elif type == "o":
        #     print("£7.50")
        # else:
        #     raise ValueError("input not s/a/o")
    except KeyError as e:
        print(f"Error, invalid ticket band: {e}")
