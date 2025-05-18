def div():
    try:
        return 3 / 0
    except ZeroDivisionError:
        print("Caught division by zero!")
        return None  # Or handle appropriately.