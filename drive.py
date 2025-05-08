
while True:
    try:
        age = int(input("age: "))
        if int(age)>= 17:
            print("you can drive")
        else:
            print("you can't drive")
        break
    except Exception as e:
        print(f"invalid input! {e}")
