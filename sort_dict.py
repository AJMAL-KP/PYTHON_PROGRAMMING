"""my_dict = {'banana': 3, 'apple': 4, 'cherry': 2}

items = list(my_dict.items())

for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:
            
            items[j], items[j + 1] = items[j + 1], items[j]

sorted_dict = {}
for key, value in items:
    sorted_dict[key] = value

print(sorted_dict)"""

dictionary = {5: "aejhro", 2: "soeiu", 6: "eiie", 1: "ojo"}


print("Ascending: ", dict(sorted(dictionary.items())))
print("Descending: ", dict(sorted(dictionary.items(), reverse=True)))