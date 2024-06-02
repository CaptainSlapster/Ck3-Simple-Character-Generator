from character_class import *
import sys
###MAINFILE

print("""

Simple CK3 Character Generator by Austin Smith AKA CaptainSlapster!

""")


##TEST VARIABLES
start_year = input("Enter in your start year!: e.g. 867: ")
min_age = input("Enter the minimum age for your characters: ")
max_age = input("Enter the maximum age for your characters: ")

start_year = int(start_year)
min_age = int(min_age)
max_age = int(max_age)


names_file = sys.argv[1]
#names_file = 'names.txt'

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


def create_character(charid,start_year,name,min_age,max_age,religion,culture):
    #initialize character
    char = Character()
    char.id = charid
    char.determine_birth(start_year,min_age,max_age)
    char.determine_deathyear(start_year,min_age,max_age)
    char.determine_gender(25)
    char.culture = culture
    char.religion = religion
    char.name = name
    return char

filetext = '''
{0}_{1} = {{
    name = "{2}"

    religion = {3}
    culture = {4}

    {5}.{6}.{7} ={{
        birth = yes
    }}
    {8}.{9}.{10} = {{
        death = yes
    }}
}}

'''
filetext_female = '''
{0}_{1} = {{
    name = "{2}"

    religion = {3}
    culture = {4}
    female = {5}
    {6}.{7}.{8} ={{
        birth = yes
    }}
    {9}.{10}.{11} = {{
        death = yes
    }}

}}

'''


##Create empty file for the characters##
with open('outfile.txt','w+',encoding= 'utf-8')as out:
    out.write('\ufeff')
    for i in range(70):
        random.seed()
        name = None
        char = create_character(i,start_year,name,min_age,max_age,"catholic","roman")
        if char.isfemale == True:
            char.name = random.choice(names_female[random.randrange(len(names_female))])                        
            out.write(filetext_female.format(char.culture,char.id,char.name,char.religion,char.culture,'yes',char.birthyear,char.birthmonth,char.birthday,char.deathyear,char.deathmonth,char.deathday))
        else:
            char.name = random.choice(names_male[random.randrange(len(names_male))])  
            out.write(filetext.format(char.culture,char.id,char.name,char.religion,char.culture,char.birthyear,char.birthmonth,char.birthday,char.deathyear,char.deathmonth,char.deathday))