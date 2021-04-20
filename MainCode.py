import time
import threading

# Variables
wait = time.sleep
Unavailable = "Still being worked on."
commands = Unavailable
GenerationNumber = 1

# Bitcoin generator function
def BitcoinCount():
    global Bitcoin
    global BitcoinActive
    global Bitcoin_1

    Bitcoin_1 = True
    BitcoinActive = True
    Bitcoin = 0


    while BitcoinActive:
        wait(1)
        Bitcoin = Bitcoin + GenerationNumber


# Main function
def Main(gen_num):
    global SoftwareUpgrade

    Game = True
    Balance = 500
    SoftwareUpgrade = 1

    if Game:
        print("To get the commands type \"help\".")

        while Game:
            MainInput = input("\nCommand: ")

            # Help
            if MainInput == "help":
                print(commands)

            # Value
            elif MainInput == "value":
                print(str(Bitcoin) + "dc")

            # Upgrade
            elif MainInput == "upgrade":
                global upgrade2
                global upgrade3
                global break2
                global break3

                upgrade = True
                upgrade2 = False
                upgrade3 = False
                break2 = False
                break3 = False

                phrase = "What upgrade would you like to get: lvl_2, lvl_3, none"
                print(phrase)

                while upgrade:
                    upgrade_input = input("\nUpgrade: ")

                    # Upgrade 2
                    if upgrade_input == "lvl_2":

                        if not upgrade2:
                            Lvl2_upgrade = True
                            Upgrade2_price = 50
                            print("Would you like to buy LVL 2 bitcoin software for 50$?")
                            print("Yes: \'y\', No: \'n\'")

                            if Lvl2_upgrade:

                                while Lvl2_upgrade:
                                    verification2 = input("\nCommand2: ")

                                    if verification2 == "y":

                                        if Balance > Upgrade2_price:
                                            gen_num = 2
                                            Balance = Balance - 50
                                            SoftwareUpgrade = 2
                                            upgrade2 = True
                                            break2 = True
                                            print("Upgrade Complete!")
                                            print("\n" + phrase)
                                            break

                                        else:
                                            print("You do not have enough cash!")

                                    elif verification2 == "n":
                                        print(phrase + "\n")
                                        break

                                    elif break2:
                                        break

                                    else:
                                        print("Invalid Command!")
                        else:
                            print("You already have this upgrade!")

                    # Upgrade 3
                    elif upgrade_input == "lvl_3":

                        if upgrade2:

                            if not upgrade3:
                                Lvl3_upgrade = True
                                Upgrade3_price = 200
                                print("Would you like to buy LVL 3 bitcoin software for 200$?")
                                print("Yes: \'y\', No: \'n\'")

                                if Lvl3_upgrade:

                                    while Lvl3_upgrade:
                                        verification3 = input("\nCommand3: ")

                                        if verification3 == "y":

                                            if Balance > Upgrade3_price:
                                                gen_num = 3
                                                Balance = Balance - 200
                                                upgrade3 = True
                                                print("Upgrade Complete!")
                                                break

                                            else:
                                                print("You do not have enough cash!")

                                        elif verification3 == "n":
                                            print(phrase + "\n")
                                            break

                                        else:
                                            print("Invalid Command!")
                            else:
                                print("You Already have this upgrade!")
                        else:
                            print("You do not have upgrade 2!")

                    # No Upgrade
                    elif upgrade_input == "none":
                        break

                    else:
                        print("Invalid Command")

            # Convert
            elif MainInput == "convert":
                print(Unavailable)

            # Balance
            elif MainInput == "balance":
                print(str(Balance) + "$")

            # Live
            elif MainInput == "live":
                live = True
                if live:
                    print("type \'.\' to end live counting.")
                    while live:
                        wait(1)
                        print(Bitcoin)


            else:
                print("Invalid Command!")

# Running all functions
threading.Thread(target=BitcoinCount).start()
threading.Thread(target=Main, args=(GenerationNumber,)).start()
