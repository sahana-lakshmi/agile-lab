from datetime import datetime 

name = input("enter your name")
print("your name is", name)
regno = input("enter your Register number")
print("Reg no:", regno)
department = input("enter your department")
print("Dep:", department)
now = datetime.now()
print("current date: ",now.strftime("%d-%m-%y"))
print("current time: ",now.strftime("%H-%M-%S"))