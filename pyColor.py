
""" Use this module to simply print to the command line in color
	For python 2.7

	Usage:
	print pyColor.YELLOW + "Warning: No active frommets remain. Continue?" 
      + pyColor.ENDC
"""

class color:
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	ENDC = '\033[0m'

	def Disable(self):
		self.PURPLE = ''
		self.BLUE = ''
		self.GREEN = ''
		self.YELLOW = ''
		self.RED = ''
		self.ENDC = ''