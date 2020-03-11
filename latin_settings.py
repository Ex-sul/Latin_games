import json

settings_json = json.dumps([
    {'type': 'title',
     'title': 'Settings'},
    {'type': 'options',
     'title': 'Number of Words to Display',
     'desc': 'Choose how many words to display.',
     'key': 'Number of Words to Display',
     'section': 'General Settings',
     'options': ['One', 'Two', 'Three']},
    {'type': 'title',
     'title': 'First Word'},
    {'type': 'string',
     'title': 'Regular Verb One',
     'desc': 'Example: laudo, laudāre, laudavi, laudatum, to praise',
     'section': 'General Settings',
     'key': 'firstword'},
    {'type': 'title',
     'title': 'Second Word'},
    {'type': 'title',
     'title': 'Third Word'},
])