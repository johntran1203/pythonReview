# Define my_stuff
my_stuff = [1, 2, 3, 4, "Camera", 2.5]
# Define nums
nums = list(range(1,100))

# 'Camera' in my_stuff

numbers = [1,2,3,4]

for number in numbers:
    print(number)

colors = ['red', 'purple', 'teal', 'emerald', 'magenta']
colors.append("purple")
colors.extend(["white", 1,2])
colors.insert(1,'hi')

# index =0
# while index < len(colors):
#     print(f"{index}: {colors[index]}")
#     index += 1

colors.pop()
colors.remove(1)
print(colors)