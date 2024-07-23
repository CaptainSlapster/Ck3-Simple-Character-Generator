'''
Character class. This will only generate characters right now.
'''
import random
from character_dynasty import *

class Character():
    def __init__(self):
        self.id = 0
        self.name = ""
        self.age = 0
        self.isfemale = False
        self.inDynasty = False #default for count function
        self.birthyear = 0
        self.birthmonth = 0
        self.birthday = 0
        self.deathyear = 0
        self.deathmonth = 0
        self.deathday = 0
        self.femalechance = random.random()
        self.culture = ''
        self.religion = ''
        #this will fill up with traits and will add the traits later from a file 
        self.traits = []
        self.dynasty = 0
        self.dead = False


    def determine_gender(self,female_chance):
        fchance = random.random()

        if female_chance == 0:
            self.isfemale = False
            return
        elif female_chance == 100:
            self.isfemale = True
            return
        
        female_chance = female_chance / 100
        if female_chance > fchance:
            self.isfemale = True
        else:
            self.isfemale = False
        
        return self.isfemale
    def determine_birth_death(self,start_year,min_age,max_age):
        ##Generates the birth year and age for the character object##
        random.seed()
        set_age = random.randrange(min_age,max_age)
        mortality_chance = random.random() * 100
        age_mod = set_age

        base_death_chance = mortality_chance + age_mod
        max_death_chance = 100 + max_age

        if base_death_chance > 100 + max_age:
            base_death_chance = max_death_chance

        self.age = set_age
        if self.age >= max_age:
            self.age = max_age
        elif self.age <= min_age:
            self.age = min_age

        ##Kept getting around 500-515 for a death range. This should open it up a bit##
        self.birthyear = (start_year + random.randrange(-25,50)) - self.age

        ###DEATH STUFF###
        if base_death_chance >= max_death_chance:
            self.dead = True

        if base_death_chance > 50:
            self.dead = True

        if self.dead == True:
            self.deathyear = self.birthyear + self.age

        #Death catch all in case they're not generated dead#
        #I'll just make it around 50-70 years 
        if self.dead == False:
            deathdate = random.randrange(25,45)
            if self.age <= max_age + deathdate:
                self.deathyear = self.birthyear + self.age + deathdate
            elif self.age <= max_age:
                self.deathyear = self.birthyear + self.age

        ##Random stuff for the months/days##
        self.birthmonth = random.randrange(1,12)
        if self.birthmonth == 2:
            self.birthday = random.randrange(1,28)
        elif self.birthmonth % 2:
            if self.birthmonth == 8:
                self.birthday = random.randrange(1,31)
            else:
                self.birthday = random.randrange(1,30)
        else:
            self.birthday = random.randrange(1,31)
        self.deathmonth = random.randrange(1,12)
        if self.deathmonth == 2:
            self.deathday = random.randrange(1,28)
        elif self.deathmonth % 2:
            if self.birthmonth == 8:
                self.deathday = random.randrange(1,31)
            else:
                self.deathday = random.randrange(1,30)
        else:
            self.deathday = random.randrange(1,31)
  
    def determine_name(self,names_male,names_female):
        random.seed()
        if self.isfemale == True:
            self.name = random.choice(names_female)
        else:
            self.name = random.choice(names_male)
        return self.name
    
    def determine_traits(self,trait_list,max_traits):
        tl = trait_list
        for i in range(random.randrange(max_traits)):
            self.traits.append(random.choice(tl))
        
    def create_character(self,charid,start_year,min_age,max_age,religion,culture,percent_female,trait_no,names_male,names_female,trait_list):
        #initialize character
        char = Character()
        char.id = charid
        char.determine_birth_death(start_year,min_age,max_age)
        char.determine_gender(percent_female)
        if trait_no > 0:
            char.determine_traits(trait_list,trait_no)
        else:
            pass
        char.culture = culture
        char.religion = religion
        char.name = char.determine_name(names_male,names_female)
        return char
