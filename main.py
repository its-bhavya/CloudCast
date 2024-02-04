Welcome to Cloudcast! This interactive game tests your problem solving abilities (besides reviving the vintage era of text-based consoles). The setup is as follows:

The Hogwarts Meteorological Department owns a high-tech weather prediction software, which forecasts the upcoming month's weather statistics. This data is very valuable for the foreseeing and protection of the castles from threats. However, the return of the Dark Lord has messed their data up. As a result, the predictions have been offset by a large difference. Crunch time is approaching as Dark Magic is breaking through the shields around Hogwarts. The department, trusting you as an able logician, invites you to correct their data in limited moves.
'''
instructions = '''
You will be provided with two datasets, namely 30_day_forecasted_weather and 30_day_actual_weather. You may choose any week of the month, and any field out of - Temperature(T), Pressure(P) and Humidity(H) - from the predicted dataset, and change the department's prediction to your prediction. This costs a move, and you will have limited moves.
Your aim is to minimise the difference in your prediction and the recorded weather within restricted moves.
NOTE: Don't judge the game difficulty by the number of moves!
'''
final = '''
The Hogwarts Meteorological Department thanks you for your services. May the enchantments keep you safe.
(press enter to quit)...'''
title = "\n ************************************************************ ##CLOUDCAST## ************************************************************ "
bad = "Bad input."
prompt = "Kindly choose one of the above option numbers to proceed: "
unit = {'T':'°C', 'P':'hPa', 'H':'%'}

#scoring variables
offset = 0
maxdiff = offset
scoreslate = 0
score = 0
#difficulty selector
moves = 5
#state variables
new = True
conti = False



toolkit.Connect(pwd)
while True:
    print(title)
    print ('Menu Items  :\n1. Start\n2. Load\n3. Set difficulty level\n4. Instructions\n5. About\n6. Exit')
    choice=int(input(prompt))

    if choice==1:
        if new:
            print("Loading, please wait...")
            gen.generator(pwd)
            new = False
        if not conti:
            offset, scoreslate = scoring.init(moves)
            maxdiff = offset
            toolkit.display()
            conti = True
        
        while (moves):
            print('\n1. Make a move\n2. Display and compare\n3. Main Menu')
            cmd = int(input(prompt))

            if cmd == 1:
                week = int(input('\nWeek(1-5)... '))
                day = int(input('Day(1-7)... '))
                stat = input('Field (T-Temperature|P-Pressure|H-Humidity)... ').upper()

                if (1<=week<=5 and 1<=day<=7 and stat in ('T', 'P', 'H')):
                    u = unit[stat]
                    oldp, rec = toolkit.get_val(week, day, stat)
                    print('\nPrediction:', oldp, u)
                    val = int(input(f'Your prediction ({u}): '))
                    toolkit.update(week, day, stat, val)
                    offset -= abs(oldp-rec)
                    offset += abs(val-rec)
                    print("Updated successfully!")
                    moves -= 1
                    print("\nYou have %s move(s) remaining."%moves)
                else:
                    print(bad)

            elif cmd == 2:
                week = int(input("\nWeek of the month(1-5)... "))
                if (1<=week<=4):
                    toolkit.display(week)
                    woff = 0
                    for day in range(1,8):
                        for stat in ('T', 'P', 'H'):
                            pred, rec = toolkit.get_val(week, day, stat)
                            woff += abs(pred-rec)
                    print("Gross difference:", woff)
                    foo = input('\nPress enter to continue...')
                elif(week==5):
                    toolkit.display(week)
                    woff = 0
                    for day in range(1,3):
                        for stat in ('T', 'P', 'H'):
                            pred, rec = toolkit.get_val(week, day, stat)
                            woff += abs(pred-rec)
                    print("Gross difference:", woff)
                    foo = input('\nPress enter to continue...')
                else:
                    print(bad)

            elif cmd == 3:
                print("\nConsider saving before exiting!")
                conti = True
                break
            else:
                print(bad)
        else:
            foo = input("\nOut of moves! Press enter to evaluate your optimisation score...")
            score = scoring.judge(offset, scoreslate, maxdiff)
            print("Your optimisation score is ", score, "%. This is relative to the maximum possible score (100%). Congratulations!", sep='')
            new = True
            conti = False

    elif choice==2:
        e = toolkit.load()
        if e != -1:
            new = False
            conti = True
            maxdiff, scoreslate, offset, moves = e
            print("\nProgress restored. Choose start to begin.")
            foo = input('(press enter for main menu)...')
        else:
            print("\nSave file not found!")

    elif choice==3:
        if conti:
            print("\nError: A game is in progress!")
        else:
            print("\nChoose a level  :\nI - 5 moves\nII - 10 moves\nIII - 20 moves")
            lvl = input('>>> ').upper()
            if lvl in ['1', 'I']:
                moves = 5
            elif lvl in ['2', 'II']:
                moves = 10
            elif lvl in ['3', 'III']:
                moves = 20
            else:
                print(bad)

    elif choice==4:
        print(instructions)
        foo = input('Press enter to continue...')

    elif choice==5:
        print(about)
        foo = input('Press enter to continue...')

    elif choice==6:
        print("\nDo you want to save your progress?")
        x = input('(Y/N): ')
        if x.upper()=='Y':
            toolkit.exit(maxdiff, scoreslate, offset, moves, save=True)
        elif x.upper()=='N':
            toolkit.exit(save=False)
        else:
            print(bad+" Saving anyway...")
            toolkit.exit(maxdiff, scoreslate, offset, moves, save=True)
        foo = input(final)
        break

    else:
        print(bad)import gen
import toolkit
import scoring

#global constants
pwd = '5CyLgdZw.1owD_C?r4V_'
about = '''




