import datetime

class MessageUser():
	user_details = []
	messages = []
	base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""

	def add_user(self, name, amount, email=None):
		name = name[0].upper() + name[1:].lower()
		date = datetime.datetime.now().strftime('%D/%Y %H:%M:%S')
		detail ={
			"name": name,
			"amount": "%.2f" %(amount),
			"date": date,
		}
		if email != None:
			detail["email"] = email
		self.user_details.append(detail)

	def get_details(self):
		if len(self.user_details) > 0:
			return self.user_details
		return ["not details"]
	def make_messages(self):
		if len(self.user_details) > 0:
			for detail in self.get_details():
				name = detail["name"]
				amount = detail["amount"]
				date = detail["date"]
				message = self.base_message
				new_msg = message.format(
					name=name,
					date=date,
					total=amount,
					)
				self.messages.append(new_msg)
			return self.messages
		return ["no users"]

obj = MessageUser()
obj.add_user("Araaft",333,"rkle@lice.om")
obj.add_user("Araaft",333,"rkle@lice.om")
obj.add_user("Araaft",333,"rkle@lice.om")
obj.add_user("Araaft",333,"rkle@lice.om")
obj.add_user("mohaemd",58)
obj.get_details()
obj.make_messages()