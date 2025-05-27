#Diego Osornio
#1/24/2025

words = ["Yes definitely","Signs point to yes", "It is certain", "It is decidedly so", "Without a doubt", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", " Ask again later", "Concentrate and ask again", "Reply hazy, try again", " My reply is no", "Outlook not so good"]
#Init
import random
import time
#fun
def ball():
    while True:
        try:
                print("Welcome to the 8 Ball! ")



                x = (input("Please enter a YES or NO question"))
                if x.endswith("?"):
                    print("Shaking...")
                    time.sleep(3)
                    print(random.choice(words))


                else:
                    print(" the question did NOT have a question mark")

                z = input("Would you like to play again? (y/n)")

                if z == "y":
                    continue
                if z == "n":
                    break

        except:
            print("Invalid put the Question with a question mark")










#main
ball()
