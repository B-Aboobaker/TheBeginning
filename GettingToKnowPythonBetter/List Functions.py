print("LIST FUNCTIONS!!!\n")

friends = ["Mike", "Jake", "Manny", "Sam", "Farhana"]
lucky_numbers = [4, 8, 15, 23, 42]

friends.extend(lucky_numbers)  # 'extend' function allows to concatenate lists
print(friends)
print("")

friends.append("Marry")  # append to end of list
print(friends)
print("")

friends.pop()  # removes last element from list
print(friends)
print("")

friends.insert(1, "Aboo")  # insert at any element
print(friends)
print("")

friends.remove("Manny")  # remove any element from list
print(friends)
print("")

print(friends.index("Aboo"))

friends.sort()  # alphabetical order 
print(friends)
