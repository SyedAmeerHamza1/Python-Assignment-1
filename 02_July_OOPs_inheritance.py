# 1. Explain what inheritance is in object-oriented programming and why it is used.
# 2. Discuss the concept of single inheritance and multiple inheritance, highlighting their
# differences and advantages.
# 3. Explain the terms "base class" and "derived class" in the context of inheritance.
# 4. What is the significance of the "protected" access modifier in inheritance? How does
# it differ from "private" and "public" modifiers?
# 5. What is the purpose of the "super" keyword in inheritance? Provide an example.
# 6. Create a base class called "Vehicle" with attributes like "make", "model", and "year".
# Then, create a derived class called "Car" that inherits from "Vehicle" and adds an
# attribute called "fuel_type". Implement appropriate methods in both classes.
# 7. Create a base class called "Employee" with attributes like "name" and "salary."
# Derive two classes, "Manager" and "Developer," from "Employee." Add an additional
# attribute called "department" for the "Manager" class and "programming_language"
# for the "Developer" class.
# 8. Design a base class called "Shape" with attributes like "colour" and "border_width."
# Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add
# specific attributes like "length" and "width" for the "Rectangle" class and "radius" for
# the "Circle" class.
# 9. Create a base class called "Device" with attributes like "brand" and "model." Derive
# two classes, "Phone" and "Tablet," from "Device." Add specific attributes like
# "screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.
# 10. Create a base class called "BankAccount" with attributes like "account_number" and
# "balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from
# "BankAccount." Add specific methods like "calculate_interest" for the
# "SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.



# 1. Explain what inheritance is in object-oriented programming and why it is used.
'''
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit properties
and behaviors from another class. It is a mechanism that promotes code reuse and establishes relationships between
classes.

In inheritance, the class that inherits the properties and behaviors of another class is called the derived class or
child class. The class whose properties and behaviors are inherited is called the base class or parent class.'''

# 2. Discuss the concept of single inheritance and multiple inheritance, highlighting their
# differences and advantages.

'''
Single inheritance and multiple inheritance are two different types of inheritance in object-oriented programming (OOP).

Single inheritance is a type of inheritance where a derived class inherits from a single base class. This means that 
the derived class can only access the properties and methods of the base class.

Multiple inheritance is a type of inheritance where a derived class inherits from multiple base classes. This means 
that the derived class can access the properties and methods of all of its base classes.

Feature	                                  Single inheritance	                            Multiple inheritance
Number of base classes	                        1	                                                   >1
Access to properties and methods	  Only the properties and methods of the base class	    The properties and methods of all base classes
Complexity	                                  Simpler	                                            More complex
Potential for errors	                      Less likely	                                        More likely

Advantages of single inheritance:
Single inheritance is simpler to understand and implement than multiple inheritance.
Single inheritance reduces code duplication, which can make code more maintainable.

Advantages of multiple inheritance:
Multiple inheritance can provide more flexibility than single inheritance.
Multiple inheritance can allow a derived class to inherit from multiple different types of objects.

'''

# 3. Explain the terms "base class" and "derived class" in the context of inheritance.

'''In the context of inheritance, a base class is a class from which another class inherits properties and behaviors. 
The class that inherits from the base class is called the derived class.

The base class provides the foundation for the derived class. The derived class can add new properties and behaviors, 
or override existing ones, but it always inherits the properties and behaviors of the base class.'''

# 4. What is the significance of the "protected" access modifier in inheritance? How does
# it differ from "private" and "public" modifiers?


'''

The protected access modifier is a keyword used in object-oriented programming (OOP) to control the accessibility of 
members of a class. Protected members can be accessed by:

1.The class in which they are declared. 
2.Derived classes of the class in which they are declared. 

Protected members are not accessible from outside the class or its derived classes. This makes them a good choice for 
members that should be accessible to subclasses, but not to other classes.

The private access modifier is a keyword used in OOP to control the accessibility of members of a class. Private 
members can only be accessed by the class in which they are declared. This makes them a good choice for members that 
should be hidden from other classes.

The public access modifier is a keyword used in OOP to control the accessibility of members of a class. Public 
members can be accessed by any class. This makes them a good choice for members that should be accessible to all 
classes.'''


class person:
    def __init__(self, name, surname, profession):
        self._name = name  # Private
        self.__surname = surname  # Protected
        self.profession = profession  # public


# 5. What is the purpose of the "super" keyword in inheritance? Provide an example.

'''
The super keyword in Python is used to refer to the parent class of a subclass. It allows you to call methods 
defined in the superclass from the subclass, enabling you to extend and customize the functionality inherited from 
the parent class.'''


class cafe:
    def __init__(self, coffee, cold_brews, smoothies):
        self.coffee = coffee
        self.cold_brews = cold_brews
        self.smoothies = smoothies


class cafe_branch_2(cafe):
    def __init__(self, coffee, smoothies, cold_brews, salads):
        super().__init__(coffee, smoothies, cold_brews)
        self.salads = salads


menu = cafe_branch_2('black', 'blueberry', 'orange', 'veg salad')
print(menu.salads)


# 6. Create a base class called "Vehicle" with attributes like "make", "model", and "year".
# Then, create a derived class called "Car" that inherits from "Vehicle" and adds an
# attribute called "fuel_type". Implement appropriate methods in both classes.

class vehicle:
    def __init__(self, made_in, model, year):
        self.make = made_in
        self.model = model
        self.year = year


class car(vehicle):
    def __init__(self, made_in, model, year, fuel_type):
        super().__init__(made_in, model, year)
        self.fuel_type = fuel_type


Tata = car('India', 'Nexon', 2022, 'Diesel')

print(Tata.year)


# 7. Create a base class called "Employee" with attributes like "name" and "salary."
# Derive two classes, "Manager" and "Developer," from "Employee." Add an additional
# attribute called "department" for the "Manager" class and "programming_language"
# for the "Developer" class.

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name of the employee is {self.name} and salary is {self.salary}")


class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info_of_manager(self):
        super().display_info()
        print(f"He is from a department of {self.department}")


class developer(employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info_of_developer(self):
        super().display_info()
        print(f"Developing on {self.programming_language}")


functional_role = manager('Mak', 60000, "Marketing")
technical_role = developer('John', 100000, 'Python')
print(technical_role.display_info_of_developer())
print(functional_role.display_info_of_manager())


# 8. Design a base class called "Shape" with attributes like "colour" and "border_width."
# Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add
# specific attributes like "length" and "width" for the "Rectangle" class and "radius" for
# the "Circle" class.


class shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width

    def display_info(self):
        print(f'Colour is {self.colour} and border_width is set as {self.border_width}')


class rectangle(shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width)
        self.length = length
        self.width = width

    def display_info_of_rectangle(self):
        super().display_info()
        return f'Length and width of rectangle is {self.length} and {self.width}'


class circle(shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width)
        self.radius = radius

    def display_info_of_circle(self):
        super().display_info()
        return f'Radius of a circle is {self.radius}'


coffee_Table = rectangle('Black', 3, '4 feet', '3 feet')
circle_coffee_table = circle('brown', 3, 2)

print(coffee_Table.display_info_of_rectangle())
print(circle_coffee_table.display_info_of_circle())


# 9. Create a base class called "Device" with attributes like "brand" and "model." Derive
# two classes, "Phone" and "Tablet," from "Device." Add specific attributes like
# "screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.

class device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f'Brand and model of device is {self.brand} and {self.model}')


class Phone(device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def info_of_phone(self):
        super().info()
        return f"Phone's screen_size is {self.screen_size}"


class tablet(device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def info_of_tablet(self):
        super().info()
        return f'Battery_capacity of table is {self.battery_capacity}'


Apple = Phone('Apple', 'iphone14', '5.78 in')
Samsung = tablet('Samsung', 'Galaxy Tab A8', '7,040mAh')

print(Apple.info_of_phone())
print(Samsung.info_of_tablet())


# 10. Create a base class called "BankAccount" with attributes like "account_number" and
# "balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from
# "BankAccount." Add specific methods like "calculate_interest" for the
# "SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.

class bank_account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def info(self):
        print(f'Account_number is {self.account_number} and available balance is {self.balance}')


class savingsAccount(bank_account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f'Interest has been added and available balance is {self.balance}')


class checkingAccount(savingsAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deduct_fees(self):
        fees = 5
        self.balance -= fees
        print('5rs has been debited from your account for checkingAccount fees ')


savings_account = savingsAccount("123456789", 1000)
savings_account.deposit(500)
print(savings_account.balance)
savings_account.calculate_interest()

checking_account = checkingAccount("987654321", 500)
checking_account.deposit(100)
print(checking_account.balance)
checking_account.deduct_fees()
print(checking_account.balance)