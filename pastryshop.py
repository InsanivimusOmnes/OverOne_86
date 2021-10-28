import pyttsx3

engine = pyttsx3.init()     # инициализация движка

# зададим свойства
engine.setProperty('rate', 170)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)

pastry = {'napoleon': [['butter', 'flour', 'sugar'], 7, 1000],
          'honey cake': [['flour', 'butter', 'sugar'], 4, 1025],
          'kiev': [['sugar', 'flour', 'butter'], 5, 985]}

choices = [0, 1, 2, 3, 4, 5]

while True:
    # engine.say('''If you want to see a description, enter 1.
    #  View price - enter 2.
    #  View quantity - enter 3.
    #  View all information - enter 4.
    #  If you want to buy a cake, enter 5.
    #  To exit the program, enter 0''')rm
    # engine.runAndWait()
    choice = input('Make your choice: ')

    try:
        choice = int(choice)
    except ValueError:
        engine.say('You have not entered a number')
        engine.runAndWait()
    else:
        if choice == 0:
            engine.say('Come again!')
            engine.runAndWait()
            break
        elif choice not in choices:
            engine.say('There is no such option')
            engine.runAndWait()
        else:
            while True:
                engine.say('''If you want to continue the selection, enter which cake you are interested in.
                 If you want to exit to the menu above, enter 0.''')
                engine.runAndWait()
                cake = input('Enter which cake you are interested in or 0 to exit: ').lower()

                if cake == '0':
                    break
                elif cake not in pastry.keys():
                    engine.say('There is no such cake')
                    engine.runAndWait()
                else:
                    for k, v in pastry.items():
                        if cake == k:
                            if choice == 1:
                                engine.say(f'The cake {cake} consists of {v[0]}')
                                engine.runAndWait()
                            elif choice == 2:
                                engine.say(f'The cake {cake} costs {v [1]} rubles')
                                engine.runAndWait()
                            elif choice == 3:
                                engine.say(f'The cake {cake} {v [2]} grams left')
                                engine.runAndWait()
                            elif choice == 4:
                                engine.say(f'The cake {cake} consists of {v[0]}')
                                engine.say(f'The cake {cake} costs {v [1]} rubles')
                                engine.say(f'The cake {cake} {v [2]} grams left')
                                engine.runAndWait()
                            elif choice == 5:
                                while True:
                                    engine.say('''If you want to continue the selection, enter how many cake you should put
                                     If you want to exit to the menu above, enter 0 ''')
                                    engine.runAndWait()
                                    amount = input('Enter the amount of cake in grams or 0 to exit: ')

                                    try:
                                        amount = int(amount)
                                    except ValueError:
                                        engine.say('You have not entered the quantity')
                                        engine.runAndWait()
                                    else:
                                        if amount == 0:
                                            break
                                        elif amount <= v[2]:
                                            total = amount * v[1] / 100
                                            engine.say(f'To pay {total} rubles')
                                            engine.say(f'The cake {cake} left {v [2] - amount} grams')
                                            engine.runAndWait()
                                            v[2] = v[2] - amount
                                        else:
                                            engine.say(f'You have entered more grams than you have left: {cake} total {v [2]} grams')
                                            engine.runAndWait()
