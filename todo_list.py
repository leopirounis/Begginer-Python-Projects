# Todo list my solution ✅

tasks = []

def is_word(s):
    return all(ch.isalpha() or ch.isspace() for ch in s) and s.strip() != ""


while True:
    print('''
Todo List Menu 
1. View Tasks
2. Add a Task
3. Remove a Task
4. Exit''')
    try:
      choice = int(input('Enter your choice: '))
      if choice == 1:
            if tasks != []:
                  for i, task in enumerate(tasks, start=1):
                       print(f"{i}. {task}")
            else:
                  print("No tasks in the list.\n")
      elif choice == 2:
            while True:
                  try:
                        new_task = input("Enter a new task: ")
                        if not is_word(new_task):
                              raise ValueError('Invalid task.')  
                        else:
                              tasks.append(new_task) 
                              break  
                  except: ValueError        
      elif choice == 3:
          for i, task in enumerate(tasks, start=1):
                  print(f"{i}. {task}")
          while True:
                try:
                      task_number = int(input("Enter the task number: "))
                      if 0 < task_number <= len(tasks): 
                             del tasks[task_number-1]
                             break
                      else: 
                            print("Invalid task number.")
                except ValueError:
                       print("Invalid task number.")          
      elif choice == 4:
            break
      else:
          print("Invalid choice.")    
    except ValueError:
         print("Invalid choice.")
                       