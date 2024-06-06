from character_class import *
import sys
###MAINFILE
###
#   Yes I will need to rewrite this and make it better. I created it with 3-4 hrs of work.s
###
print("""

Simple CK3 Character Generator by Austin Smith AKA CaptainSlapster!

""")


##TEST VARIABLES
start_year = input("Enter in your start year! e.g. 867: ")
min_age = input("Enter the minimum age for your characters: ")
max_age = input("Enter the maximum age for your characters: ")
religion = input("Enter the religion for your characters e.g. catholic: ")
culture = input("Enter the culture for your characters e.g. roman: ")
percent_female = input("Enter a percentage rate for female characters e.g. 0 = 0% 100 = 100%: ")

number_of_characters = input("Enter the number of characters to generate: ")
start_year = int(start_year)
min_age = int(min_age)
max_age = int(max_age)
number_of_characters = int(number_of_characters)
percent_female = int(percent_female)


#names_file = sys.argv[1]
names_file = 'names.txt'

names_male = []
names_female = []
name_list = []

def find_between_tags(lst, start_tag, end_tag):
    start_index = lst.index(start_tag)
    end_index = lst.index(end_tag, start_index)
    return lst[start_index + 1: end_index]

with open(names_file, 'r') as infile:
    for line in infile:
        name_list.append(line.strip(' \n,'))

names_male = find_between_tags(name_list,"male:{","}")
names_female = find_between_tags(name_list,"female:{","}")

names_male = [i.split() for i in names_male]
names_female = [i.split() for i in names_female]

names_male = [num for elem in names_male for num in elem]
names_female = [num for elem in names_female for num in elem]

print(names_male)
print(names_female)

def create_character(charid,start_year,min_age,max_age,religion,culture,names_male,names_female):
    #initialize character
    char = Character()
    char.id = charid
    char.determine_birth_death(start_year,min_age,max_age)
    char.determine_gender(percent_female)
    char.culture = culture
    char.religion = religion
    char.name = char.determine_name(names_male,names_female)
    return char


def generate_text(fileobj,charobj):
    fileobj.write(f'''
    {charobj.culture}_{charobj.id} = {{
                name = "{charobj.name}"

                religion = {charobj.religion}
                culture = {charobj.culture}
    ''')
    if charobj.isfemale == True:
        fileobj.write(f'\t\t\tfemale = yes\n')
    else:
        pass
    ##Leave space here for traits/skills later on##

    fileobj.write(f'''
                {charobj.birthyear}.{charobj.birthmonth}.{charobj.birthday} = {{
                    birth = yes
                }}
                {charobj.deathyear}.{charobj.deathmonth}.{charobj.deathday} = {{
                    death = yes
                }}
    }}
    ''')

##Create empty file for the characters##
with open('outfile.txt','w+',encoding= 'utf-8')as out:
    out.write('\ufeff')
    for i in range(1,number_of_characters):
        char = create_character(i,start_year,min_age,max_age,religion,culture,names_male,names_female)
        generate_text(out,char)
