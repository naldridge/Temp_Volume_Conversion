from os import system, name
from Converter_Classes import *
import time,os,sys

# clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux
    else:
        _ = system('clear')

#Intro Message#
def welcome():
    clear()
    print("Welcome to the Unit Conversion Tester")
    time.sleep(2)
    print("To begin Select Temperature or Volume:")
    print("Type 1 for Temperature")
    print("Type 2 for Volume")
    user_input = input()
    if user_input == "1":
        temp_converter()
    else:
        volume_converter()

#Temperature Conversion Tool#
def temp_converter():
    clear()
    question = Temp()
    print("Temperature Converter")

    #Starting Temperature Unit Selection#
    print("To begin select the starting temperature unit:")
    time.sleep(2)
    print("--Type C for Celsius--")
    print("--Type F for Fahrenheit--")
    print("--Type K for Kelvin--")
    print("--Type R for Rankine--")
    input_unit = input()
    question.input_unit = input_unit.capitalize()    
    clear()
    print("Great! You selected ", question.input_unit)
    time.sleep(2)

    #Target Temperature Unit Selection#
    print("Now what would you like your target unit to be?")
    if question.input_unit == "C":
        print("--Type F for Fahrenheit--")
        print("--Type K for Kelvin--")
        print("--Type R for Rankine--")
    elif question.input_unit == "F":
        print("--Type C for Celsius--")
        print("--Type K for Kelvin--")
        print("--Type R for Rankine--")
    elif question.input_unit == "K":
        print("--Type C for Celsius--")
        print("--Type F for Fahrenheit--")
        print("--Type R for Rankine--")
    elif question.input_unit == "R":
        print("--Type C for Celsius--")
        print("--Type F for Fahrenheit--")
        print("--Type K for Kelvin--")
    else:
        print("I didn't understand that. Let's start over.")
        temp_converter()
    target_unit = input()
    question.target_unit = target_unit.capitalize()
    clear()
    print("Great! So you would like to convert ", question.input_unit, " into ", question.target_unit)
    time.sleep(2)

    #User inputs starting temperature in degrees#
    print("Input the number in °", question.input_unit, " you would like to convert.")
    print("*From here on out we will automatically round all numbers to the tenths place (example: 10.54 = 10.5)*")
    question.start_degrees = round(float(input()), 1)
    time.sleep(2)
    clear()

    #User inputs guess for target temperature in degrees#
    print("Now ", question.start_degrees, "°", question.input_unit, " =  ? °", question.target_unit)
    print ("Type your answer")
    question.guess_target = round(float(input()), 1)

    #Converts input temperature to target temperature based on selections#
    if question.input_unit == "C" and question.target_unit == "F":
        question.answer_target = question.convert_c_to_f()
    elif question.input_unit == "C" and question.target_unit == "K":
        question.answer_target = question.convert_c_to_k()
    elif question.input_unit == "C" and question.target_unit == "R":
        question.answer_target = question.convert_c_to_r()
    elif question.input_unit == "F" and question.target_unit == "C":
        question.answer_target = question.convert_f_to_c()
    elif question.input_unit == "F" and question.target_unit == "K":
        question.answer_target = question.convert_f_to_k()
    elif question.input_unit == "F" and question.target_unit == "R":
        question.answer_target = question.convert_f_to_r()
    elif question.input_unit == "K" and question.target_unit == "C":
        question.answer_target = question.convert_k_to_c()
    elif question.input_unit == "K" and question.target_unit == "F":
        question.answer_target = question.convert_k_to_f()
    elif question.input_unit == "K" and question.target_unit == "R":
        question.answer_target =question.convert_k_to_r()
    elif question.input_unit == "R" and question.target_unit == "C":
        question.answer_target = question.convert_r_to_c()
    elif question.input_unit == "R" and question.target_unit == "F":
        question.answer_target = question.convert_r_to_f()
    elif question.input_unit == "R" and question.target_unit == "K":
        question.answer_target = question.convert_r_to_k()

    #Validation will return correct or incorrect statements based on the accuracy of the user's guess#
    question.validate_answer()
    time.sleep(2)
    end_menu()


#Menu allows user to restart the temp conversion or continue to Volume Conversion#
def end_menu():
        print("1. Try Temp Conversion?")
        print("2. Try Volume Conversion?")
        print("3. Exit")
        user_input = input()
        if user_input == "1":
            temp_converter()
        elif user_input == "2":
            volume_converter()
        else:
            exit()

def volume_converter():
    clear()
    question = Volume()
    print("Volume Converter")

    #Starting Volume Unit Selection#
    print("To begin select the starting Volume unit:")
    time.sleep(2)
    print("--Type L for Liter--")
    print("--Type T for Tablespoon--")
    print("--Type C for Cup--")
    print("--Type CI for Cubic-Inch--")
    print("--Type CF for Cubic-Foot--")
    print("--Type G for Gallon--")
    input_unit = input()
    question.input_unit = input_unit.capitalize()    
    clear()
    print("Great! You selected ", question.input_unit)
    time.sleep(2)

    #Target Volume Unit Selection#
    print("Now what would you like your target unit to be?")
    if question.input_unit == "L":
        print("--Type T for Tablespoon--")
        print("--Type C for Cup--")
        print("--Type CI for Cubic-Inch--")
        print("--Type CF for Cubic-Foot--")
        print("--Type G for Gallon--")
    elif question.input_unit == "T":
        print("--Type L for Liter--")
        print("--Type C for Cup--")
        print("--Type CI for Cubic-Inch--")
        print("--Type CF for Cubic-Foot--")
        print("--Type G for Gallon--")
    elif question.input_unit == "C":
        print("--Type L for Liter--")
        print("--Type T for Tablespoon--")
        print("--Type CI for Cubic-Inch--")
        print("--Type CF for Cubic-Foot--")
        print("--Type G for Gallon--")
    elif question.input_unit == "CI":
        print("--Type L for Liter--")
        print("--Type T for Tablespoon--")
        print("--Type C for Cup--")
        print("--Type CF for Cubic-Foot--")
        print("--Type G for Gallon--")
    elif question.input_unit == "C":
        print("--Type L for Liter--")
        print("--Type T for Tablespoon--")
        print("--Type CI for Cubic-Inch--")
        print("--Type CF for Cubic-Foot--")
        print("--Type G for Gallon--")
    elif question.input_unit == "CF":
        print("--Type L for Liter--")
        print("--Type T for Tablespoon--")
        print("--Type C for Cup--")
        print("--Type CI for Cubic-Inch--")
        print("--Type G for Gallon--")
    elif question.input_unit == "G":
        print("--Type L for Liter--")
        print("--Type T for Tablespoon--")
        print("--Type C for Cup--")
        print("--Type CI for Cubic-Inch--")
        print("--Type CF for Cubic-Foot--")
    else:
        print("I didn't understand that. Let's start over.")
        volume_converter()
    target_unit = input()
    question.target_unit = target_unit.capitalize()
    clear()
    print("Great! So you would like to convert ", question.input_unit, " into ", question.target_unit)
    time.sleep(2)

    #User inputs starting volume to convert#
    print("Input the number in", question.input_unit, "you would like to convert.")
    print("*From here on out we will automatically round all numbers to the tenths place (example: 10.54 = 10.5)*")
    user_input = input()
    question.input_volume = round(float(user_input), 1)
    time.sleep(2)
    clear()

    #User inputs guess for target volume#
    print("Now ", question.input_volume, question.input_unit, " =  ?", question.target_unit)
    print ("Type your answer")
    question.guess_target = round(float(input()), 1)

    #Class method to convert the input volume from the starting unit to the target unit#
    if question.input_unit == "L" and question.target_unit == "T":
        question.answer_target = question.convert_l_to_t()
    elif question.input_unit == "L" and question.target_unit == "CI":
        question.answer_target = question.convert_l_to_ci()
    elif question.input_unit == "L" and question.target_unit == "C":
        question.answer_target = question.convert_l_to_c()
    elif question.input_unit == "L" and question.target_unit == "CF":
        question.answer_target = question.convert_l_to_cf()
    elif question.input_unit == "L" and question.target_unit == "G":
        question.answer_target = question.convert_l_to_g()
    elif question.input_unit == "T" and question.target_unit == "L":
        question.answer_target = question.convert_t_to_l()
    elif question.input_unit == "T" and question.target_unit == "CI":
        question.answer_target = question.convert_t_to_ci()
    elif question.input_unit == "T" and question.target_unit == "C":
        question.answer_target = question.convert_t_to_c()
    elif question.input_unit == "T" and question.target_unit == "CF":
        question.answer_target = question.convert_t_to_cf()
    elif question.input_unit == "T" and question.target_unit == "G":
        question.answer_target = question.convert_t_to_g()
    elif question.input_unit == "CI" and question.target_unit == "T":
        question.answer_target = question.convert_ci_to_t()
    elif question.input_unit == "CI" and question.target_unit == "L":
        question.answer_target = question.convert_ci_to_l()
    elif question.input_unit == "CI" and question.target_unit == "C":
        question.answer_target = question.convert_ci_to_c()
    elif question.input_unit == "CI" and question.target_unit == "CF":
        question.answer_target = question.convert_ci_to_cf()
    elif question.input_unit == "CI" and question.target_unit == "G":
        question.answer_target = question.convert_ci_to_g()
    elif question.input_unit == "CF" and question.target_unit == "T":
        question.answer_target = question.convert_cf_to_t()
    elif question.input_unit == "CF" and question.target_unit == "L":
        question.answer_target = question.convert_cf_to_l()
    elif question.input_unit == "CF" and question.target_unit == "C":
        question.answer_target = question.convert_cf_to_c()
    elif question.input_unit == "CF" and question.target_unit == "CI":
        question.answer_target = question.convert_cf_to_ci()
    elif question.input_unit == "CF" and question.target_unit == "G":
        question.answer_target = question.convert_cf_to_g()
    elif question.input_unit == "C" and question.target_unit == "T":
        question.answer_target = question.convert_c_to_t()
    elif question.input_unit == "C" and question.target_unit == "L":
        question.answer_target = question.convert_c_to_l()
    elif question.input_unit == "C" and question.target_unit == "CI":
        question.answer_target = question.convert_c_to_c()
    elif question.input_unit == "C" and question.target_unit == "CF":
        question.answer_target = question.convert_c_to_cf()
    elif question.input_unit == "C" and question.target_unit == "G":
        question.answer_target = question.convert_c_to_g()
    elif question.input_unit == "G" and question.target_unit == "T":
        question.answer_target = question.convert_g_to_t()
    elif question.input_unit == "G" and question.target_unit == "L":
        question.answer_target = question.convert_g_to_l()
    elif question.input_unit == "G" and question.target_unit == "C":
        question.answer_target = question.convert_g_to_c()
    elif question.input_unit == "G" and question.target_unit == "CF":
        question.answer_target = question.convert_g_to_cf()
    elif question.input_unit == "G" and question.target_unit == "CI":
        question.answer_target = question.convert_g_to_ci()

    #Validation will return correct or incorrect statements based on the accuracy of the user's guess#
    question.validate_answer()
    time.sleep(2)

    #Menu allows user to restart the Volume Conversion or continue to Temp Conversion#
    end_menu()
    

welcome()