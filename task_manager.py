'''SE T26 - Capstone Project III - Lists, Functions and String Handling
'''

#=====importing libraries===========
import datetime
from datetime import datetime, timedelta
from datetime import date

#===Functions===

def users_dict():
	'''Creates a dictionary of users and their passwords from users.txt'''
	users_dict = {}
	with open('user.txt', 'r+', encoding = 'utf-8') as users_file:
		for line in users_file.read().split("\n"):
			user, pswrd = line.split(", ")
			users_dict[user] = pswrd
	return users_dict

def reg_user(users):
	'''Add a new user to the user.txt file
	- Request input of a new username
	- Request input of a new password
	- Request input of password confirmation.
	- Check if the new password and confirmed password are the same.
	- If they are the same, they are added to the user.txt file,
	- Otherwise there is a message asking to try again.'''
	new_user = input("Enter new username: ")
	if new_user in users: #prevents duplicate usernames in user.txt
		print("This username is already registered.")
	else:
		new_pswrd1 = input("Enter new password: ")
		new_pswrd2 = input("Confirm new password: ")
		if new_pswrd1 == new_pswrd2:
			with open('user.txt', 'a+', encoding = 'utf-8') as users_file: #appends to the end of the file
				users_file.write(f"\n{new_user}, {new_pswrd1}")
			print(f"New user {new_user} added.")
		else:
			print("Whoops! Those passwords don't match. Please try again.")
	return

def add_task(user, current_date):
	'''Allow a user to add a new task to task.txt file
			- The user is prompted for the following: 
				- A username of the person whom the task is assigned to,
				- A title of a task,
				- A description of the task and 
				- the due date of the task.
			- Then gets the current date.
			- The data is added to the file task.txt and
			- 'No' is added to indicate if the task is complete.'''
	new_task_user = input("Enter the username to assign the task: ")
	if new_task_user not in users: # prevents a user being assigned to task before the user has been added to users.txt
		print("This user does not exist. Please register user.") # Goes back to menu
	else:
		new_task_title = input("Enter the title of the task: ")
		if not new_task_title: # if no input, records [Blank]
			new_task_title = '[Blank]'
		new_task_desc = input("Enter the description of the task: ")
		if not new_task_desc: # if no input, records [Blank]
			new_task_desc = '[Blank]'
		new_task_due = input("Enter the due date of the task, e.g. 10 Oct 2019\nOr hit return to add date 7 days from now: ")
		if not new_task_due: # if no input, date is 7 days from current date
			seven_days_ahead = date.today() + timedelta(days=7)
			new_task_due = seven_days_ahead.strftime("%d %b %Y")
		with open('tasks.txt', 'a+', encoding = 'utf-8') as tasks_file: #appends to the end of the file
			tasks_file.write(f"\n{new_task_user}, {new_task_title}, {new_task_desc}, {current_date}, {new_task_due}, No")
		print(f"New task added:\n{new_task_user}, {new_task_title}, {new_task_desc}, {current_date}, {new_task_due}, No")
		return

def read_tasks():
	'''Program will read the task from task.txt file and save to list'''
	tasks_file = open('tasks.txt', 'r', encoding = 'utf-8')

	tasks = []

	for line in tasks_file.read().split("\n"):
		tasks.append(line)
	tasks_file.close()
	
	return tasks
	#end of read_tasks()

def view_all():
	'''Program will read the task from task.txt file and print all the tasks to the console in the format of Output 2 in the task PDF'''
	tasks_file = open('tasks.txt', 'r', encoding = 'utf-8')
	
	tasks = read_tasks()
	all_tasks = []

	for task in tasks:
		task_user, task_title, task_desc, date_created, task_due, isTaskComplete = task.split(", ")
		all_tasks.append(f'''
			______________________________________________________

			Task:               {task_title}
			Assigned to:        {task_user}
			Date assigned:      {date_created}
			Due date:           {task_due}
			Task complete?      {isTaskComplete}
			Task description:
				{task_desc}''')

	for task in all_tasks:
		print(task)

def view_mine(users, username):
	'''Program will read the task from task.txt file and print user's tasks to the console with corresponding number to identify task.
		The user can select a specific task (by number) or input '-1' to return to main menu
		If the user selects a specific task, they should be able to choose to either 'mark the task as complete' or 'edit the task'
			- mark the task as complete: the 'Yes'/'No' value is changed to 'Yes'
			- edit the task:  the username of the person to whom the task is assigned or the due date of the task can be edited.
			- the task can only be edited if it not yet completed.
	'''
	
	tasks = read_tasks()

	my_tasks_formatted = [] #The readable format of the user's tasks
	my_tasks = [] #The format for modifying tasks.txt
	task_count = 1

	for line in tasks:
		task_user, task_title, task_desc, date_created, task_due, isTaskComplete = line.split(", ")
		if task_user == username:
			my_tasks.append([task_user, task_title, task_desc, date_created, task_due, isTaskComplete]) #append filtered task as list to my_tasks list
			my_tasks_formatted.append(f'''
				______________________________________________________

				Task number:        {task_count}
				Task:               {task_title}
				Assigned to:        {task_user}
				Date assigned:      {date_created}
				Due date:           {task_due}
				Task complete?      {isTaskComplete}
				Task description:
					{task_desc}''')
			task_count += 1
		else:
			pass
	for task in my_tasks_formatted:
		print(task)

	view_menu2 = True
	while view_menu2 == True:
		'''User can choose a task from the list by number. -1 will take user back to main menu.'''
		try:
			choose_task = int(input('''\nChoose a task number. Or enter -1 to return to menu: '''))
		except:
			print('You must enter an integer.')
		else:
			if choose_task != -1:
				if choose_task in range(1, task_count): # makes sure choice is valid

					taskToChange = my_tasks[choose_task-1] # picks the task from the list based on chosen number
					taskToChange = ', '.join(taskToChange) # changes the task from a list to a string (so it can be split and also to use replace later)
					task_user, task_title, task_desc, date_created, task_due, isTaskComplete = taskToChange.split(", ")
					
					print(f"You have chosen task number {choose_task}:\n{taskToChange}")
					
					menu2 = input('''
Select one of the following Options below:
	mc	-     Mark the task as complete
	ed	-     Edit the task
	e	-     Go back
''').lower()
					if menu2 == 'mc':
						'''Mark the task complete and overwrite the task in the text file.'''
						if (isTaskComplete == 'No'): # check task is not completed

							updated_task = f"{task_user}, {task_title}, {task_desc}, {date_created}, {task_due}, Yes"
							with open('tasks.txt', 'r', encoding = 'utf-8') as task_file: #reads the file
								mod_task_file = task_file.read() #copy the file
								mod_task_file = mod_task_file.replace(taskToChange, updated_task) #replace the existing task with modified task (isTaskComplete changed to 'Yes')
							with open('tasks.txt', 'w', encoding = 'utf-8') as task_file2: 
								task_file2.write(mod_task_file) #overwrites the file
							print(f"Updated! The task is marked as complete: \n{updated_task}")
							#end of update the task as complete
						else:
							print("This task is already complete.")
						# end of mark the task complete

					elif menu2 == 'ed':
						if (isTaskComplete == 'No'): # Task can only be edited if the task has not been completed 
							menu3 = input('''
Which one of the following Options:
	us	-	Change the user assigned to task
	dd	-	Change the due date of the task
	e	-	Go back
		''').lower()
							if menu3 == 'us': # user chooses to change the user assigned
								new_task_user = input('To whom do you want to change the assigned user?: ')
								if new_task_user in users.keys():
									updated_task_user = f"{new_task_user}, {task_title}, {task_desc}, {date_created}, {task_due}, {isTaskComplete}"
									with open('tasks.txt', 'r', encoding = 'utf-8') as task_file: #reads the file
										mod_task_file = task_file.read() #copy the file
										mod_task_file = mod_task_file.replace(taskToChange, updated_task_user) #replace the existing task with new user)
									with open('tasks.txt', 'w', encoding = 'utf-8') as task_file2: 
										task_file2.write(mod_task_file) #overwrites the file
									print(f"Updated! The user assigned has changed: \n{updated_task_user}")
								else:
									print(f"{new_task_user} is not a valid user.")
								# end of change the user assigned

							elif menu3 == 'dd': # user chooses to change due date
								new_task_due = input('What is the new due date? Please use the format dd mmm yyyy: ')

								updated_task_dd = f"{task_user}, {task_title}, {task_desc}, {date_created}, {new_task_due}, {isTaskComplete}"
								with open('tasks.txt', 'r', encoding = 'utf-8') as task_file: #reads the file
									mod_task_file = task_file.read() #copy the file
									mod_task_file = mod_task_file.replace(taskToChange, updated_task_dd) #replace the existing task with new due date)
								with open('tasks.txt', 'w', encoding = 'utf-8') as task_file2: 
									task_file2.write(mod_task_file) #overwrites the file
								print(f"Updated! The user assigned has changed: \n{updated_task_dd}")
								# end of change the due date

							elif menu3 == 'e': # user chooses to go back
								pass #back to menu2
							else:
								print("Sorry. This is not a correct menu choice")
						else:
							print('This task cannot be edited because it is alreaady completed.')
						# end of edit task

					elif menu2 == 'e': # user chooses to go back
						pass #back to choose a task input
						# end of go back from menu2

					else:
						print("Sorry. This is not a correct menu choice.")
					# end of menu2	
				else: # If a number outside the range from 1 to number of tasks is chosen (apart from -1)
					print(f"Whoops! Please choose a task number between 1 and {len(my_tasks)}.")
				# end of check task number is valid
			
			elif choose_task == -1: # if -1 is typed
				view_menu2 = False #back to main menu
			
			else:
				print("You have made a wrong choice. Please try again")
	# end of def view_mine(username)

def tot_tasks(): # counts the total number of tasks in tasks.txt
	'''Total number of tasks'''
	tot_tasks = 0
	with open('tasks.txt', 'r', encoding = 'utf-8') as tasks_file:
		for line in tasks_file.read().split("\n"):
			tot_tasks += 1
	return tot_tasks
	#end of tot_tasks

def tot_completed_tasks(current_date): # returns total completed tasks and total overdue tasks
    tasks = read_tasks()
    tot_completed_tasks = 0
    tot_overdue_tasks = 0
    current_date = datetime.strptime(current_date, "%d %b %Y")

    for task in tasks:
        task_user, task_title, task_desc, date_created, task_due, isTaskComplete = task.split(", ")
        task_due = datetime.strptime(task_due, "%d %b %Y")
        if isTaskComplete == 'Yes':
            tot_completed_tasks +=1
        elif (isTaskComplete == 'No') and (task_due < current_date):
            tot_overdue_tasks +=1
        else:
            pass
    return tot_completed_tasks, tot_overdue_tasks
	# end of tot_completed_tasks()

def user_completed_tasks(user, current_date): # returns for each user: total tasks, total compelted tasks, and total overdue tasks
	tasks = read_tasks()
	user_tot_tasks = 0
	user_tot_completed_tasks = 0
	user_tot_overdue_tasks = 0
	current_date = datetime.strptime(current_date, "%d %b %Y")

	for task in tasks:
		task_user, task_title, task_desc, date_created, task_due, isTaskComplete = task.split(", ")
		task_due = datetime.strptime(task_due, "%d %b %Y")
		if user == task_user:
			user_tot_tasks += 1
			if isTaskComplete == 'Yes':
				user_tot_completed_tasks +=1
			elif (isTaskComplete == 'No') and (task_due < current_date):
				user_tot_overdue_tasks +=1
			else:
				pass
	return user_tot_tasks, user_tot_completed_tasks, user_tot_overdue_tasks
	#end of user_completed_tasks()

def tot_users():
	'''Counts number of users'''
	tot_users = 0
	with open('user.txt', 'r+', encoding = 'utf-8') as users_file:
		for line in users_file.read().split("\n"):
			tot_users += 1
	return tot_users
	# end of tot_users

def percentage(part, whole): # calculates percentage and returns as string to 1 decimal point
    if part != 0:
        percentage = 100 * float(part)/float(whole)
    else: # prevent zero error
        percentage = 0
    return "{:.1f}%".format(percentage)

def disp_stats(tot_tasks, tot_users):
  '''The total number of tasks and the total number of users are displayed'''
  print(f'''
        Total users:    {tot_users}
        Total tasks:    {tot_tasks}
  ''')
  # end of disp_stats()

def gen_task_reports(tot_completed_tasks, tot_overdue_tasks, tot_tasks):
	'''Text files called task_overview.txt is generated'''
	'''task_overview.txt should contain:
		-	total number of tasks
		-	total number of completed tasks
		-	total number of uncompleted tasks
		-	total number of are overdue
		-	percentage of tasks that are incomplete
		-	percentage of tasks that are overdue
	'''
	tot_uncompleted_tasks = tot_tasks-tot_completed_tasks
	percentage_incomplete = percentage(tot_uncompleted_tasks, tot_tasks)
	percentage_overdue = percentage(tot_overdue_tasks, tot_tasks)

	with open('task_overview.txt', 'w+', encoding = 'utf-8') as task_overview:
		task_overview.write(f'''Total number of tasks:                      {tot_tasks}
Total number of completed tasks:            {tot_completed_tasks}
Total number of uncompleted tasks:          {tot_uncompleted_tasks}
Total number of overdue tasks:              {tot_overdue_tasks}
Percentage of incomplete tasks:             {percentage_incomplete}
Percentage of overdue tasks:                {percentage_overdue}''')
	print("New file task_overview.txt generated.")
	# end of gen_task_report

def gen_user_report(users, tot_users, tot_tasks):
    '''Text file user_overview.txt is generated'''
    '''user_overview.txt should contain:
		-	total number of users registered
		-	total number of tasks
		-	for each user describes:
			-	total number of tasks assigned
			-	percentage of the tasks assigned that are completed
			-	percentage of the tasks assigned that are incomplete
			-	percentage of taks that are overdue
    '''
    
    with open('user_overview.txt', 'w+', encoding = 'utf-8') as user_overview:
        user_overview.write(f'''Total number of users:                      {tot_users}
Total number of tasks:                      {tot_tasks}''')
    for user in users.keys():
        user_tot_tasks, user_tot_completed_tasks, user_tot_overdue_tasks = user_completed_tasks(user, current_date)
        user_percentage_complete = percentage(user_tot_completed_tasks, user_tot_tasks)
        user_percentage_incomplete = percentage(user_tot_tasks - user_tot_completed_tasks, user_tot_tasks)
        user_percentage_overdue = percentage(user_tot_overdue_tasks, user_tot_tasks)
        
        with open('user_overview.txt', 'a', encoding = 'utf-8') as user_overview:
            user_overview.write(f'''
For {user}:
    Total number of tasks assigned:             {user_tot_tasks}
    Percentage of completed tasks:              {user_percentage_complete}
    Percentage of incomplete tasks:             {user_percentage_incomplete}
    Percentage of overdue tasks:                {user_percentage_overdue}''')
    print("New file user_overview.txt generated.")
	# end of gen_user_report()

def print_report(file):
	'''Program will print the task_overview.txt or user_overview.tx in a user-friendly manner'''
	stats_file = open(file, 'r', encoding = 'utf-8')
	for line in stats_file:
		print(line)

#====Login Section====
'''Allow the user to login.
'''
users = users_dict() # creates a dictionary of users and their passwords from users.txt

username = input("Username: ")
while username not in users.keys():
    print("This username is not recognised. Please try again.")
    username = input("Username: ")

password = input("Password: ")
while password != users[username]:
    print("Incorrect password. Please try again.")
    password = input("Password: ")

#====Menu Section====
'''Allow the user to choose from the menu.
The menu appears differently depending if the user is the admin.
'''
current_date = date.today().strftime("%d %b %Y")
tasks = [] #overwrites tasks list when file is restarted

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
	if username == "admin":
		menu = input('''
Select one of the following Options below:
	r -     Registering a user
	a -     Adding a task
	va -    View all tasks
	vm -    View my tasks
	gr -    Generate reports
	ds -    Display statistics
	e -     Exit
: ''').lower()
	else:
		menu = input('''
Select one of the following Options below:
	r -     Registering a user
	a -     Adding a task
	va -    View all tasks
	vm -    View my tasks
	e -     Exit
	: ''').lower()    

	if (menu == 'r') and (username == "admin"):
		users = users_dict()
		reg_user(users)
	
	elif (menu == 'r') and (username != "admin"):
		print('Only the admin can register users.')

	elif menu == 'a':
		users = users_dict()
		add_task(users, current_date)

	elif menu == 'va':
		view_all()
		print('			______________________________________________________') # print final line under printed tasks

	elif menu == 'vm':
		users = users_dict()
		view_mine(users, username)

	elif menu == 'gr':
		users = users_dict() # creates users dictionary
		gr_tot_tasks = tot_tasks() # counts the total number of tasks
		gr_tot_users = tot_users() # counts the total number of users
		gr_tot_completed_tasks, gr_tot_overdue_tasks = tot_completed_tasks(current_date)
		gen_task_reports(gr_tot_completed_tasks, gr_tot_overdue_tasks, gr_tot_tasks) # generates task_overview.txt  
		gen_user_report(users, gr_tot_users, gr_tot_tasks) # user_overview.txt

	elif menu == 'ds' and username == "admin":
		users = users_dict() # creates users dictionary
		ds_tot_tasks = tot_tasks() # counts the total number of tasks
		ds_tot_users = tot_users() # counts the total number of users
		ds_tot_completed_tasks, ds_tot_overdue_tasks = tot_completed_tasks(current_date)
		gen_task_reports(ds_tot_completed_tasks, ds_tot_overdue_tasks, ds_tot_tasks) # generates task_overview.txt  
		gen_user_report(users, ds_tot_users, ds_tot_tasks) # user_overview.txt
		
		print('Summary:')
		disp_stats(tot_tasks, tot_users)
		print('''\nDisplaying task_overview.txt:
______________________________________________________\n''')
		print_report('task_overview.txt')
		print('''\nDisplaying user_overview.txt:
______________________________________________________\n''')
		print_report('user_overview.txt')
		print('______________________________________________________')

	elif menu == 'e':
		print('Goodbye!!!')
		exit()

	else:
		print("You have made a wrong choice. Please try again")
