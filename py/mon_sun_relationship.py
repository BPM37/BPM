from __future__ import print_function, division


west_to_vedic = {0:[23 ,0],1:[24,0],2:[25,0],3:[26,0],4:[27,0],5:[28,0],6:[29,0],7:[14,-1],8:[15,-1],9:[16,-1],10:[17,-1],
                 11:[18,-1],12:[19,-1],13:[20,-1],14:[21,-1],15:[22,-1],16:[23,-1],17:[24,-1],18:[25,-1],19:[26,-1],20:[27,-1],
                 21:[28,-1],22:[29,-1],23:[0,0],24:[1,0],25:[2,0],26:[3,0],27:[4,0],28:[5,0],29:[6,0]}

sign_tuple = ((range(0, 30),'AR'),(range(30, 60), 'TA'),(range(60, 90), 'GE'),
            (range(90, 120), 'CN'), (range(120, 150), 'LE'), (range(150, 180), 'VI'),
            (range(180, 210), 'LI'),(range(210, 240), 'SC'), (range(240, 270), 'SG'),
            (range(270, 300), 'CP'), (range(300, 330), 'AQ'),(range(330, 360), 'PI')
            )

zodiac = {'AR':0, 'TA':30, 'GE':60, 'CN':90, 'LE':120, 'VI':150, 'LI':180, 'SC':210, 'SG':240, 'CP':270,
          'AQ':300, 'PI':330}

#https://archive.org/details/lightonlife00hart/page/62/mode/1up?view=theater
planetStrenght = {'AR':{'sat':'weak','ven':'weak','jup':'strong','mas':'strong','sun':'exalted'},
                  'TA':{'mas':'weak','jup':'strong','rah':'weak','ket':'weak','ven':'slightly strong','mon':'exalted'},
                  'GE':{'mec':'strong','jup':'weak','sat':'strong','rah':'exalted'},
                  'CN':{'sat':'weak','mec':'strong','mas':'weak','mon':'strong','jup':'exalted'},
                  'LE':{'sat':'weak','mas':'strong','sun':'strong'},
                  'VI':{'jup':'weak','sat':'strong','ven':'weak', 'mec':'though exalted but slightly strong'},
                  'LI':{'mas':'weak','jup':'strong','sun':'weak','ven':'strong','sat':'exalted'},
                  'SC':{'ven':'weak','sun':'strong','mon':'weak','ket':'exalted','rah':'exalted','mas':'slightly strong'},
                  'SG':{'mec':'weak','ven':'strong','ket':'exalted','jup':'strong'},
                  'CP':{'mon':'weak','mec':'strong','jup':'weak','sat':'slightly strong','mas':'exalted'},
                  'AQ':{'sun':'weak','sat':'strong'},
                  'PI':{'mec':'weak','ven':'exalted','jup':'slightly strong'}
                  }
potentialStrenght = {'exalted':'87.5 - 100', 'trinal':'75 - 87.5', 'positive':'62.5 - 75','negative':'50 - 62.5',
                     'F':'37.5 - 50','N':'25 - 37.5','E':'12.5 - 25','weak':'0 - 12.5'}

planetRelationship = {'sun':{'mon':'Friend','jup':'Friend','mas':'Friend','mec':'Neutral','ven':'Enemy','sat':'Enemy'},
                  'mon':{'sun':'Friend','mec':'Friend','ven':'Neutral','mas':'Neutral','jup':'Neutral','sat':'Neutral'},
                  'mec':{'sun':'Friend','ven':'Friend','mas':'Neutral','jup':'Neutral','sat':'Neutral','mon':'Enemy'},
                  'ven':{'mec':'Friend','sat':'Friend','mas':'Neutral','jup':'Neutral','sun':'Enemy','mon':'Enemy'},
                  'mas':{'sun':'Friend','mon':'Friend','jup':'Friend','ven':'Neutral','mec':'Enemy','sat':'Neutral'},
                  'jup':{'sun':'Friend','mon':'Friend','mas':'Friend','sat':'Neutral','ven':'Enemy','mec':'Enemy'},
                  'sat':{'mec':'Friend','ven':'Friend','jup':'Neutral','sun':'Enemy','mon':'Enemy','mas':'Enemy'}
                  }
rulership = {'AR':'mas', 'TA':'ven', 'GE':'mec', 'CN':'mon', 'LE':'sun', 'VI':'mec', 'LI':'ven', 'SC':'mas',
             'SG':'jup', 'CP':'sat', 'AQ':'sat', 'PI':'jup'}


class VediChart:
    '''vars'''
    def __init__(self, natal, transit_):
        self.nat = natal
        self.transit = transit_

    def _vedicpt(self, planet):
        """returns the planet vedic degree and sign"""
        #print(zodiac[self.nat[planet]['sign']])
        zodiacDeg = abs((zodiac[self.nat[planet]['sign']] +  self.nat[planet]['deg']) - 23) #sun (330 + 3) - 23 = 310
        
        #get the range of 310
        for range_, name_ in sign_tuple:
            if zodiacDeg in range_:
                vedic_sign = name_ #AQ
                
        #                 310 - 300 = 10
        vedicDeg = zodiacDeg - zodiac[vedic_sign]
        strenght = planetStrenght[vedic_sign].get(self.nat[planet]['syb'])
        
        
        #                10             aq                       310
        return {'deg':vedicDeg, 'sign':vedic_sign, 'zodiac_deg':zodiacDeg, 'strenght':strenght} 

    def enemy_or_friend(self, planet):
        planet_sign = self._vedicpt(planet)['sign'] #CP
        ruler_planet_sign = rulership[planet_sign] #sat
        enemy_or_friend_ruler_sign = planetRelationship[ruler_planet_sign].get(planet) #E
        
        return enemy_or_friend_ruler_sign
    
    def planetState(self, planet):
       
        planet_signn = self._vedicpt(planet)['sign'] #CP
        odd_sign_range = (
                            (range(zodiac[planet_signn], zodiac[planet_signn] + 7),'child'),
                            (range(zodiac[planet_signn] + 7, zodiac[planet_signn] + 14),'youth'),
                            (range(zodiac[planet_signn] + 14, zodiac[planet_signn] + 21),'young'),
                            (range(zodiac[planet_signn] + 21, zodiac[planet_signn] + 28),'aged'),
                            (range(zodiac[planet_signn] + 28, zodiac[planet_signn] + 35),'dead')
                            )
        
        even_sign_range = (
                            (range(zodiac[planet_signn] + 28, zodiac[planet_signn] + 35),'dead'),
                            (range(zodiac[planet_signn] + 21, zodiac[planet_signn] + 28),'aged'),
                            (range(zodiac[planet_signn] + 14, zodiac[planet_signn] + 21),'young'),
                            (range(zodiac[planet_signn] + 7, zodiac[planet_signn] + 14),'youth'),
                            (range(zodiac[planet_signn], zodiac[planet_signn] + 7),'child')
                            )
        
        if planet_signn in ['AR','GE','LE','LI','SG','AQ']:
            for range_, state in odd_sign_range:
                if self._vedicpt(planet)['zodiac_deg'] in range_:
                    planet_statee = state
                    break
    
        if planet_signn in ['TA','CN','VI','SC','CP','PI']:
            for range_, state in even_sign_range:
                if self._vedicpt(planet)['zodiac_deg'] in range_:
                    planet_statee = state
                    break
        
        return planet_statee
    
    def planet_strenght(self, planet):
        #exaltation and dibilitation
        pass
    
    def planet_details(self):
        star_list = []
        for star in ('sun','mon','mec','ven','mas','jup','sat','rah','ket'):
            sign = self._vedicpt(star)['sign']
            starStrent = self._vedicpt(star)['strenght']
            starCamp = self.enemy_or_friend(star)
            starState = self.planetState(star)
            #star_list.append(f"The {star} is {starStrent} in strength, in {starCamp}'s camp and is {starState}.")
            star_list.append({'planet':star,'strenght':starStrent,'camp':starCamp,'state':starState,'sign':sign})
        return star_list


    def __str__(self):
        return """returns the planet vedic degree and sign"""
    






"""   
nat = { #'asc':{'deg':16,'sign':'SG','min':15,'syb':"A"},
        'sun':{'deg':3,'sign':'PI','min':3,'syb':"sun"},
        'mon':{'deg':11,'sign':'AQ','min':3,'syb':"mon"},
        #'mon':{'deg':11,'sign':'GE','min':3,'syb':"mon"},
        'mec':{'deg':6,'sign':'AQ','min':40,'syb':"mec"},
        #'mec':{'deg':24,'sign':'LE','min':40,'syb':"merc"},
        'ven':{'deg':25,'sign':'CP','min':41,'syb':"ven"},
        'mas':{'deg':19,'sign':'LI','min':10,'syb':"mas"},
        'jup':{'deg':10,'sign':'SC','min':19,'syb':"jup"},
        'sat':{'deg':21,'sign':'LI','min':50,'syb':"sat"},
        'rah':{'deg':21,'sign':'CN','min':56,'syb':"rah"},
        'ket':{'deg':21,'sign':'CP','min':56,'syb':"ket"},
        
        }
"""
"""
#felix
nat = {'sun': {'deg': 0, 'sign': 'AR', 'min': 19, 'syb': 'sun'}, 'mon': {'deg': 24, 'sign': 'PI', 'min': 50, 'syb': 'mon'},
       'mec': {'deg': 17, 'sign': 'AR', 'min': 43, 'syb': 'mec'}, 'ven': {'deg': 21, 'sign': 'AR', 'min': 13, 'syb': 'ven'},
       'mas': {'deg': 4, 'sign': 'TA', 'min': 12, 'syb': 'mas'}, 'jup': {'deg': 8, 'sign': 'AQ', 'min': 59, 'syb': 'jup'},
       'sat': {'deg': 27, 'sign': 'SC', 'min': 58, 'syb': 'sat'}, 'rah': {'deg': 17, 'sign': 'SG', 'min': 59, 'syb': 'rah'},
       'ket': {'deg': 3, 'sign': 'CP', 'min': 33, 'syb': 'ket'}}
"""
"""
#noxis
nat = {'sun': {'deg': 27, 'sign': 'VI', 'min': 6, 'syb': 'sun'}, 'mon': {'deg': 2, 'sign': 'SC', 'min': 44, 'syb': 'mon'},
       'mec': {'deg': 23, 'sign': 'LI', 'min': 28, 'syb': 'mec'}, 'ven': {'deg': 28, 'sign': 'LE', 'min': 40, 'syb': 'ven'},
       'mas': {'deg': 6, 'sign': 'CP', 'min': 5, 'syb': 'mas'}, 'jup': {'deg': 12, 'sign': 'CN', 'min': 45, 'syb': 'jup'},
       'sat': {'deg': 14, 'sign': 'GE', 'min': 55, 'syb': 'sat'}, 'rah': {'deg': 21, 'sign': 'AQ', 'min': 34, 'syb': 'rah'},
       'ket': {'deg': 6, 'sign': 'AQ', 'min': 12, 'syb': 'ket'}}
"""
"""
#NK
nat = {'sun': {'deg': 6, 'sign': 'TA', 'min': 1, 'syb': 'sun'}, 'mon': {'deg': 17, 'sign': 'AQ', 'min': 55, 'syb': 'mon'},
       'mec': {'deg': 8, 'sign': 'AR', 'min': 59, 'syb': 'mec'}, 'ven': {'deg': 23, 'sign': 'AR', 'min': 2, 'syb': 'ven'},
       'mas': {'deg': 22, 'sign': 'PI', 'min': 23, 'syb': 'mas'}, 'jup': {'deg': 4, 'sign': 'VI', 'min': 40, 'syb': 'jup'},
       'sat': {'deg': 17, 'sign': 'AQ', 'min': 38, 'syb': 'sat'}, 'rah': {'deg': 18, 'sign': 'CP', 'min': 0, 'syb': 'rah'},
       'ket': {'deg': 18, 'sign': 'CP', 'min': 57, 'syb': 'ket'}}
"""
#bet
bet = {'sun': {'deg': 13, 'sign': 'AQ', 'min': 6, 'syb': 'sun'}, 'mon': {'deg': 23, 'sign': 'AQ', 'min': 24, 'syb': 'mon'},
       'mec': {'deg': 24, 'sign': 'CP', 'min': 41, 'syb': 'mec'}, 'ven': {'deg': 11, 'sign': 'CP', 'min': 20, 'syb': 'ven'},
       'mas': {'deg': 6, 'sign': 'CP', 'min': 10, 'syb': 'mas'}, 'jup': {'deg': 7, 'sign': 'PI', 'min': 27, 'syb': 'jup'},
       'sat': {'deg': 15, 'sign': 'AQ', 'min': 36, 'syb': 'sat'}, 'rah': {'deg': 10, 'sign': 'TA', 'min': 54, 'syb': 'rah'},
       'ket': {'deg': 21, 'sign': 'PI', 'min': 28, 'syb': 'ket'}}

transit = {
        'sat':{'deg':1, 'sign':12, 'min':29, 'syb':'tsat'} #to the materal world measurement
        }

chart = VediChart(bet, transit)
star_details = chart.planet_details()
print(star_details)


