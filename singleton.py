# only one instance
#gloaal variable in an oop way

#borg design pattern

class Borg:
	"""Borg class making class attributes global"""
	_shared_state = {} #Attribute dictionary

class Singleton(Borg): #inherits from the Borg class
	""" This class now shares all its attributes among its various instances """
	#This essentially makes the singleton objects an object oriented global variable

	def __init__(self, word_dict):

		self.__dict__ = self._shared_state
		#Update the attribute dictionary by insering a new key value pair
		self._shared_state.update(word_dict)

	def __str__(self):
		# returns the attribute dictionary for printing
		return str(self._shared_state)

#let's create a singleton object and add our first acronym =
x = Singleton({'HTTP ' : 'Hper Text Tranfer Protocol'})
# print the object
print(x)

#let's create a singleton object and addind another acronym =
y = Singleton({'lalal' : ' a song'})
print(y)