from fetch import get_price_now

YELLOW_BOUNDARY = 5 # Cents (Euro)
RED_BOUNDARY = 15   # Cents (Euro)

def which():
    price = get_price_now()
    price /= 10 # Default is tens of cents for some reason

    red = price > RED_BOUNDARY
    yellow = price > YELLOW_BOUNDARY and not red
    green = not red and not yellow

    light_control = {"r": red, "y": yellow, "g": green}
    return light_control


if __name__=="__main__":
    print(which())
