import tasks

print("Welcome to your personal Task Tracker")

master_tracker = tasks.TaskManager(input("What is your name?\n"))

menu_string = '\n' + 'Please select onf of the following options:' +'\n\n'+ \
                'MENU' + '\n' + \
                '----------------------------------------' + '\n' + \
                '1 Create new task' + '\n' + \
                '2 Edit existing task' + '\n' + \
                '3 Mark task as complete' + '\n' + \
                '4 Show tasks to be competed' + '\n' + \
                '5 EXIT' + '\n'
valid_options = ['1', '2', '3', '4', '5']
valid_changes = ['name', 'date', 'description']

while True:
    while True:
        var = input('\n ...press enter to continue...')
        if not(var):
            print(menu_string)
            menu_input = input('Enter Menu Choice: ')
            break
        else:
            print('Press enter to continue')
    
    # 1: CREATE NEW TASK
    if menu_input == '1':
        master_tracker.addTask()
    # 2: EDIT TASK
    elif menu_input == '2':
        task_name_to_change = "!!!!!"
        while (master_tracker.indexTask(task_name_to_change) > -1):
            master_tracker.listTasks()
            print()
            task_name_to_change = input("Which task would you like to change?\n")

        
        while True:
            change_option = input("What would you like to change (Name, Date, Description)").lower()
            if change_option == 'name':
                master_tracker.tasks[master_tracker.indexTask(task_name_to_change)].name = input("What would You like to chnage the name to?\n")
                break
            elif change_option == 'date':
                master_tracker.tasks[master_tracker.indexTask(task_name_to_change)].due_date = input("What is the new due date?\n")
                break
            elif change_option == 'description':
                master_tracker.tasks[master_tracker.indexTask(task_name_to_change)].description = input("What would you like to change the description to?")
                break
            else:
                print("Invalid Input")


    # 3: MARK AS COMPLETE
    elif menu_input == '3':
        task_name_to_change = ""
        while (master_tracker.indexTask(task_name_to_change) > -1):
            master_tracker.listTasks()
            print()
            task_name_to_change = input("Which task would you like to change?\n")

        master_tracker.tasks[master_tracker.indexTask(task_name_to_change)].competed = True
        master_tracker.update()
        
    # 4: DISPLAY TASKS
    elif menu_input == '4':
        master_tracker.listTasks()
    elif menu_input == '5':
        break

print('Goodbye!')