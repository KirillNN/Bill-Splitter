# write your code here
count = int(input('Enter the number of friends joining (including you):\n'))
if count <= 0:
    print('No one is joining for the party')
else:
    friends = {}
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(count):
        friends[input()] = 0

    bill = int(input('\nEnter the total bill value:\n'))

    friends = friends.fromkeys(friends, round(bill / len(friends), 2))
    # for i in range(len(friends)):
    #     friends[i] = round(bill / len(friends), 2)
    # for item in friends.items():
    #     print(item)

    print(friends)
