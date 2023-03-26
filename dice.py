import random

num_list = [ 1 , 2 , 3 , 4 , 5 , 6 ]
num = random.choice(num_list)
print(num)
if num == 1:
    print("┌─────────┐")
    print("|         |")
    print("|    ●    |")
    print("|         |")
    print("└─────────┘")
elif num == 2:
    print("┌─────────┐")
    print("| ●       |")
    print("|         |")
    print("|       ● |")
    print("└─────────┘")
elif num == 3:
    print("┌─────────┐")
    print("| ●       |")
    print("|    ●    |")
    print("|       ● |")
    print("└─────────┘")
elif num == 4:
    print("┌─────────┐")
    print("| ●     ● |")
    print("|         |")
    print("| ●     ● |")
    print("└─────────┘")
elif num == 5:
    print("┌─────────┐")
    print("| ●     ● |")
    print("|    ●    |")
    print("| ●     ● |")
    print("└─────────┘")
else:
    print("┌─────────┐")
    print("| ●     ● |")
    print("| ●     ● |")
    print("| ●     ● |")
    print("└─────────┘")


# print("Rolling the dice " + str(a) + " times...")
# for i in range(a):
#     result = num
#     print("Roll " + str(i+1) + ": " + str(result))