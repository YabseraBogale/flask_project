class SimpleStudentAgent():
	def __init__(self):
		self.Id=["RCD/3093/2013","RCD/3091/2013","RCD/3087/2013","RCD/3053/2013","RCD/3120/2013"]
		self.Student="out"
	def Preciver(self,ID):
		if self.Id.count(ID)==1:
			self.Student="in"
		else:
			self.Student="out"
	def Act(self):
		return self.Student



Agent=SimpleStudentAgent()

Agent.Preciver("RCD/3093/2013")
Action=Agent.Act()
print(Action)
Agent.Preciver("RCD/5513/2013")
Action=Agent.Act()
print(Action)
