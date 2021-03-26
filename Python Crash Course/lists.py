friends = ["Peter", "Pete", "Pet", "Hun", "Jade"]

print(friends)
print(friends[1])
friends[1] = "Julie"
print(friends[1:])

lucky_numbers = [4, 3, 2, 7, 13, 23]
#friends.extend(lucky_numbers)
friends.append("Ralph")
friends.insert(1, "Pony")
friends.remove("Pet")
friends.pop()
print(friends)
friends.index("Pony")

friends.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
print(friends2)