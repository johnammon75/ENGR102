# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         John Ammon
# Section:      528
# Assignment:   Lab0b-2 
# Date:         3 2 2021
#

import math, numpy
#Part A: 
    
mass = 2 #Create a variable for mass
acceleration = 5 #Create a variable for acceleration
Force = mass * acceleration #Multiply mass times acceleration to get force

print("Force is", Force, "N") #print out the force


#Part B:
    
distance = 0.025 #Create a variable for distance
degree = numpy.radians(25) #Create a variable for degrees
wavelength = 2 * distance * (math.sin(degree)) #Calculate wavelength
print("Wavelength is", wavelength, "nm") #print the wavelength

#Part C: 
    
time = 5 #Create a variable for the days/time passed
initial_amount = 3 #Create a variable for the initial amount of grams
half_life = 3.8 #Create a variable for the elements half life
radon222_left = initial_amount * math.pow(2 , -time/half_life) #Calculate the amount of radon22 left
print("Radon-222 left is", radon222_left, "g") #print amount of radon222 left

#Part D:  
    
volume = 0.15 #Create a variable for volume
moles = 0.005 #Create a variable for moles
constant = 8.314 #Create a variable for constant
temperature = 425 #Create a variable for temperature
pressure = (moles * constant * temperature)/volume #Calculate pressure
print("Pressure is", pressure, "kPa") #Print pressure


    


