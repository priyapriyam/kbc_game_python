Question = ["(1)who is 	the co-founder of navgurukul","(2)who is the facility inchaage of navgurukul","(3)How many grils in there navgurukul","(4)what is the meaning of navgurukul"]

first_options = ["(1)Abhshek","(1)vandna","(1)70","(1)New year"]
secound_options = ["(2)Amar","(2)Aanu","(2)60","(2)Nav Gurukul"]
third_options = ["(3)kiran","(3)komal","(3)54","(3)New house"]
frouth_options = ["(4)sanjay","(4)Nilam","(4)20","(4)Navnirmit"]
all_options = ["first_options","secound_options","third_options","frouth_options"]
ans_key = [1,2,3,4]
help_line = [["(1)Abhshek","(2)Amar"],["(1)vandna","(2)Aanu"],["(1)54","(2)20"],["(1)New house","(2)Navnirmit"]]
help_line_key = [1,2,1,2]
i = 0
while i < len(Question):
	print Question[i]
	print len(Question[i])
	print first_options[i]
	print secound_options[i]
	print third_options[i]
	print frouth_options[i]
	user_input =input("Enter the answer no. or can you help of help_line so put 50-50")
	if ans_key[i] == user_input:
		print "your answer right"
		i = i + 1
	elif user_input == 5050:
		print Question[i]
		print help_line[i]
		user_input1 =int(raw_input("Enter the answer no."))	
		if user_input1 == help_line_key[i]:
			print "you win!"
		else:
			print "you lose!"
			break
	i = i + 1