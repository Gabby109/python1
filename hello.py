Birth_year =int(input("Enter birth year "))
age =(2019 - Birth_year)
if age <= 18:
   print("minor")
elif age <=36:
   print("youth")
else:
   print("elder")