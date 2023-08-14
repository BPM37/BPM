#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

def digit_sum(num):
    return sum([int(char) for char in str(num)])

x = datetime.datetime.now()

#x = datetime.datetime(2017, 7, 20)

year_now = x.year
month_now = x.strftime("%m")
day_now = x.strftime("%d")


class DateOfBirth:
    def __init__(self, dob, whichYear):
        self.dob = dob
        self.dd = digit_sum(int(dob[0:2]))
        self.mm = digit_sum(int(dob[3:5]))
        self.yyyy = digit_sum(digit_sum(int(dob[6:10])))
        
        self.whichYear = whichYear
        
        self.masters = [11, 22]
        self.num_behind = [13, 14, 16, 19]
        
        #is year current or in past
        if whichYear == "forNow":
            self.yearNow = year_now
        else:
            self.yearNow = int(whichYear)
            
            
        #current year
        self.currentYear = digit_sum(self.yearNow)
        
        
    def resultForCores(self, num):
        if num in self.masters:
            core = num
        else:
            core = digit_sum(digit_sum(num))
            
        if num in self.num_behind:
            coreKarma = num
        else:
            coreKarma = 0
            
        return {'core':core, 'coreKarma':coreKarma}
    
        
    def lifePath(self):
        #Feb 22 1982
        preLifePath = self.mm + self.dd + self.yyyy
        lifePath = self.resultForCores(preLifePath)['core']
        
        if lifePath == self.mm:
            subelem = self.mm
        else:
            subelem = 0
        bLpBrigde = abs(lifePath - self.dd)
        
        def __str__(self):
            return "{'core': 8, 'karma': 0, 'subelem': 0, 'birthdayLifepathBrigde': 4}"
        
        return {'core':self.resultForCores(preLifePath)['core'], 'karma':self.resultForCores(preLifePath)['coreKarma'],
                'subelem':subelem,'birthdayLifepathBrigde':bLpBrigde}
    
    def personalYearNum(self):
        #personal year number bd + bm + cy1
        prePersonalYearNum = self.dd + self.mm + self.currentYear
        return self.resultForCores(prePersonalYearNum)
    
    def personalMonthNum(self):
        #personal month number calendermonth + personal year
        prePersonalMonthNum = int(month_now) + self.personalYearNum()['core']
        return self.resultForCores(prePersonalMonthNum)
    
    def personalDayNum(self):
        #personal day number= calendermonth + calenderday + personal year
        prePersonalDayNum = int(month_now) + int(day_now) + self.personalYearNum()['core']
        return self.resultForCores(prePersonalDayNum)
    
    def __str__(self):
            return "methods = lifePath, personalYearNum, personalMonthNum, personalDayNum"
       
oracle = DateOfBirth('22/02/1982', 'forNow')
print(oracle)
print(oracle.personalYearNum()['core'])
print(oracle.personalMonthNum()['core'])
print(oracle.personalDayNum()['core'])



