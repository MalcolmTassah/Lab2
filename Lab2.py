"""
Malcolm Tassah - Lab 2 - 9/6/2024

"""
Human_Years = float(input("Enter your age: "))



#Dog Calculator

#each dog year is a human year times 7
dog_age = Human_Years * 7

#making it a int value
dog_years = int(dog_age)

#separates raiming fraction of year but subtracting to get full year
dog_fractional_year = dog_age - dog_years

#finding the months for dogs
dog_months = int(dog_fractional_year * 12)

#the remaining of the months I use for days in this equation since each month is around 30 days
dog_days = int(((dog_fractional_year * 12) %1)*30)

print(f'Your age in dog years is, {dog_years} years {dog_months} months and {dog_days} days') 




#Cat Calculator

#each cat year is 9 human years so use division isntead of multiplication
cat_age = Human_Years / 9

#making it a int value
cat_years = int(cat_age)

#separates raiming fraction of year but subtracting to get full year
cat_fractional_year = cat_age - cat_years

#finding the months for cats
cat_months = int(cat_fractional_year * 12)

#the remaining of the months I use for days in this equation since each month is around 30 days
cat_days = int(((cat_fractional_year * 12) %1)*30)

print(f'Your age in cat years is, {cat_years} years {cat_months} months and {cat_days} days') 




#Horse Calculator

#equation for horse years from lab pdf
horse_age = 3*(((Human_Years **2 - 47)/7)+ 12)

#making it a int value
horse_years = int(horse_age)

#separates raiming fraction of year but subtracting to get full year
horse_fractional_year = horse_age - horse_years

#finding the months for horse
horse_months = int(horse_fractional_year * 12)

#the remaining of the months I use for days in this equation since each month is around 30 days
horse_days = int(((horse_fractional_year * 12) %1)*30)

print(f'Your age in horse years is, {horse_years} years {horse_months} months and {horse_days} days')
