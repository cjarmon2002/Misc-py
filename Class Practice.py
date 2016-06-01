class car(object):
	def __init__(self, make, model, style):
		self.make = make
		self.model = model
		self.style = style

	def description(self):
		print "Your car is a %s %s and is concidered a %s." % (self.make,
			self.model, self.style)

focus = car('Ford', 'Focus', 'sedan')
camry = car('Toyota', 'Camry', 'sedan')
F150 = car('Ford', 'F150', 'Truck')

focus.description()
camry.description()
F150.description()

