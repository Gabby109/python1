vowels = ['a','e','i','o','u']
string = set()
my_vowels = set()


def count_vowels (my_string):
  for element in my_string:

      if my_string.count(element) >= 2:

         string.add(element)
  if element in vowels:
       my_vowels.add(element)

  new_string = len(string)
  vowel = " ".join(my_vowels)
  return(vowel, new_string)
my_string = input("Enter text: ")
result = count_vowels(my_string)
print(result)