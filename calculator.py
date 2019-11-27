class Calculator:
    def add(x, y):
        print(x + y)

    def sub(x, y):
        print(x - y)

    def increment(x):
        print(x + 1)

    def add_scan():
        x = input("First number (x): ")
        y = input("Second number (y): ")
        result = int(x) + int(y)
        print("The sum of x and y is " + str(result))

    def help():
        print("Hallo")
