# -*- coding: utf-8 -*-
"""
Functions about calendars

This program provides the functionality to check Leap-Years using
either the Gregorian or Milankovican calendars.

"I have neither given nor received help on this assignment."
author: Xander Dyer (xdyer)
"""
__version__ = 1

import pytest

def gregorian(year):
    # This function checks if a given year is a Gregorian leap year
    # Input: a specific year
    # Returns: Whether the year is a leap year or not
    # A logic tree to determine if a given year is a Gregorian Leap year
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False


def milankovic(year):
    # This function checks if a given year is a Milankovic leap year
    # Input: a specific year
    # Returns: Whether the year is a leap year or not
    # A logic tree to determine if a given year is a Milankovican Leap year
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 900 == 200 or year % 900 == 600:
                return True
            else:
                return False
        else: 
            return True
    else: 
        return False
        


def gregorian_count(year1, year2):
    # This function determines the number of leap years that lie 
    # between two dates on the Gregorian calendar.
    # Input: a range of years (Year 1 must be smaller than Year 2)
    # Returns: the number of leap years within the given 
    # range (year2 non-inclusive)
    
    if year1 >= year2:
        raise ValueError("Invalid range: year1 must be larger than year2")       
    
    count = 0
    for year in range(year1, year2):
        #Loops through given range of years counting each leap year
        if gregorian(year) == True:
            count += 1
    return count


def milankovic_count(year1, year2):
    # This function determines the number of leap years that lie 
    # between two dates on the Milankovican calendar.
    # Input: a range of years (Year 1 must be smaller than Year 2)
    # Returns: the number of leap years within the given 
    # range (year2 non-inclusive)
    
    if year1 >= year2:
        raise ValueError("Invalid range: year1 must be larger than year2")  
    
    count = 0    
    for year in range(year1, year2):
        #Loops through given range of years counting each leap year
        if milankovic(year) == True:
            count += 1
    return count


def main():
    # Runs test conditions for the program
    
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    testGC()
    testMC()
    
    print("All tests passed!")



###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for gregorian()
def test1():
    # Tests to see if a year divisible by 4 but not by 100 returns True
    assert gregorian(1696) == True, "The function does not provide correct "
    "feedback given a Gregorian Leap year"
    assert gregorian(4) == True, "The function does not provide correct "
    "feedback given a Gregorian Leap year"

def test2():
    # Tests if a year is divisible by 4 and also 100 but not 400 returns False
    assert gregorian(100) == False, "The function does not provide correct "
    "feedback given a non-Gregorian Leap year"
    assert gregorian(600) == False, "The function does not provide correct "
    "feedback given a non-Gregorian Leap year"
    
def test3():
    # Tests to see if a year divisible by 4, 100 and 400 returns True
    assert gregorian(400) == True, "The function does not provide correct "
    "feedback given a Gregorian Leap year"
    assert gregorian(1200) == True, "The function does not provide correct "
    "feedback given a Gregorian Leap year"

def test4():
    # Tests to see if a year not divisible by 4 returns False
    assert gregorian(3) == False, "The function does not provide correct "
    "feedback given a non-Gregorian Leap year"
    assert gregorian(1697) == False, "The function does not provide correct "
    "feedback given a non-Gregorian Leap year"

# Below are the tests for milankovic()
def test5():
    # Tests to see if a year divisible by 4 but not by 100 returns True
    assert milankovic(1696) == True, "The function does not provide correct "
    "feedback given a Milankovican Leap year"
    assert milankovic(4) == True, "The function does not provide correct "
    "feedback given a Milankovican Leap year"

def test6():
    # Tests to see if a year divisible by 4 and also 100 but does not
    # have remainder of 200 or 600 when divided by 900 returns False
    assert milankovic(1200) == False, "The function does not provide correct "
    "feedback given a non-Milankovican Leap year"
    assert milankovic(800) == False, "The function does not provide correct "
    "feedback given a non-Milankovican Leap year"
    
def test7():
    # Tests to see if a year divisible by 4 + 100 and has a remainder of 
    # of 200 or 600 when divided by 900 returns True
    assert milankovic(1500) == True, "The function does not provide correct "
    "feedback given a Milankovican Leap year"
    assert milankovic(1100) == True, "The function does not provide correct "
    "feedback given a Milankovican Leap year"

def test8():
    # Tests to see if a year not divisible by 4 returns False
    assert milankovic(3) == False, "The function does not provide correct "
    "feedback given a non-Milankovican Leap year"
    assert milankovic(1697) == False, "The function does not provide correct "
    "feedback given a non-Milankovican Leap year"

# Below are the tests for gregorian_count()
def testGC():
    # Tests various edge cases
    assert gregorian_count(0, 4) == 1, "The function does not provide correct "
    "feedback given a range of Gregorian calendar years" 
    with pytest.raises(ValueError):
        gregorian_count(4, 4)
    with pytest.raises(ValueError):
        gregorian_count(4, 3)
    assert gregorian_count(1, 3) == 0, "The function does not provide correct "
    "feedback given a range of Gregorian calendar years"
    assert gregorian_count(1696, 1697) == 1, "The function does not provide" 
    "correct feedback given a range of Gregorian calendar years"
    assert gregorian_count(1900, 1901) == 0, "The function does not provide" 
    "correct feedback given a range of Gregorian calendar years"
    assert gregorian_count(2000, 3000) == 243, "The function does not provide" 
    "correct feedback given a range of Gregorian calendar years"
    assert gregorian_count(2000, 2850) == 207, "The function does not provide" 
    "correct feedback given a range of Gregorian calendar years"   

# Below are the tests for milankovic_count()
def testMC():
    # Tests various edge cases
    assert milankovic_count(0, 4) == 0, "The function does not provide" 
    "correct feedback given a range of Milankovican calendar years" 
    with pytest.raises(ValueError):
        milankovic_count(4, 4)
    with pytest.raises(ValueError):
        milankovic_count(4, 3)
    assert milankovic_count(1, 3) == 0, "The function does not provide" 
    "correct feedback given a range of Milankovican calendar years"
    assert milankovic_count(1696, 1697) == 1, "The function does not provide" 
    "correct feedback given a range of Milankovican calendar years"
    assert milankovic_count(1900, 1901) == 0, "The function does not provide" 
    "correct feedback given a range of Milankovican calendar years"
    assert milankovic_count(2000, 3000) == 243, "The function does not provide" 
    "correct feedback given a range of Milankovican calendar years"
    assert milankovic_count(2000, 2850) == 206, "The function does not provide" 
    "correct feedback given a range of Milankovican calendar years"

    
###############################################################    
    
if __name__ == "__main__":
    main()    