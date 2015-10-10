# -*- coding: utf-8 -*-
import sys
import random

def get_practice_key():
	keys = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
	accidentals = ("#", "b","")
	return random.choice(keys) + random.choice(accidentals) 

def get_traditional_mode():
	modes = {
				'Ionian':	{ 'example': "C  D  E  F  G  A  B  C" , "info": 'all major and perfect intervals' },
				"Dorian":	{ 'example': "C  D  Eb F  G  A  Bb C",  'info': 	'minor 3rd and 7th'},
				"Phrygian":	{ 'example': "C  Db Eb F  G  Ab Bb C",	'info': 'minor 2nd, 3rd, 6th, 7th'},
				"Lydian":	{ 'example': "C  D  E  F# G  A  B  C",	'info': 'augmented 4th'	},
				"Mixolydian":{ 'example': "C  D  E  F  G  A  Bb C",	'info': 'minor 7th'},
				"Aeolian":	{ 'example': "C  D  Eb F  G  Ab Bb C",	'info': 'minor 3rd, 6th, 7th'},
				"Locrian":	{ 'example': "C  Db Eb F  Gb Ab Bb C",	'info': 'minor 2nd, 3rd, 6th, 7th, diminished 5th'}
			}
	choice = random.choice(modes.keys())
	return choice, modes[choice]

if __name__ == '__main__':

	print "Random major/minor scale in the key of %s" % (get_practice_key())
	print "Random Mode to practice: %s " %(str(get_traditional_mode())) 
	print "Why not try in the key of %s " % (get_practice_key())