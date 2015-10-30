
zodiac_signs = { 
	'aries': ['eager', 'brave', 'impulsive', 'assertive', 'active', 'demanding', 'energetic', 'determined', 'ambitious', 'blunt', 'quirky', 'curious'], 
	'taurus': ['stubborn', 'stable', 'determined', 'stubborn', 'opinionated', 'possessive', 'productive', 'dependable', 'jealous'], 
	'gemini': ['fair', 'generous', 'communicative', 'inquistive', 'adaptable', 'tense', 'nosy', 'quarrelsome'], 
	'cancer': ['practical', 'intuitive', 'nurturing', 'protective', 'helpful','perceptive', 'supportive', 'loving', 'compassionate'], 
	'leo': ['popular', 'pushy', 'confident', 'expressive', 'cheerful', 'courageous', 'bossy', 'arrogant', 'controlling', 'romantic'], 
	'virgo': ['witty', 'fussy', 'thoughtful', 'helpful', 'reliable', 'kind', 'shrewd' , 'analytical', 'expressive', 'dedicated'], 
	'libra': ['adventurous', 'charming', 'creative', 'romantic', 'balanced', 'stylish', 'expressive', 'flighty', 'sociable', 'artistic', 'manipulative'], 
	'scorpio': ['freaky', 'volatile', 'suspicious', 'magnetic', 'sensual', 'intense', 'compulsive', 'social', 'cunning'], 
	'sagittarius': ['loving', 'positive', 'enthusiastic', 'sensual', 'generous', 'stimulating', 'honest', 'frank', 'domineering', 'carefree'], 
	'capricorn': ['hardworking', 'straightforward', 'irresistable', 'witty', 'canny', 'rigid', 'unpredictable', 'fearless', 'responsible', 'talkative', 'energetic'], 
	'aquarius': ['innovative', 'admired', 'distant', 'eccentric', 'sefless', 'idealistic', 'candid', 'cranky', 'elitist', 'dogmatic', 'perfect', 'fair', 'friendly', 'selfess'], 
	'pisces': ['alluring', 'friendly', 'wise', 'inuitive', 'trusting', 'escapist', 'secretive', 'gullible', 'temperamental', 'sensitive'], 
}
def lookup_adjective(adjective):
	# # adjective_dictionary = { 
	# # 'a': 'stimulating', 
	# # 'b': 'romantic', 
	# # 'c': 'determined', 
	# # 'd': 'fair', 
	# # 'e': 'generous', 
	# # 'f': 'intuitive',
	# # }
	# adjective = adjective_dictionary[letter] 

	signs_found = [] 
	for sign, sign_adjectives in zodiac_signs.items():
		if adjective in sign_adjectives:
			signs_found.append(sign)
			print 'added ', sign, 'signs_found is now: ', signs_found 
	return signs_found 

sign_counter = {'aries':0, 'taurus':0, 'gemini':0, 'cancer':0, 'leo':0, 'virgo':0, 'libra':0, 'scorpio':0, 'sagittarius':0, 
'capricorn':0, 'aquarius':0, 'pisces':0}

question_1_sign = None 
answer = raw_input('How do you feel at this moment? (a) analytical or (b) expressive or (c) cranky or (d) energetic or (e) social or (f) communicative\n')
if answer == 'a':
	adjective = 'analytical'
elif answer == 'b':
	adjective = 'expressive'
elif answer == 'c':
	adjective = 'cranky'
elif answer == 'd':
	adjective = 'energetic'
elif answer == 'e':
	adjective = 'social'
elif answer == 'f':
	adjective = 'communicative'

question_1_sign = lookup_adjective(adjective)
for sign in question_1_sign:
	sign_counter[sign] += 1

print 'Question 1 sign:', question_1_sign

question_2_sign = None 
answer = raw_input('How would your friends describe you? (a) friendly or (b) trusting or (c) sociable or (d) stylish or (e) carefree or (f) bossy\n')
if answer == 'a':
	adjective = 'friendly'
elif answer == 'b':
	adjective = 'trusting'
elif answer == 'c':
	adjective = 'sociable'
elif answer == 'd':
	adjective = 'stylish'
elif answer == 'e':
	adjective = 'carefree'
elif answer == 'f':
	adjective = 'bossy'
question_2_sign = lookup_adjective(adjective)
for sign in question_2_sign:
	sign_counter[sign] += 1

print 'Question 2 sign:', question_2_sign

question_3_sign = None 
answer = raw_input('What are you like as a lover? (a) possessive or (b) supportive or (c) magnetic or (d) freaky or (e) romantic or (f) generous\n')
if answer == 'a':
	adjective = 'possessive'
elif answer == 'b':
	adjective = 'supportive'
elif answer == 'c':
	adjective = 'magnetic'
elif answer == 'd':
	adjective = 'freaky'
elif answer == 'e':
	adjective = 'romantic'
elif answer == 'f':
	adjective = 'generous'
question_3_sign = lookup_adjective(adjective)
for sign in question_3_sign:
	sign_counter[sign] += 1

print 'Question 3 sign:', question_3_sign

question_4_sign = None 
answer = raw_input('How would your family describe you? (a) compassionate or (b) perfect or (c) selfless or (d) expressive or (e) generous or (f) helpful\n')
if answer == 'a':
	adjective = 'compassionate'
elif answer == 'b':
	adjective = 'perfect'
elif answer == 'c':
	adjective = 'selfess'
elif answer == 'd':
	adjective = 'expressive'
elif answer == 'e':
	adjective = 'generous'
elif answer == 'f':
	adjective = 'helpful'
question_4_sign = lookup_adjective(adjective)
for sign in question_4_sign:
	sign_counter[sign] += 1

print 'Question 4 sign:', question_4_sign

question_5_sign = None 
answer = raw_input('How would your coworkers describe you? (a) confident or (b) hardworking or (c) cheerful or (d) productive or (e) enthusiastic or (f) responsible\n')
if answer == 'a':
	adjective = 'confident'
elif answer == 'b':
	adjective = 'hardworking'
elif answer == 'c':
	adjective = 'cheerful'
elif answer == 'd':
	adjective = 'productive'
elif answer == 'e':
	adjective = 'enthusiastic'
elif answer == 'f':
	adjective = 'responsible'
question_5_sign = lookup_adjective(adjective)
for sign in question_5_sign:
	sign_counter[sign] += 1

print 'Question 5 sign:', question_5_sign

question_6_sign = None 
answer = raw_input('At your worst - you can be... (a) temperamental or (b) cranky or (c) manipulative or (d) fussy or (e) jealous or (f) stubborn\n')
if answer == 'a':
	adjective = 'temperamental'
elif answer == 'b':
	adjective = 'cranky'
elif answer == 'c':
	adjective = 'manipulative'
elif answer == 'd':
	adjective = 'fussy'
elif answer == 'e':
	adjective = 'jealous'
elif answer == 'f':
	adjective = 'stubborn'
question_6_sign = lookup_adjective(adjective)
for sign in question_6_sign:
	sign_counter[sign] += 1

print 'Question 6 sign:', question_6_sign

question_7_sign = None 
answer = raw_input('Choose a characteristic that you would like to embrace more? (a) determined or (b) innovative or (c) charming or (d) reliable or (e) ambitious or (f) fair\n')
if answer == 'a':
	adjective = 'determined'
elif answer == 'b':
	adjective = 'innovative'
elif answer == 'c':
	adjective = 'charming'
elif answer == 'd':
	adjective = 'reliable'
elif answer == 'e':
	adjective = 'ambitious'
elif answer == 'f':
	adjective = 'fair'
question_7_sign = lookup_adjective(adjective)
for sign in question_7_sign:
	sign_counter[sign] += 1

print 'Question 7 sign:', question_7_sign

print sign_counter


max_count = max(sign_counter.values())

print 'You are one of these: '
for sign in sign_counter:
	if sign_counter[sign] == max_count:
		print sign