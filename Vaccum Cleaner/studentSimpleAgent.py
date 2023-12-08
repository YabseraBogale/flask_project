class SimpleStudentAgent():
	def __init__(self):
		self.Id=["RCD/3093/2013","RCD/3091/2013","RCD/3087/2013","RCD/3053/2013","RCD/3120/2013"]
		self.Student="out"
	def Preciver(self,ID):
		if self.ID.find(ID)!=-1:
			self.Student="in"
		else:
			self.Student="out"
	def Act(self):
		return self.Student



