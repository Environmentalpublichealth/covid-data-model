'''
Constants to use for a build. In a separate file to avoid
auto-importing a dataset when we don't necessarily need to.
'''

from datetime import datetime, timedelta, date


def get_interventions(start_date=datetime.now().date()):
    return [
        None,  # No Intervention
        {  # 2.3
            start_date: 2.3,
            start_date + timedelta(days=140) : None
        },
        {  # Social Distancing
            start_date: 1.7,
            start_date + timedelta(days=140) : None
        },
        {  #scenario 1
            start_date: (1 - .575 * .08 * .05) * 1.7,
            start_date + timedelta(days=140) : None
        },
        {  #scenario 2
            start_date: (1 - .575 * 1 * 1) * 1.7,
            start_date + timedelta(days=140) : None
        },
        {  #scenario 3
            start_date: (1 - .575 * .54 * .525) * 1.7,
            start_date + timedelta(days=140) : None
        },
        {  #scenario 4
            start_date: (1 - .4 * .08 * .05) * 1.7,
            start_date + timedelta(days=140) : None
        },
        {  #scenario 5
            start_date: (1 - .75 * 1 * 1) * 1.7,
            start_date + timedelta(days=140) : None
        },
    ]


OUTPUT_DIR = 'results/test'

# Dict to transform longhand state names to abbreviations
US_STATE_ABBREV = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'United States All': 'USa'
}
