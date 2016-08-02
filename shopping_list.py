shopping_list = []

def add_item():
	print("What would you like to add to your shopping list?")
	show_commands()

	while True:
		item = input("> ").upper()

		if item == "DONE":
			break

		if item in shopping_list:
			print("This item is already on your list.")
			continue

		if item == "SHOW":
			print_list()

		elif item == "HELP":
			show_commands()
			
		else:
			shopping_list.append(item)
			print("Added {}. The list now has {} item(s)".format(item, len(shopping_list)))
		
	print_list()	

def show_commands():
	print("""Type 'SHOW' to see items in shopping list
Type 'HELP' to see these commands again
Type 'DONE' to quit the app""")

def print_list():
	print("Shopping List:")
	print(shopping_list)

add_item()