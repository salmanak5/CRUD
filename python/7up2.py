# #enhance 7up or 7down gamej

# while True:
#     a = input("7up/7down: ").lower()
#     if a == '7up':
#         print("Congratulations, you win!")
#         break
#     elif a == '7down':
#         print('Try again, you lose.')
#         break
#     else:
#         print('Invalid input. Please choose "7up" or "7down".')

wins = 0
losses = 0

while True:
    a = input("7up/7down (or 'exit' to quit): ").lower()
    if a == '7up':
        print("Congratulations, you win!")
        wins += 1
    elif a == '7down':
        print('Try again, you lose.')
        losses += 1
    elif a == 'exit':
        print("Thanks for playing!")
        break
    else:
        print('Invalid input. Please choose "7up" or "7down".')
