import os
import request


class Commit():
	def onlyGitCommitAll(self):
		self.status=os.system("git status")
		if self.status==0:
			os.system("git add .")
			os.system("git commit -m 'ok'")
			os.system("git push")
			return "Operation complete"
		return "Problem"
	def checkConnection(self):
		try:
			
		except requests.ConnectionError:
			return False
