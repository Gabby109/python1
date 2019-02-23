class Person:
    # instantiation
    def __init__(self, my_name, my_height, my_age, my_gender):
        self.name = my_name
        self.height = my_height
        self.age = my_age
        self.gender = my_gender

    def get_year_of_birth(self):
        current_year = 2019
        return current_year - self.age

    def print_name(self):
        title = ''
        if self.gender.lower().startswith("m"):
            title = 'Mr.'
        else:
            title = 'Mrs.'

        print(title + " " + self.name)

    def print_height(self):
        print(f"{self.height} cm")

allan = Person("Allan", 350, 25, "Male")
mugisha = Person("Mugisha", 560, 29, "Male")
cyrus = Person("Cyrus", 950, 20, "Female")
ronald = Person("Ronald", 3540, 23, "Male")

print("--- Allan's object --- ")
print(f"Yr of birth: {allan.get_year_of_birth()}")
allan.print_name()
allan.print_height()


print("--- Mugisha's object --- ")
print(f"Yr of birth: {mugisha.get_year_of_birth()}")
mugisha.print_name()
mugisha.print_height()


print("--- cyrus's object --- ")
print(f"Yr of birth: {cyrus.get_year_of_birth()}")
cyrus.print_name()
cyrus.print_height()


print("--- Ronald's object --- ")
print(f"Yr of birth: {ronald.get_year_of_birth()}")
ronald.print_name()
ronald.print_height()