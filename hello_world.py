def div():
    print("this is division method (but not dividing by zero)")
    return 3/1  # Changed from 3/0 to avoid ZeroDivisionError

def check():
    return "hello"

if __name__ == "__main__": 
    div()
    check()