colors = input("Enter colors (comma separated): ")

color_list = colors.split(",")

first_color = color_list[0]
last_color = color_list[-1]

print(f"First Color: {first_color}")
print(f"Last Color: {last_color}")
