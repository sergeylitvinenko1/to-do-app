import functions
import time

user_prompt = "Type add, show, edit, complete, or exit: "
now = time.strftime('%b %d, %Y %H:%M:%S')
print("It is", now)

while True:

    user_action = input(user_prompt)
    user_action = user_action.strip()  # return a copy of the string with leading and trailing whitespace removed

    if user_action.startswith("add"):

        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]  # list comprehension

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"  # f strings
            print(row)

    elif user_action.startswith("edit"):

        try:

            number = int(user_action[5:])
            print(number)
            index = int(number) - 1

            todos = functions.get_todos()
            new_todo = input("Enter the new todo: ")
            todos[index] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:

            print("Your command is not valid:")
            continue

    elif user_action.startswith("complete"):

        try:

            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_remove} was removed from thr list."

            print(message)

        except IndexError:

            print("There is not item with that number")
            continue

    elif user_action.startswith("exit"):

        break  # exit the while loop

    else:

        print("The command is not valid!")

print("Bye!")
