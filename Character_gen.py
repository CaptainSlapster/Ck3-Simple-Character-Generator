from character_class import *
from trait_handler import *
from character_filehandler import *
import sys,configparser
###MAINFILE
###
#   Yes I will need to rewrite this and make it better. I created it with 3-4 hrs of work.s
###
print("""

Simple CK3 Character Generator by Austin Smith AKA CaptainSlapster!

""")

##INIT#
C = Character()
config = configparser.ConfigParser()
##TEST VARIABLES
config.read('test_config.ini')
start_year = int(config.get('CONFIG','start_year'))
min_age = int(config.get('CONFIG','min_age'))
max_age = int(config.get('CONFIG','max_age'))
trait_number = int(config.get('CONFIG','no_of_traits'))

religion = config.get('CONFIG','religion')
culture = config.get('CONFIG','culture')

percent_female = int(input("Enter a percentage rate for female characters e.g. 0 = 0% 100 = 100%: "))

number_of_characters = int(input("Enter the number of characters to generate: "))

#names_file = sys.argv[1]


##Create empty file for the characters##
with open('outfile.txt','w+',encoding= 'utf-8')as out:
    out.write('\ufeff')
    for i in range(1,number_of_characters):
        char = C.create_character(i,start_year,min_age,max_age,religion,culture,percent_female,trait_number,names_male,names_female,trait_list)
        generate_text(out,char)

