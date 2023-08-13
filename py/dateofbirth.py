#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

def digit_sum(num):
    return sum([int(char) for char in str(num)])

x = datetime.datetime.now()
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
            year_now = x.year
        else:
            year_now = int(whichYear)
        
        self.yearNow = year_now
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
        preLifePath = m + d + y
        
        lifePath = self.resultForLifeNum(preLifePath)['core']
        
        
        if lifePath == m:
            subelem = m
        else:
            subelem = 0
        
        
        
        #personal year number bd + bm + cy1
        prePersonalYearNum = (dd + mm + currentYear)
        
        PersonalYearNum = self.resultForLifeNum(prePersonalYearNum)
        
        bLpBrigde = abs(lifePath - d)
        
        
        
        #print(lifePath, PersonalYearNum)    
        
        return {'lifePath':self.resultForLifeNum(preLifePath), 'subelem':subelem,
                'yearNum':PersonalYearNum, 'bLpBrigde':bLpBrigde
                }
    
    def personalYearNum(self):
        #personal year number bd + bm + cy1
        prePersonalYearNum = (self.dd + self.mm + self.currentYear)
        return self.resultForCores(prePersonalYearNum)
    
    def personalMonthNum(self):
        #personal month number calendermonth + personal year
        prePersonalMonthNum = (int(month_now) + self.personalYearNum()['core'])
        return self.resultForCores(prePersonalMonthNum)
        
       