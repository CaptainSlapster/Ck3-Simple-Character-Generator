'''

This will handle the traits for character creation. It will be done similarly to the character names except with trait names.

'''

trait_file = 'traits.txt'

trait_list = []

with open(trait_file, 'r') as tf:
    for line in tf:
        trait_list.append(line.strip(' \n,'))
trait_list = [i.split() for i in trait_list]
trait_list = [num for elem in trait_list for num in elem]

print(trait_list)