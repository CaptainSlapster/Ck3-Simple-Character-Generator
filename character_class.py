'''
Character class. This will only generate characters right now.
'''
import random


class Character():
    def __init__(self):
        self.id = 0
        self.name = ""
        self.age = 0
        self.isfemale = False
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
    #    self.dynasty = 0
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
    def determine_birth(self,start_year,min_age,max_age):
        ##Generates the birth year and age for the character object##
        chooser = random.randrange(min_age,max_age)        
        self.age = chooser
        self.birthyear = start_year - self.age
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


    def determine_deathyear(self,start_year,min_age,max_age):
        age_range = random.randrange(min_age,max_age)
        #laziness for now
        self.deathyear = (start_year + max_age)
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
            


    #    if self.age >=age_range:
    #        self.deathyear = start_year + self.age
    #    return self.deathyear
    #def determine_dynasty(self,dynastyid):
    #    self.dynasty = dynastyid
    #    return self.dynasty