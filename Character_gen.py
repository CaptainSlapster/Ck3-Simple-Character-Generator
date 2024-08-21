from character_class import *
from character_trait_handler import *
from character_filehandler import *
import configparser
###MAINFILE
###
#   Yes I will need to rewrite this and make it better. I created it with 3-4 hrs of work.s
###
print("""

Simple CK3 Character Generator by Austin AKA CaptainSlapster!

""")

##INIT#
C = Character()


number_of_characters = int(input("Enter the number of characters to generate: "))

##Create empty file for the characters##
with open('outfile.txt','w+',encoding= 'utf-8')as out:
    out.write('\ufeff')
    
    for i in range(1,number_of_characters):
        char = C.create_character(i,start_year,min_age,max_age,religion,culture,percent_female,trait_number,names_male,names_female,trait_list,min_date_range,max_date_range)
        print("birth year: " + str(char.birthyear))
        print("age: " + str(char.age))
        print("death year: " + str(char.deathyear))
        
        generate_text(out,char)


