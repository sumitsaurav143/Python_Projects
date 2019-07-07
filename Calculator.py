while True:
    print("CALCULATOR:-")
    print("1. ENTER ADD FOR ADDITION")
    print("2. ENTER SUB FOR SUBTRACTION")
    print("3. ENTER MUL FOR MULTIPLICATION")
    print("4. ENTER QUIT FOR EXIT")

    user_input = input("WHAT TO DO? : ")
    if user_input == "ADD":
          print("ADDITION")
          print("--------")
          a = int(input("ENTER FIRST NUMBER : "))
          b = int(input("ENTER SECOND NUMBER : "))
          c = a + b
          print("RESULT: ",c)
    elif user_input == "SUB" :
         print("SUBTRACTION")
         print("--------")
         a = int(input("ENTER FIRST NUMBER : "))
         b = int(input("ENTER SECOND NUMBER : "))
         c = a - b
         print("RESULT: ", c)
    elif user_input == "MUL" :
        print("MULTIPLICATION")
        print("--------")
        a = int(input("ENTER FIRST NUMBER : "))
        b = int(input("ENTER SECOND NUMBER : "))
        c = a * b
        print("RESULT: ", c)
    elif user_input == "QUIT" :
        exit()
    else:
        print("WRONG INPUT...!!")