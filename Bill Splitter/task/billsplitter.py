# write your code here
import random

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

    # print(friends)

    lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky == 'Yes':
        lucky_friend = random.choice(list(friends.keys()))
        print(f'{lucky_friend} is lucky one!\n')
        friends = friends.fromkeys(friends, round(bill / (len(friends) - 1), 2))
        friends[lucky_friend] = 0
    else:
        print('No one is going to be lucky')

    print(friends)