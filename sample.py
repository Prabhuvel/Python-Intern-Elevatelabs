class Calculator:
    def __init__(self,numbers,choice): #initializer
        self.numbers=numbers
        self.choice=choice

    def perform(self):
        if self.choice==1:  #Addition
            a=0
            for i in self.numbers:
                a+=i
            print("Sum :",a) 

        elif self.choice==2: #Subtraction
            s=self.numbers[0]
            for i in self.numbers[1:]:
                s-=i
            print("Difference :",s)

        elif self.choice==3:#Multiplication
            m=1
            for i in self.numbers:
                m*=i
            print("Product :",m)

        elif self.choice==4:#Divison
            d=self.numbers[0]
            try:
                for i in self.numbers[1:]:
                    d/=i
                print("Quotient:",d)
            except ZeroDivisionError:
                print("Error Cant be divided by Zero")
                
        else:
            print("Kindly Enter the correct choice")

print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice (1-5): "))

if choice == 5:
    print("Exiting calculator. Goodbye!")
    exit()

num = int(input("How many numbers do you want to enter: "))
list_of_numbers = []

for i in range(num):
    n = float(input(f"Enter number {i + 1}: "))
    list_of_numbers.append(n)

Calc = Calculator(list_of_numbers, choice)
Calc.perform()
