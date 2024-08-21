import sys,configparser
##File handling#

##THIS IS FOR TESTING PURPOSES##
names_file = 'names.txt'

#Drag and drop your file onto the exe#
#names_file = sys.argv[1]

names_male = []
names_female = []
name_list = []


config = configparser.ConfigParser()
config.read('config.ini')
start_year = int(config.get('CONFIG','start_year'))
min_age = int(config.get('CONFIG','min_age'))
max_age = int(config.get('CONFIG','max_age'))
trait_number = int(config.get('CONFIG','max_no_of_traits'))
percent_female = int(config.get('CONFIG', 'female_percentage'))
min_date_range = int(config.get('CONFIG', 'earliest_date_range'))
max_date_range = int(config.get('CONFIG', 'max_date_range'))



religion = config.get('CONFIG','religion')
culture = config.get('CONFIG','culture')

with open(names_file, 'r') as infile:
    for line in infile:
        name_list.append(line.strip(' \n,'))


def generate_text(fileobj,charobj):
    fileobj.write(f'''
    {charobj.culture}_{charobj.id} = {{
                name = "{charobj.name}"
    ''')
    if charobj.inDynasty == True:
        fileobj.write(f'''
                dynasty = {charobj.dynasty}           
        ''')
    else:
        pass                    
    fileobj.write(f'''
                religion = {charobj.religion}
                culture = {charobj.culture}                 
    ''')
    if charobj.isfemale == True:
        fileobj.write(f'\t\t\tfemale = yes\n')
    else:
        pass
    ##Leave space here for traits/skills later on##
    for i, v in enumerate(charobj.traits):
        fileobj.write(f'''
                trait = {v}''')

    if charobj.inDynasty == True:
        fileobj.write(f'''
                father ={charobj.father}
                mother ={charobj.mother}         
        ''')
    else:
        pass     
    fileobj.write(f'''
                {charobj.birthyear}.{charobj.birthmonth}.{charobj.birthday} = {{
                    birth = yes
                }}
                {charobj.deathyear}.{charobj.deathmonth}.{charobj.deathday} = {{
                    death = yes
                }}
    }}
    ''')



def find_between_tags(lst, start_tag, end_tag):
    start_index = lst.index(start_tag)
    end_index = lst.index(end_tag, start_index)
    return lst[start_index + 1: end_index]

names_male = find_between_tags(name_list,"male:{","}")
names_female = find_between_tags(name_list,"female:{","}")

names_male = [i.split() for i in names_male]
names_female = [i.split() for i in names_female]

names_male = [num for elem in names_male for num in elem]
names_female = [num for elem in names_female for num in elem]


