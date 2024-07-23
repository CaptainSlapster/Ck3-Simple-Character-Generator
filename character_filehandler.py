
##File handling#

names_file = 'names.txt'

names_male = []
names_female = []
name_list = []

with open(names_file, 'r') as infile:
    for line in infile:
        name_list.append(line.strip(' \n,'))


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
    for i, v in enumerate(charobj.traits):
        fileobj.write(f'''
                trait = {v}''')

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


