def todo_list():
    task = []
    while True:
        print("1.Add task\n2.View task\n3.Remove task\n4.Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task.append(input("Enter the task: "))
            print("Task added")
        elif choice == '2':
            if task:
                for i, j in enumerate(task, 1):
                    print(f"Task-{i}: {j}")
            else:
                print("No tasks")
        elif choice == '3':
            if task:
                n = int(input("Enter the task to remove: "))
                if 0 <= n < len(task):
                    del task[n-1]
                    print("Task removed")
            else:
                print("No tasks to remove")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid input")
todo_list()
