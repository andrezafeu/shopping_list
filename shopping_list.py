def add_item():
	print("What would you like to add to your shopping list?")
	print("Enter 'DONE' when you finish adding items")
	shopping_list = []
	while True:
		item = input("Item: ")

		if item == "DONE":
			break

		shopping_list.append(item)
		
	print("Shopping List:")
	print(shopping_list)

add_item()