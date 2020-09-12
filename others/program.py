# task 1 - create names dictionary (in format: name: name's length)
name_list = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
name_dictionary = {}

for name in name_list:
    name_dictionary[name] = len(name)

print(name_dictionary)

# task 2 - get prime numbers from list
my_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
prime_numbers = []
for pr in my_list:
  if pr == 1:
    pass
  else: 
    for i in range(2,pr):
      if pr % i == 0:
        break
    else:  
      prime_numbers.append(pr)
print(prime_numbers)

# task 3 - insert missing days
days = ['pon','śro','pią','sob']
new_days = {'wto': 2,'czw': 4, 'nie': 7}

for day, number in new_days.items():
    days.insert(day, number - 1)

print(days)

# task 4 - print steps to prepare tea
unsorted_steps = ['włącz czajnik', 'znajdź opakowanie herbaty', 'zalej herbatę', 'nalej wody do czajnika', 'wyjmij kubek', 'włóż herbatę do kubka']
steps = [unsorted_steps[4], unsorted_steps[1], unsorted_steps[5], unsorted_steps[3], unsorted_steps[0], unsorted_steps[2]]

for index, step in enumerate(steps):
    print(f'Krok {index + 1}: {step}')

# task 4b - operate on the same array
steps = ['włącz czajnik', 'znajdź opakowanie herbaty', 'zalej herbatę', 'nalej wody do czajnika', 'wyjmij kubek', 'włóż herbatę do kubka']

steps.insert(0, steps.pop(4))
steps.insert(1, steps.pop(2))
steps.insert(2, steps.pop(5))
steps.insert(3, steps.pop(3))
steps.insert(4, steps.pop(2))

for index, step in enumerate(steps):
    print(f'Krok {index + 1}: {step}')
