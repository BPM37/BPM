import html
import calendar


zodiac = {'AR':0, 'TA':30, 'GE':60, 'CN':90, 'LE':120, 'VI':150, 'LI':180, 'SC':210, 'SG':240, 'CP':270, 'AQ':300, 'PI':330}


consts_dict = {1:['Fortune to get more and more.', 'auspicious'],2:['Will be stolen.','unauspicious'],
               3:['Danger from fire.','unauspicious'],4:['Improves bank position.','auspicious'],
               5:['Will be spoild by rat.','unauspicious'],6:['One loses money.','unauspicious'],
               7:['There can be no troubles.','auspicious'],8:['Promises wealth.','auspicious'],
               9:['Will be destroyed.','unauspicious'],10:['Threatens danger to life.','unauspicious'],
               11:['Threatens trouble from government.','unauspicious'],
               12:['Increases income and offer good health.','auspicious'],13:['Gives success.','auspicious'],
               14:['Will have more and more.','auspicious'],15:['Is good for rich foods.','auspicious'],
               16:['Increases popularity.','auspicious'],17:['For good Friendships and Social Success.','auspicious'],
               18:['Shows loses.','unauspicious'],19:['Lose of things in water.','unauspicious'],
               20:['Health loss.','unauspicious'],21:['Sumptuous feast.','auspicious'],
               22:['Threatens eye disease.','unauspicious'],23:['Good yeild from field.','auspicious'],
               24:['Danger from poison.','unauspicious'],25:['Danger from water.','unauspicious'],
               26:['Child Birth.','auspicious'],27:['Becomes rich, purchases gems.','auspicious'],
               }


consts_num = {'aswini':1,'bharani':2,'krittika':3,'rohini':4,'mrigasira':5,'ardra':6,'punarvasu':7,'pushyami':8,
              'aslesha':9,'magha':10,'poorvaphalguni':11,'uttaraphalguni':12,'rohinihasta':13,'mrigasirachitra':14,
              'ardraswati':15,'visakha':16,'anuradha':17,'jyeshta':18,'moola':19,'poorvashadha':20,'uttarashadha':21,
              'sravana':22,'dhanista':23,'satabhisha':24,'poorvabhadra':25,'uttarabhadra':26,'Revati':27
              }

const_tuple = ((range(0, 14),'ketu', 'aswini'),(range(15, 27), 'ven', 'bharani'),(range(27, 41), 'sun', 'krittika'),
               (range(41, 59), 'mon', 'rohini'),(range(59, 67), 'mars', 'mrigasira'),(range(67, 81), 'rahu', 'ardra'),
               (range(81, 94), 'jup', 'punarvasu'),(range(94, 107), 'sat', 'pushyami'),(range(107, 121), 'merc', 'aslesha'),
               
               (range(121, 134),'ketu', 'magha'),(range(134, 147), 'ven','poorvaphalguni'),
               (range(137, 161), 'sun', 'uttaraphalguni'),(range(161, 174), 'mon', 'hasta'),
               (range(174, 187), 'mars', 'chitra'),(range(187, 201), 'rahu', 'swati'),(range(201, 214), 'jup', 'visakha'),
               (range(214, 227), 'sat', 'anuradha'),(range(227, 241), 'merc', 'jyeshta'),
               
               (range(241, 254),'ketu', 'moola'),(range(254, 267), 'ven', 'poorvashadha'),
               (range(267, 281), 'sun', 'uttarashadha'),(range(281, 294), 'mon', 'sravana'),
               (range(294, 307), 'mars', 'dhanista'),(range(307, 321), 'rahu', 'satabhisha'),
               (range(321, 334), 'jup', 'poorvabhadra'),(range(334, 347), 'sat', 'uttarabhadra'),
               (range(347, 360), 'merc', 'Revati')
               )


week_days = ['Mo','Tu','We','Th','Fr','Sa','Su']


class Calendar:
    def __init__(self, moonPosition, year, month):
        self.moonPos = moonPosition
        self.year = year
        self.month = month
        
    def _calenderWeeks(self, year, month):
        cal = calendar.Calendar()
        weeks = cal.monthdays2calendar(year, month)
        return weeks

        
    def allDays(self):
        calender_ = []
        week_list = self._calenderWeeks(self.year, self.month)
        
        """The zodiac degree is the sign position + planet degree the - 23 degree to convert it to vedic or tropical"""
        planet_deg_ = (zodiac[self.moonPos['sign']] + int(self.moonPos['deg'])) - 23 #mon = 288
        #print(f"""planet_deg_ from const = {planet_deg_}""")
        
        
        #find it in const_tuple
        for const_range, const_lord, const_name in const_tuple:
            if planet_deg_ in const_range:
                constName = const_name
                break
            
        #print(constName)
        #print(consts_dict[constName])
            
        
        const_name_ = consts_num[constName]
        
        week = 0
        while week <= 4: #4
            date_and_day = 0
            while date_and_day <= 6:#6
                #
                date,day = 0,1
                
                date_ = week_list[week][date_and_day][date]
                day_ = week_list[week][date_and_day][day]
                
                """
                check for empty days in the python calender weeks and we dont whant
                to change the value of the start constallation number.
                """
                if date_ == 0:
                    const_name_ = consts_num[constName]
                    
                else:
                    days_features = {'aup_or_not':consts_dict[const_name_][1],'date':date_,'week':week_days[day_],
                                     'disc':consts_dict[const_name_][0]}
                    
                    
                    #day_html = f"""<div class="card"><div class="{consts_dict[const_name_][1]}"></div>\
                     #           <div class="container"><h2><b>{date_}</b> {week_days[day_]}</h2>\
                      #          <p>{consts_dict[const_name_][0]}</p></div></div>"""
                    
                    calender_.append(days_features)
                #
                    #the is need the check when the 27 const are used since we have 31 or 30 days
                    if const_name_ <= 27:
                        const_name_ += 1
                    if const_name_ >= 27:
                        const_name_ = 1
                
                date_and_day += 1
                
            week += 1
        
        # Joining a list of strings with a comma
        #single_html_calender = "".join(self.calender_)
        
        #lets write it
        #with open(f'./ephemeris/2023_calender/dec.txt', 'a') as calen:
        #    calen.write(single_html_calender)
        
        return calender_#single_html_calender
    
"""
nov = '18GE21'
dec = '21CN45'
moon_point = nov

curr_moon_pos = {'deg':moon_point[0:2],'sign':moon_point[2:4],'min':moon_point[4:6]}
    
calendar_ = Calendar(curr_moon_pos, 2023, 11)
calendars = calendar_.allDays()
print(calendars)
"""










"""
consts_dict_1 = {
    'aswini':'Fortune to get more and more.',
    'bharani':'Will be stolen.',
    'krittika':'Danger from fire.',
    'rohini':'Improves bank position.',
    'mrigasira':'Will be spoild by rat.',
    'ardra':'One loses money.',
    'punarvasu':'There can be no troubles.',
    'pushyami':'Promises wealth.',
    'aslesha':'Will be destroyed.',
    'magha':'Threatens danger to life.',
    'poorvaphalguni':'Threatens trouble from government.',
    'uttaraphalguni':'Increases income and offer good health. = A',
    'hasta':'Gives success.',
    'chitra':'Will have more and more.',
    'swati':'Is good for rich foods.',
    'visakha':'Increases popularity.',
    'anuradha':'For good Friendships and Social Success.',
    'jyeshta':'Shows loses.',
    'moola':'Lose of things in water.',
    'poorvashadha':'Health loss.',
    'uttarashadha':'Sumptuous feast.',
    'sravana':'Threatens eye disease.',
    'dhanista':'Good yeild from field.',
    'satabhisha':'Danger from poison.',
    'poorvabhadra':'Danger from water.',
    'uttarabhadra':'Child Birth.',
    'Revati':'Becomes rich, purchases gems.'
    }
"""
    