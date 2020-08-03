class Patient:

	patient_id = 1

	def __init__(self, name, age, disease):
		self.name = name
		self.age = age
		self.disease = disease
		self.id = Patient.patient_id
		Patient.patient_id += 1

	def display_patient_data(self):
		print("Patient id:", self.id)
		print("Name:", self.name)
		print("Age:", self.age)
		print("Disease:", self.disease) 
