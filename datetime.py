import datetime
message = " Hey {name} thanks for message us your {total} is in {date}"
names = ["arafat", "aly", "omar", "hosny"]
totals = [234,345,43,34]
date=datetime.datetime.now().strftime('%D/%Y')
def custom_messages(message,names,totals):
    i=0
    for name in names:
        message = message.format(name=name,\
                                 total=totals[i],\
                                 date=datetime.datetime.now().strftime('%D%Y %H:%M:%S'))
        i+=1
        print(message)
custom_messages(message,names,totals)

#================2
import datetime

default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""

def make_messages(names, amounts):
	messages, i = [], 0
	if len(names) == len(amounts):
		for name in names:
			name = name[0].upper() + name[1:].lower()
			date = datetime.datetime.now().strftime('%D/%Y %H:%M:%S')
			total = "%.2f"%(amounts[i])
			i+=1
			new_message = unf_message.format(name=name,
											 date=date,
											 total=total
											 )
			messages.append(new_message)
		return messages
	else:
		print("Your lists is not equal")
