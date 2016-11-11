class SchoolSystem():

	__registration = "ABMI"
	__password = "Admin"

	def __init__(self, name=''):
		self.name = name
	def assign_class(self):
		print( "This is your class")
	def assign_department(self):
		print( "This is your department")

class department(SchoolSystem):
	"""The department inherits from the class"""
	def assign_club(self):
		print("This will be your chosen club")
	def assign_class(self):
		print("Would you like to change classes?")

class Student(SchoolSystem):
	"""Student class also inherits from Schoolsystem"""
	def pay_fee(self):
		print("Current fee has been paid")
	def begin_semester(self):
		print("Can begin after paying school fees")
		self.__secret_word
		return
	def __secret_word(self):
		print("Albania")
		return


	def main():
		login =SchoolSystem()
		login.set_password ("Jolly")
		login.begin_semester






		
		
