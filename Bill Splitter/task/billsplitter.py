# write your code here
count = int(input('Enter the number of friends joining (including you):\n'))
if count <= 0:
    print('No one is joining for the party')
else:
    friends = {}
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(count):
        friends[input()] = 0

    print(friends)