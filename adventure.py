continue_game = True

rooms = {
    'initial_room': {
        'description': 'You entered the INITIAL ROOM and see 2 doors, one leads to the [l]left and the other one to the [r]right. What do you do?',
        'l': 'left_room',
        'r': 'right_room'
    },
    'middle_room': {
        'description': 'You entered the MIDDLE ROOM and see 1 door, it leads to the [a]ahead. What do you do?',
        'a': 'critical_room'
    },
    'left_room': {
        'description': 'You entered the LEFT ROOM and see 2 door, one leads [b]back to the initial room and the other one goes [a]ahead to the next room. What do you do?',
        'b': 'initial_room',
        'a': 'middle_room'
    },
    'right_room': {
        'description': 'You entered the RIGHT ROOM and see 1 door, it leads [b]back to the initial room. What do you do?',
        'b': 'initial_room'
    },
    'critical_room': {
        'description': 'You entered the CRITICAL ROOM and see 2 doors, one leads to the [l]left and the other one to the [r]right. What do you do?',
        'l': 'dragon_room',
        'r': 'final_room'
    },
    'dragon_room': {
        'description': 'You entered the DRAGON ROOM. You saw a hugh Dragon and it kills you. YOU\'R DEAD!',
    },
    'final_room': {
        'description': 'You entered the FINAL ROOM and see a lot of gold and precious stones. YOU WON THE GAME!',
    }
}

def print_introduction():
    print('--------------------   TextBased Adventure Game   --------------------')
    print('You are about to enter in a world of adveture, chaos and fluffy things')
    print('Hold my hand and I will show you every room of this magic land')
    print('Be aware! This might be super duper fun, so don\'t hold off my hand')
    print('or you might get lost for the whole eternity!')
    print('----------------------------------------------------------------------')
    print()



print_introduction()

actual_room = 'initial_room'

while continue_game:
    print(rooms[actual_room]['description'])

    next_room = input()
    print()

    try:
        actual_room = rooms[actual_room][next_room]
    except:
        print('Please, try enter a valid room.')
        print()
    
    if actual_room in ('dragon_room', 'final_room'):
        print(rooms[actual_room]['description'])
        print()
        continue_game = False

print('The Game is Over! Thank you for playing this game')
