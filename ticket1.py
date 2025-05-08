
ticket_types = {'s':5, 'a':10, 'o':7.5}
while True:
    try:
        band = input("type of ticket: s/a/o ")[0]
        if band == "x":
            raise ValueError("band x")
        price = ticket_types[band]
        print(price)
        break 
    except KeyError as e:
        print(f"Invalid ticket band, {e}")
    except ValueError as e:
        print(f"Band X entered: {e}")
    




