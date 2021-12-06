# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:24:01 2021

@author: wbelden
"""
import csv

    # The class dateClass is used to initialize and store a date given the number of days that have passed since 01/01/2021.
class dateClass:
    def __init__(self, daysToPass):
        
        self.daysPassed = daysToPass                        # This is the number of days passed since 01/01/2021
        self.yearsPassed = self.set_yearsPassed()           # This is the number of years passed since 2021
        self.dateYear = self.set_year()                     # This is the year number of the date being created
        self.leapDays = self.set_leapDays()                 # This is the number of leapDays that occurred since 2021
        self.daysRemainder = self.set_daysRemainder()       # This is the number of days remaining after accounting for the years passed & leap days
        self.monthDay = self.set_monthDay()                 # This is an array containing month number at index 0 and day number at index 1
        self.dateMonth = self.monthDay[0]                   # This is the month number of the date being created
        self.dateDay = self.monthDay[1]                     # This is the day number of the date being created
        self.weekdayNum = self.daysPassed % 7               # This is the number corresponding to the day of the week
        self.dayOfWeek = self.set_dayOfWeek()               # This is the string value for the day of the week
        
            # ID for easier parsing when using the JSON file
        self.dateID = str("{:04d}{:02d}{:02d}".format(self.dateYear, self.dateMonth, self.dateDay))         
        

        # the set_yearsPassed function is used to return the number of years that passed since 2021        
    def set_yearsPassed(self):
        
            # the initial if statement checks to see if the next leap year has occured (2024)
            # if not, then the number of years passed 2021 is returned by dividing days passed by 365 days and rounding down
        if self.daysPassed // 365 < 3:
            return (self.daysPassed // 365)
        
            # the elif checks to see if the year is the the first leap year (2024) 
        elif (self.daysPassed) // 365 == 3:

                # next we check if the date is before Feb 28th 
                # if so, we do nothing because the leap day has not occured
                # this is accomplished by subtracting 3 years of non-leap year days from the days passed 2021 and if that is less than the number of days from Jan 1st to Feb 28th 
            if self.daysPassed - (3 * 365) < 58:
                return ((self.daysPassed) // 365)

                # if the date is after Feb 28th, then the leap day has occurred and we must subtract 1 day from the days passed before finding the years passed
                # if we don't do this, when we try to create a date in a leap year, a logic error occurs and the wrong date is returned instead
            else:
                return ((self.daysPassed - 1) // 365)

            # the rest of this function repeats the above steps for different sets of years

            # 2025, 2026, 2027
        elif ((self.daysPassed - 1) // 365) < 7:
            return ((self.daysPassed - 1) // 365)

            # 2028
        elif (self.daysPassed - 1) // 365 == 7:
            if self.daysPassed - (7 * 365) - 1 < 58:
                return ((self.daysPassed - 1) // 365)
            else:
                return ((self.daysPassed - 2) // 365)

            # 2029, 2030, 2031
        elif ((self.daysPassed - 2) // 365) < 11:
            return ((self.daysPassed - 2) // 365)

            # 2032 
        elif (self.daysPassed - 2) // 365 == 11:
            if ((self.daysPassed - (11 * 365) - 2)) < 58:
                return ((self.daysPassed - 2) // 365)
            else:
                return ((self.daysPassed - 3) // 365)

            # 2033, 2034, 2035
        elif ((self.daysPassed - 3) // 365) < 15:
            return ((self.daysPassed - 3) // 365)

            # 2036
        elif (self.daysPassed - 3) // 365 == 15:
            if ((self.daysPassed - 5475 - 3)) < 58:
                return ((self.daysPassed - 3) // 365)
            else:
                return ((self.daysPassed - 4) // 365)

            # 2037, 2038, 2039
        elif ((self.daysPassed - 4) // 365) < 19:
            return ((self.daysPassed - 4) // 365)

            # 2040
        elif (self.daysPassed - 4) // 365 == 19:
            if ((self.daysPassed - 5475 - 4)) < 58:
                return ((self.daysPassed - 4) // 365)
            else:
                return ((self.daysPassed - 5) // 365)

            # 2041, 2042, 2043
        elif ((self.daysPassed - 5) // 365) < 23:
            return ((self.daysPassed - 5) // 365)

            # 2044
        elif (self.daysPassed - 5) // 365 == 23:
            if ((self.daysPassed - 5475 - 5)) < 58:
                return ((self.daysPassed - 5) // 365)
            else:
                return ((self.daysPassed - 6) // 365)

            # 2045, 2046, 2047
        elif ((self.daysPassed - 6) // 365) < 27:
            return ((self.daysPassed - 6) // 365)

            # 2048
        elif (self.daysPassed - 6) // 365 == 27:
            if ((self.daysPassed - 5475 - 6)) < 58:
                return ((self.daysPassed - 6) // 365)
            else:
                return ((self.daysPassed - 7) // 365)

            # 2049, 2050, 2051
        elif ((self.daysPassed - 7) // 365) < 31:
            return ((self.daysPassed - 7) // 365)

            # 2052
        elif (self.daysPassed - 7) // 365 == 31:
            if ((self.daysPassed - 5475 - 7)) < 58:
                return ((self.daysPassed - 7) // 365)
            else:
                return ((self.daysPassed - 8) // 365)

            # 2053, 2054, 2055
        else:
            return ((self.daysPassed - 8) // 365)


        # This function sets the year for the created date     
    def set_year(self):
            # Calculated by adding the years passed to the start year, 2021
        return (2021 + self.yearsPassed)


        # This function sets the number of leap days that occurred since 2021
    def set_leapDays(self):
            # Calculation is the number of years passed plus one (to align with the leap years), floor divide by 4 to find how many times a leap year occurred
        return ((self.yearsPassed + 1) // 4)
        

        # This function sets the days remaining after calculating years and leap days
        # In other words, this is the day number for the current year of the date created
    def set_daysRemainder(self):
            # if the date is not in a leap year (years passed plus one to align with leap years, modular division by 4; if calculation is 1, 2, or 3 then not a leap year)
            # calculate by subtracting years passed times 365 days and leapDays that have occurred from the days passed 2021
        if (self.yearsPassed + 1) % 4 != 0:
            daysRem = (self.daysPassed - (self.yearsPassed * 365)) - self.leapDays 

            # if the date is in a leap year, we need to check if the leap day has occurred 
            # this is done by seeing if the calculated day number of the current year is before Feb 29th
        elif (self.daysPassed - (self.yearsPassed * 365)) - self.leapDays < 58:
                # if the day is before Feb 29th, we then calculate the days remaining with the same calculation as above
            daysRem = (self.daysPassed - (self.yearsPassed * 365)) - self.leapDays

            # otherwise we need to add one day to the days passed and then calculate days remaining
        else:
            daysRem = (self.daysPassed + 1) - (self.yearsPassed * 365) - self.leapDays
        return daysRem


        # This function is used to calculate the month & day of the date created
    def set_monthDay(self):
            # First we must check if the year is not a leap year
        if (self.yearsPassed + 1) % 4 != 0:
                # If not a leap year then we determine what month the date is in
                # Additionally, we will pass the number of days in the prior months as a parameter to the set_day function
                
                # January
            if self.daysRemainder + 1 <= 31:
                day = self.set_day(0)
                return 1, day
            
                # February
            elif self.daysRemainder + 1 <= 59:
                day = self.set_day(31)
                return 2, day

                # March
            elif self.daysRemainder + 1 <= 90:
                day = self.set_day(59)
                return 3, day

                # April
            elif self.daysRemainder + 1 <= 120:
                day = self.set_day(90)
                return 4, day

                # May
            elif self.daysRemainder + 1 <= 151:
                day = self.set_day(120)
                return 5, day
                
                # June
            elif self.daysRemainder + 1 <= 181:
                day = self.set_day(151)
                return 6, day

                # July
            elif self.daysRemainder + 1 <= 212:
                day = self.set_day(181)
                return 7, day

                # August
            elif self.daysRemainder + 1 <= 243:
                day = self.set_day(212)
                return 8, day

                # September
            elif self.daysRemainder + 1 <= 273:
                day = self.set_day(243)
                return 9, day

                # October
            elif self.daysRemainder + 1 <= 304:
                day = self.set_day(273)
                return 10, day

                # November
            elif self.daysRemainder + 1 <= 334:
                day = self.set_day(304)
                return 11, day

                # December
            else:
                day = self.set_day(334)
                return 12, day

            # if the date is in a leap year, we need to add one to the date calculation since there is an additional day after february
        else:
                # January
            if self.daysRemainder + 1 <= 31:
                day = self.set_day(0)
                return 1, day

                # February
            elif self.daysRemainder + 1 <= 60:
                day = self.set_day(31)
                return 2, day

                # March
            elif self.daysRemainder + 1 <= 91:
                day = self.set_day(60)
                return 3, day

                # April
            elif self.daysRemainder + 1 <= 121:
                day = self.set_day(91)
                return 4, day

                # May
            elif self.daysRemainder + 1 <= 152:
                day = self.set_day(121)
                return 5, day

                # June
            elif self.daysRemainder + 1 <= 182:
                day = self.set_day(152)
                return 6, day

                # July
            elif self.daysRemainder + 1 <= 213:
                day = self.set_day(182)
                return 7, day

                # August
            elif self.daysRemainder + 1 <= 244:
                day = self.set_day(213)
                return 8, day

                # September
            elif self.daysRemainder + 1 <= 274:
                day = self.set_day(244)
                return 9, day

                # October
            elif self.daysRemainder + 1 <= 305:
                day = self.set_day(274)
                return 10, day

                # November
            elif self.daysRemainder + 1 <= 335:
                day = self.set_day(305)
                return 11, day

                # December
            else:
                day = self.set_day(335)
                return 12, day


        # This function is used to calculate the day of the created date and is called through the set_monthDay function
    def set_day(self, days):
            # Calculated by subtracting the number of days in the prior months (passed as parameter) from the days remaining plus one
        dayPass = (self.daysRemainder + 1) - days
        return dayPass


        # This function sets the name of the weekday
    def set_dayOfWeek(self):
            # determined by the weekdayNum (0-6) corresponding to a specific day of the week
            # note that Friday is index 0 since 01/01/2021 was a friday
        if self.weekdayNum == 2:
            return "Sunday"
        elif self.weekdayNum == 3:
            return "Monday"
        elif self.weekdayNum == 4:
            return "Tuesday"
        elif self.weekdayNum == 5:
            return "Wednesday"
        elif self.weekdayNum == 6:
            return "Thursday"
        elif self.weekdayNum == 0:
            return "Friday"
        elif self.weekdayNum == 1:
            return "Saturday"


        # This function returns a list of date information to be written to the CSV file
    def toCSV(self):
        data = [
            self.dateID,
            self.dateYear,
            self.dateMonth,
            self.dateDay,
            self.dayOfWeek
        ]
        return data


        # custom print for testing
    def __str__(self):
        returnString = str("Date ID: {}\nYear: {}\nMonth: {}\nDay: {}\nDay of Week: {}\nLeap Days: {}\nYears Passed: {}\nDays Remainder: {}".format(self.dateID, self.dateYear, self.dateMonth, self.dateDay, self.dayOfWeek, self.leapDays, self.yearsPassed, self.daysRemainder))
        return returnString


if __name__ == "__main__":

        # Create an empty list and iterator
    dateArray = []
    i = 0

        # While the iterator is less than 12418 (the number of days occurring between 01/01/2021 and 12/31/2054)
        # Append a new class object for each date to the dateArray list
    while i < 12418:
        dateArray.append(dateClass(i))
        i += 1

        # Create a header for the data
    header = ['dateID', 'dateYear', 'dateMonth', 'dateDay', 'dayOfWeek']
        # Run the .toCSV() member function for all dates in the dateArray list, then set the returned values to a list, and apply that to the dates key
    data = (list(map(lambda x:x.toCSV(), dateArray)))
    

        # open a new file and write the data dictionary to it with csv formatting using json.dump 
    with open('dates.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
