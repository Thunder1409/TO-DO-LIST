def create():
    task_title = open("task_title.txt", "a")
    task_description = open("task_description.txt", "a")

    title = input("Enter task tittle -: ") + "\n"
    description = input("Enter task description -: ") + "\n"

    task_title.write(title)
    task_description.write(description)

def update():
    change = input("Enter name of completed task -: ") + "\n"

    task_title = open("task_title.txt", "r")

    com = task_title.read().replace(change.removesuffix("\n"), change.removesuffix("\n") + " -> [Completed]")

    w_title = open("task_title.txt", "w")
    w_title.write(com)
    print("Done")

def track():
    task_title = open("task_title.txt", "r")
    task_description = open("task_description.txt", "r")

    title_list = task_title.readlines()
    description_list = task_description.readlines()

    for i in range(len(title_list)):
        print("\n Title -: ", title_list[i], "Description -: ", description_list[i])


print("--- Welcome to TO-DO list ---\n")

while True:

    print("\n\n1. Create \n2. Update \n3. Track \n99.Quit")
    todo = int(input("What you wnat to do -: "))

    if (todo == 1):
        create()

    elif (todo == 2):
        update()

    elif (todo == 3):
        track()

    elif(todo == 99):
        print("\nExiting")
        break

    else:
        print("Wrong Input...")