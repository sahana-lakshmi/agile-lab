while True:
    print("""select any on:\n
          1: Enter name
          2: Enter Rollnumber
          3: Enter Department
          4: Enter Cgpa 
          5: exit
          """)
    choice = int(input("Enter your choice "))
    if choice == 1:
        a = input("enter your name")
    elif choice == 2:
        a = input("enter your regno")
    elif choice == 3:
        a  = input("enter your dep")
    elif choice == 4:
        a = input("enter your cgpa")
    elif choice == 5:
        print("Exited the program")
    print(a)