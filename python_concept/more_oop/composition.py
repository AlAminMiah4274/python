class Engine:

	def __init__(self):
		pass

	def start(self):
		return "Engine started"


class Driver:

	def __init__(self):
		pass


class Car(Engine):

	def __init__(self):
		self.engine = Engine()
		self.driver = Driver()

	def start(self):
		self.engine.start()