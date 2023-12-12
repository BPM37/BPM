from __future__ import print_function, division
from mon_chart_reading import reading

sign_tuple = ((range(0, 30),'AR'),(range(30, 60), 'TA'),(range(60, 90), 'GE'),
            (range(90, 120), 'CN'), (range(120, 150), 'LE'), (range(150, 180), 'VI'),
            (range(180, 210), 'LI'),(range(210, 240), 'SC'), (range(240, 270), 'SG'),
            (range(270, 300), 'CP'), (range(300, 330), 'AQ'),(range(330, 360), 'PI')
            )

zodiac = {'AR':0, 'TA':30, 'GE':60, 'CN':90, 'LE':120, 'VI':150, 'LI':180, 'SC':210, 'SG':240, 'CP':270,
          'AQ':300, 'PI':330}

zodiac_to_num = {'AR':1, 'TA':2, 'GE':3, 'CN':4, 'LE':5, 'VI':6, 'LI':7, 'SC':8, 'SG':9, 'CP':10,'AQ':11, 'PI':12}

elements = {'AR':'fire', 'TA':'earth', 'GE':'air', 'CN':'water', 'LE':'fire', 'VI':'earth', 'LI':'air', 'SC':'water',
            'SG':'fire', 'CP':'earth','AQ':'air', 'PI':'water'}

#for houses
AR = {'ari':360,'tua':30,'gem':60,'can':90,'leo':120,'vir':150,'lib':180,'sco':210,'sag':240,'cap':270,'aqu':300,'pis':330}
PI = {'pis':360,'ari':30,'tua':60,'gem':90,'can':120,'leo':150,'vir':180,'lib':210,'sco':240,'sag':270,'cap':300,'aqu':330}
TA = {'tua':360,'gem':30,'can':60,'leo':90,'vir':120,'lib':150,'sco':180,'sag':210,'cap':240,'aqu':270,'pis':300,'ari':330}
GE = {'gem':360,'can':30,'leo':60,'vir':90,'lib':120,'sco':150,'sag':180,'cap':210,'aqu':240,'pis':270,'ari':300,'tua':330}
CN = {'can':360,'leo':30,'vir':60,'lib':90,'sco':120,'sag':150,'cap':180,'aqu':210,'pis':240,'ari':270,'tua':300,'gem':330}
LE = {'leo':360,'vir':30,'lib':60,'sco':90,'sag':120,'cap':150,'aqu':180,'pis':210,'ari':240,'tua':270,'gem':300,'can':330}
VI = {'vir':360,'lib':30,'sco':60,'sag':90,'cap':120,'aqu':150,'pis':180,'ari':210,'tua':240,'gem':270,'can':300,'leo':330}
LI = {'lib':360,'sco':30,'sag':60,'cap':90,'aqu':120,'pis':150,'ari':180,'tua':210,'gem':240,'can':270,'leo':300,'vir':330}

SC = {'H1':'SC','H2':'SG','H3':'CP','H4':'AQ','H5':'PI','H6':'AR',
      'H7':'TA','H8':'GE','H9':'CN','H10':'LE','H11':'VI','H12':'LI'}
SG = {'H1':'SG','H2':'CP','H3':'AQ','H4':'PI','H5':'AR','H6':'TA',
      'H7':'GE','H8':'CN','H9':'LE','H10':'VI','H11':'LI','H12':'SC'}
CP = {'H1':'CP','H2':'AQ','H3':'PI','H4':'AR','H5':'TA','H6':'GE',
      'H7':'CN','H8':'LE','H9':'VI','H10':'LI','H11':'SC','H12':'SG'}
AQ = {'H1':'AQ','H2':'PI','H3':'AR','H4':'TA','H5':'GE','H6':'CN',
      'H7':'LE','H8':'VI','H9':'LI','H10':'SC','H11':'SG','H12':'CP'}



class MoonChart:
    '''vars'''
    def __init__(self, natal, transit_):
        self.nat = natal
        self.transit = transit_
        self.namesInnat = ('sun','mon','mec','ven','mas','jup','sat','rah','ket')#'asc',

    def _vedicpt(self, planet):
        """returns the planet vedic degree and sign"""
        
        zodiacDeg = (zodiac[self.nat[planet]['sign']] +  self.nat[planet]['deg']) - 23 #sun (330 + 3) - 23 = 310
       
        
        #get the range of 310
        for range_, name_ in sign_tuple:
            if zodiacDeg in range_:
                vedic_sign = name_ #AQ
                
        #                 310 - 300 = 10
        vedicDeg = zodiacDeg - zodiac[vedic_sign]
        #strenght = planetStrenght[vedic_sign].get(self.nat[planet]['syb'])
        
        
        #                10             aq                       310
        return {'deg':vedicDeg, 'sign':vedic_sign, 'zodiac_deg':zodiacDeg} 

    
    def _drawChart(self, asc='mon'): #planet_name
        
        ascSignName = self._vedicpt(asc)['sign'] #cap
        
        #creat the moon chart from CAP
        #to creat planet chart call for planet sign ie cap here
        natChart = eval(ascSignName)  #a dict of cap          [a_planet_pt] #60
        
        return natChart
    
    def kamajuruma_yoga(self, asc='mon'):
        
        kamaj_read_list = []
        
        
        #fourth and tenth
        with_moon = eval(self._vedicpt(asc)['sign'])['H1']
        fourth = eval(self._vedicpt(asc)['sign'])['H4']
        tenth = eval(self._vedicpt(asc)['sign'])['H10']
        
        kamaj_list = ('with_moon','fourth','tenth')
        
        #is the any planet with the moon?
        for name_kamaj in self.namesInnat:
            for kamaj in kamaj_list:
                
                if self._vedicpt(name_kamaj)['zodiac_deg'] in range(zodiac[eval(kamaj)],zodiac[eval(kamaj)] + 29) \
                   and name_kamaj not in ['asc', 'sun', 'rah', 'ket', 'mon']:
                    
                    kamaj_read_list.append(f'{name_kamaj}_with_moon')

           
        return kamaj_read_list
        
    
    def moon_help__Houses(self, asc='mon'):
        read_list = []
        
        high_tide_list = [] #sixth seventh and eighth
        support_list = []
        resources_list = []
        
        #namesInnat = ('asc','sun','mon','mec','ven','mas','jup','sat','rah','ket')
        source_list = ('support','resources','sixth','seventh','eighth')
        
        
        support = eval(self._vedicpt(asc)['sign'])['H12'] #['AQ',range(30,59)]
        resources = eval(self._vedicpt(asc)['sign'])['H2']
        sixth = eval(self._vedicpt(asc)['sign'])['H6']
        seventh = eval(self._vedicpt(asc)['sign'])['H7']
        eighth = eval(self._vedicpt(asc)['sign'])['H8']
        
        #support
        for namee in self.namesInnat:
            for sources in source_list:
                if self._vedicpt(namee)['zodiac_deg'] in range(zodiac[eval(sources)],zodiac[eval(sources)] + 29) \
                   and namee not in ['asc', 'sun', 'rah', 'ket']:
                    
                    if namee in ['sixth','seventh','eighth']:
                        high_tide_list.append([high_tide, f'high_tide_{namee}'])
                    if namee == 'support':
                        support_list.append([support, f'support_{namee}'])
                    if namee == 'resources':
                        resources_list.append([resources, f'resources_{namee}'])
                        
        if support_list != []:
            read_list.append(reading[support_list[0]],reading[support_list[1]])
            
        if resources_list != []:
            read_list.append(reading[resources_list[0]],reading[resources_list[1]])
        
        if high_tide_list != []:
            read_list.append(reading[high_tide_list[0]],reading[high_tide_list[1]])
                        
        if high_tide_list == [] and support_list == [] and resources_list == []:
            check_planets_with_the_moon = ''
            read_list = self.kamajuruma_yoga()
        
        return read_list
    
    def fifth_and_ninth(self, asc='mon'):
        fifth_and_ninth_listt = []
        
        fifth = eval(self._vedicpt(asc)['sign'])['H5']
        ninth = eval(self._vedicpt(asc)['sign'])['H9']
        
        source_list = ('fifth','ninth')
        
        for namee in self.namesInnat:
            for sources in source_list:
                if self._vedicpt(namee)['zodiac_deg'] in range(zodiac[eval(sources)],zodiac[eval(sources)] + 29):
                    if namee in ['ven','mec','jup']:
                        fifth_and_ninth_listt.append('benefics_fifth_or_ninth')
                    if namee not in ['ven','mec','jup']:
                        fifth_and_ninth_listt.append(f'{namee}_fifth_or_ninth')
                    
        if fifth_and_ninth_listt != []:
            fifth_and_ninth_list = ['fifth_and_ninth_title'] + fifth_and_ninth_listt
                    
        return fifth_and_ninth_list
    
    def moon_sign_element(self, asc='mon'):
        signn = eval(self._vedicpt(asc)['sign'])['H1']
        return elements[signn]
    
    def house_matters(self, house, asc='mon'):
        benefics = ['wax_mon', 'mec', 'ven', 'jup']
        malifics = ['wan_mon', 'mas', 'sat', 'rah', 'ket', 'sun']
        
        any_planet_in_house = []
        planet_in_house_dict = {}
        aspect_dict = []
        
        house_sign = eval(self._vedicpt(asc)['sign'])[f'H{house}'] #AQ 2H
        house_range = range(zodiac[house_sign],zodiac[house_sign] + 29)
        #if occupied by benefics
        
        for planets in self.nat:
            vedic_deg = self._vedicpt(planets)['zodiac_deg']
            if vedic_deg in house_range:
                any_planet_in_house.append(planets)
                for house_occupants in any_planet_in_house:
                    if house_occupants in benefics:
                        print(f'PASSED house_occupants = {house_occupants}')
                    else:
                       print(f'FAILED house_occupants = {house_occupants}')
        
        #aspected by benefics
        moon_house_ranges = ('H1', 'H2', 'H3', 'H4', 'H5', 'H6','H7', 'H8', 'H9', 'H10', 'H11', 'H12')
        
        for planets in self.nat:
            for houses in moon_house_ranges:
                range_ = range(zodiac[eval(self._vedicpt(asc)['sign'])[houses]],\
                               zodiac[eval(self._vedicpt(asc)['sign'])[houses]]+30)
                if self._vedicpt(planets)['zodiac_deg'] in range_:
                    planet_in_house_dict[planets] = eval(self._vedicpt(asc)['sign'])[houses]
                    
        for key, value in planet_in_house_dict.items():
            full_aspects = zodiac_to_num[value] + 6
            if full_aspects > 12:
                full_aspect = full_aspects - 12
            else:
                full_aspect = full_aspects
                
            
            if zodiac_to_num[house_sign] == full_aspect:
                aspect_dict.append(key)
                
            #associate = conj    
            elif zodiac_to_num[house_sign] == value:
                aspect_dict.append(key)
                
            
        def specail_aspects(planet, dicts):
            mas = [3,7]
            sat = [2,9]
            jup,ket,rah = [4,8],[4,8],[4,8]
            
            for key, value in dicts.items():
                if key == planet:
                    planet1_aspectt = zodiac_to_num[value] + eval(planet)[0]
                    planet2_aspectt = zodiac_to_num[value] + eval(planet)[1]
                
            if planet1_aspectt >= 12:
                planet11_aspectt = planet1_aspectt - 12
            else:
                planet11_aspectt = planet1_aspectt
                
            if planet2_aspectt >= 12:
                planet22_aspectt = planet2_aspectt - 12
            else:
                planet22_aspectt = planet2_aspectt
            if zodiac_to_num[house_sign] in [planet11_aspectt, planet22_aspectt]:
                aspect_dict.append(planet)
            #print(zodiac_to_num[house_sign],planet11_aspectt,planet22_aspectt)    
        
        #for stars in ('mas','jup','sat','rah','ket'):
        #    specail_aspects(stars, planet_in_house_dict)        
        print(aspect_dict)
        
                       

    def __str__(self):
        return """returns the planet vedic degree and sign"""
    






    
nat = { 'asc':{'deg':16,'sign':'SG','min':15,'syb':"A"},
        'sun':{'deg':3,'sign':'PI','min':3,'syb':"sun"},
        'mon':{'deg':11,'sign':'AQ','min':3,'syb':"mon"},
        'mec':{'deg':6,'sign':'AQ','min':40,'syb':"merc"},
        #'mec':{'deg':24,'sign':'LE','min':40,'syb':"merc"},
        'ven':{'deg':25,'sign':'CP','min':41,'syb':"ven"},
        'mas':{'deg':19,'sign':'LI','min':10,'syb':"mars"},
        'jup':{'deg':10,'sign':'SC','min':19,'syb':"jup"},
        'sat':{'deg':21,'sign':'LI','min':50,'syb':"sat"},
        'rah':{'deg':21,'sign':'CN','min':56,'syb':"rahu"},
        'ket':{'deg':21,'sign':'CP','min':56,'syb':"ketu"},
        #'p_fort':{'deg':8,'sign':'CP','min':15,'syb':"p_fort"},
        }

transit = {
        'sat':{'deg':1, 'sign':12, 'min':29, 'syb':'tsat'} #to the materal world measurement
        }

moon_chart = MoonChart(nat, transit)
moon_chart_secret = moon_chart.moon_help__Houses()
personality = moon_chart.moon_sign_element()
house_effect = moon_chart.house_matters(3,asc='asc')
print(moon_chart_secret,personality,house_effect)
