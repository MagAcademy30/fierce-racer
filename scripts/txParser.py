# txParser 0.2
# by MG30

class txParser:
	def __init__(self):
		self.data = []
		self.path = None

	def read(self, pathtofile):
		self.path = pathtofile
		file = open(self.path, "r")
		read = file.read()
		file.close()

		self.data = read.split("\n")
	
	def update(self):
		needwrite = ""
		for i in self.data:
			needwrite += str(i) + "\n"

		file = open(self.path, "w")
		file.write(needwrite)
		file.close()

	def get(self, line):
		return self.data[line]

	def set(self, line, what):
		self.data[line] = what

	def getAll(self):
		return self.data

	def setAll(self, what):
		self.data = what