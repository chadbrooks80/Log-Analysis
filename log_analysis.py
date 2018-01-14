import psycopg2
from queries import popular_articles, popular_authors, errors


#This is the main Menu that pops up for someone to make a selection.  
#after they make a selection it will display the results and bring this
#menu up again 
def make_choice():
	print("\nWelcome to the Log Analysis Reporting Tool!\n")
	print('''Please Select an Option:   
   1. Find out the 3 most popular articles of all time
   2. Find out who the most popular article authors of all time are.
   3. Find out which days had more than 1% of requests lead to error

If you would like to quit this application, then please type "quit"

Enter your Selection:
	''')


#this dictionary is used for referencing which option they choose from the string
#displayed above.  
user_selection = {
	"1.": popular_articles,
	"1" : popular_articles,
	"2." : popular_authors,
	"2" : popular_authors,
	"3." : errors,
	"3" : errors,
	"quit" : "quit"
}

#this is the main loop to allow the user to make a selection and will only close 
#when they input "quit", which makes do_not_exit = false
#infinite loop (breaks when user types 'quit')
do_not_exit = True
while do_not_exit == True:
	#runs make_choice(), which prints out the menu selection options.
	make_choice()
	user_input = raw_input("Please Select Your Choice: ")

	#checks if their selection isin the user_selection dictionary
	#if it isn't, it will start the loop over and print out that
	#they made an invalid sellection.
	if user_input not in user_selection:
		print("you entered an invalid selection, please try again")
		continue

	#if the user types quit, it will break the loop and end the application
	if user_input == "quit":
		print("goodbye!!!")
		break;

	#makes run_choice equal to the selection they chose then runs the method
	run_choice = user_selection.get(user_input, "bad_input")

	run_choice()
