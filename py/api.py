from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

#our models
from num_scripts.dateofbirth import DateOfBirth
from num_scripts.read_nums import oracle_read



bp = Blueprint('api', __name__)

@bp.route('/res', methods = ['POST'])
@cross_origin()
def res():

    posted_data = request.get_json()

    #save the data
    with open('/home/bpm/u/users.txt', 'a') as f:
        f.write(f'{posted_data} \n')

    #data for our oracle
    name, dob = posted_data['name'], posted_data['dob']

    #create in balace oracle - our classes
    oracle = DateOfBirth(dob, 'forNow')

    #just the personal year
    dataforpyear = {'approach':oracle_read[oracle.personalYearNum()['core']]['APPROACH'],
                    'advice':oracle_read[oracle.personalYearNum()['core']]['ADVICE']

                    }

    dataforpmonth = {
                        'approach':oracle_read[oracle.personalMonthNum()['core']]['ADVICE'],
                        'advice':'',

                    }

    datafortro = {
                        'approach':'Oracle is busy will be ready in 24H',
                        'advice':'',

                    }

    if posted_data['reqFor'] == 'Pyear':

        return jsonify(dataforpyear)

    elif posted_data['reqFor'] == 'Pmonth':
         return jsonify(dataforpmonth)

    else:
        return jsonify(datafortro)



