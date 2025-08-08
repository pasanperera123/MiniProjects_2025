words = {"PAIR":"3", "HAIR":"3", "CHAIR":"4"}



def main():
    print("Welcome to Spelling Bee!!")
    print("Your letters are: A I P C R H G")
    print("You have 5 attempts")
    Attempts=0
    Total_score=0

    while len(words) > 0:
        Attempts +=1
        print(f"{len(words)} words left!!")
        print("Attempts :", Attempts)
        guess=input("Guess a word : ")
            

        if  Attempts==5 :
            break

        elif guess in words.keys():
            points = words.pop(guess)
            print(f"Good Job!! You scored {points} points")
            Current_score=int(points)
            Total_score = int(Total_score + Current_score)

        else:
            print("Try again!")
        
    print("\n\nGreat!!, Your total Score is : ", Total_score)


main()