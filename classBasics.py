class Animal():
	name = "jon"
	noise = "Grunt"
	color = "brown"
	normal_age = "20"
	size = "large"
	hair = "covers body"
	def get_color(self, abc="other_kwarg"):
		return self.color + " " + abc
	def make_noise(self):
		return self.noise

class Dog(Animal):
	name = "fahd"
	size = "small"
	color = "black"
	@property
	def get_size(self):
		return self.size + " " + arg