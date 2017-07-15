"""
Abstract FACTORY:

	Problem:
		Uncertainties in types of bjects
		decisions to be made at runtime regarding what classes to use

"""

class Dog:

	def speak(self):
		return "Woof!"

	def __str__(self):
		return 'Dog'

class DogFactory:
	"""Concrete Factory."""

	def get_pet(self):
		"""returns a Dog object"""
		return Dog()

	def get_food(self):
		"""returns a Dog food object"""
		return "Dog Food!"

class Cat:
	def speak(self):
		return 'meow'

	def __str__(self):
		return 'Cat'

class CatFactory:
	"""Concrete Factory."""

	def get_pet(self):
		"""returns a Dog object"""
		return Cat()

	def get_food(self):
		"""returns a Dog food object"""
		return "Cat Food!"


class PetStore:
	""" pet_factory is our Abstract Factory """

	def __init__(self, pet_factory=None):
		""" pet factory is our Abstract Factory """
		self._pet_factory = pet_factory

	def show_pet(self):

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our Pet is '{}!".format(pet))
		print("our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))

#Create a Concrete Factory
factory = CatFactory()

#create a pet store housing our Abstract Factory
shop = PetStore(factory)

#invoke the utility method to show the details of our pet
shop.show_pet()





























