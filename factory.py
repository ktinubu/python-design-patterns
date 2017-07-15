"""
FACTORY:

	Problem:
		Uncertainties in types of bjects
		decisions to be made at runtime regarding what classes to use

"""

class Dog:

	""" A simple Dog Class"""

	def __init__(self, name):
		self.name = name

	def speak(self):
		return 'woof!'

class Cat:

	""" A simple Dog Class"""

	def __init__(self, name):
		self.name = name

	def speak(self):
		return 'meow!'

def get_pet(pet='dog'):

	""" The factory method."""
	pets = {'dog' : Dog('Hope'),
			'cat': Cat('Peace')}

	return pets[pet]

d = get_pet('dog')
print(d.speak())

c = get_pet('cat')
print(c.speak())

