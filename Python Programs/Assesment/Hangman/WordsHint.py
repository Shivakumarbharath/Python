sports = ('arena', 'athletic', 'backboard', 'backhand', 'batter (baseball)', 'baseball',
          'basketball', 'bench', 'catcher', 'champion', 'championship', 'coach', 'competitive',
          'defense', 'doubles', 'dribble', 'dugout', 'fan',
          'field goal', 'finish line', 'football', 'forehand', 'goalkeeper', 'goalpost')
air_Travel = (
'aisle', 'arrival', 'baggage', 'board', 'bulkhead', 'carry-on', 'coach', 'cockpit', 'connection', 'crew', 'customs',
'declare',
'departure', 'duty-free',
'gate', 'itinerary', 'jet engine', 'jet lag', 'jumbo jet', 'landing', 'lavatory', 'luggage', 'one-way', 'overbook',
'oxygen mask')
environment = ('aquifer', 'atmosphere', 'biodegradable', 'biodiversity', 'carbon dioxide', 'carbon monoxide',
               'carcinogen', 'climate', 'coal', 'compost (noun)', 'compost (verb)', 'conservation', 'conservationist',
               'contaminant', 'contamination', 'deforestation', 'disposable', 'diversity', 'ecology', 'ecosystem',
               'emission',
               'endangered', 'energy', 'environment', 'environmentalist', 'erosion', 'extinct', 'extinction',
               'fossil fuel', 'geothermal')

family = ('mother', 'mom', 'father', 'dad', 'parent', 'children', 'son', 'daughter', 'sister', 'brother',
          'grandmother', 'grandfather', 'grandparent', 'grandson', 'granddaughter', 'grandchild', 'aunt',
          'uncle', 'niece', 'nephew', 'cousin', 'husband', 'wife', 'sister-in-law', 'brother-in-law', 'mother-in-law',
          'father-in-law', 'partner')
jobs_professions = ('accountant', 'actor', 'actress', 'architect', 'artist', 'attorney', 'banker', 'bartender',
                    'barber', 'bookkeeper', 'builder', 'businessman', 'businesswoman',
                    'businessperson', 'butcher', 'carpenter', 'cashier', 'chef', 'coach',
                    'dentist', 'designer', 'developer', 'dietician', 'doctor', 'economist',
                    'editor', 'electrician', 'engineer')

law = (
'arrest', 'accuse', 'acquit', 'adjourn', 'adoption', 'alibi', 'alimony', 'appeal', 'appeal', 'attorney', 'bankrupt',
'bribe',
'brief', 'case', 'common-law', 'contract', 'copyright' 'court', 'criminal (adjective)', 'custody', 'damages',
'death sentence', 'defend')

emotions = (
'acceptance', 'admiration', 'affection', 'aggravation', 'anger', 'anguish', 'anxiety', 'attraction', 'boredom',
'caution',
'certainty', 'compassion', 'confidence', 'confusion', 'contentment', 'courage', 'curiosity', 'defeat', 'defiance',
'delight',
'dependence', 'depression', 'desire', 'disappointment', 'dislike', 'dismay', 'distress', 'embarrassment', 'enthusiasm',
'envy')

body_parts = (
'ankle', 'arch', 'arm', 'armpit', 'beard', 'breast', 'calf', 'cheek', 'chest', 'chin', 'earlobe', 'elbow', 'eyebrow',
'eyelash', 'eyelid', 'face', 'finger', 'forearm', 'forehead', 'gum', 'heel', 'hip', 'index finger', 'jaw', 'knee',
'knuckle',
'leg', 'lip', 'mouth', 'mustache')

non_count_nouns = (
'advice', 'agriculture', 'air', 'anger', 'attention', 'chaos', 'clothing', 'courage', 'dirt', 'equipment', 'fun',
'furniture',
'garbage', 'homework', 'housework', 'information', 'jewelry', 'luck', 'luggage', 'mail', 'news', 'patience',
'permission',
'pollution', 'progress', 'research', 'scenery', 'slang', 'smoke', 'soccer')

health = ('ache', 'allergy', 'antihistamine', 'appetite', 'aspirin', 'bandage', 'bandage', 'blood', 'bone', 'broken',
          'bronchitis',
          'bruise', 'bruise', 'cast', 'clinic', 'cold', 'contagious', 'cough', 'crutch', 'cut', 'decongestant',
          'diarrhea', 'dizzy',
          'fever', 'first aid', 'flu', 'headache', 'hives', 'indigestion', 'infection')

college = ('campus', 'community college', 'course', 'credit', 'degree', 'dorm', 'enroll', 'exam', 'faculty', 'fail',
           'financial aid',
           'fraternity', 'gpa', 'graduate', 'graduate', 'instructor', 'lecture', 'major', "master's degree",
           'matriculate', 'notebook', 'notes',
           'pass', 'phd', 'postgraduate', 'prerequisite', 'professor', 'quiz', 'goa')

Catagory = [sports, air_Travel, environment, family, jobs_professions, law, emotions, body_parts, non_count_nouns,
            health, college]

Catagory_text = {sports: 'Sports', air_Travel: "Air Travel", environment: "Environment", family: "Family",
                 jobs_professions: "Jobs or Professions", law: "Law", emotions: "Emotions", body_parts: "Body Parts",
                 non_count_nouns: "Non-Count-Nouns",
                 health: "Health", college: "College Life"}

'''
while True:
    k=input()
    if k:

        college.append(k.lower())
    else:break

print(college)
#more words can be added by
#https://learnersdictionary.com/3000-words

'''
