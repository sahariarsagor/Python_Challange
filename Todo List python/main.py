# Make a Todo LIst application
# which is console based
# programming language: Python 
# Programmer: Sahariar Sagor
# Source Code on github: @sahariarsagor

# make a empty list to store task 
todoList = []

# run a infinity loop 
while True:
    
    
    # Throw user a menu 
    print("______ Todolist Menu _______")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Todo")
    print("4. Exit")

    # get command or choice from user 
    choice = int(input("Enter your choice from 1 to 4: "))

    # now action start according to user choice 
    
    # checking choice 
    
    if choice == 1:
        task = input("Enter your task: ")
        todoList.append(task)
        print("Successfully added Task")

    elif choice == 2:
        if len(todoList) == 0:
            print("Nothing to remove")
        else:
            # showing user their list first 
            print("\n your todo list: ")
            for i in range(len(todoList)):
                print(f"{i+1}. {todoList[i]}")
            
            
            # get task no to remove specific task 
            taskNo = int(input("Enter task no to remove task: "))

            if taskNo >= 1 and taskNo <= len(todoList):
                removedTask = todoList.pop(taskNo-1)
                print(f"Successfully removed task, {removedTask}")
            else:
                print("Invalid Task No, thank you ")
    
    elif choice == 3:
        if len(todoList) == 0:
            print("There was nothing to see")
        else:
            print("\n your todo list: ")
            for i in range(len(todoList)):
                print(f"{i+1}. {todoList[i]}")
    
    elif choice == 4:
        print("Exiting TodoList app, Thank you")
        break
    
    else:
        print("Wrong Command Try again ")