import random


def roll():
    min_value=1
    max_value=6
    roll_value=random.randint(min_value,max_value)
    
    return roll_value

random_value=roll()

##def print_f(v):
##    print("random value is - ",v)


##print_f(random_value)

while True:
    player_count=input("Enter the no. of players (2-4):" )
    if player_count.isdigit():
        player_count=int(player_count)
        if 2<=player_count<=4:
            break
        else:
            print("invalid number")
    else:
        print("Invalid, try again")


print ("no of players:",player_count)


max_score=50
player_scores=[0 for _ in range(player_count)]

while max(player_scores)<max_score:
        for playeridx in range(player_count):
            print("Player number",playeridx+1,"turn has just started!")
            print("your total score is : ",player_scores[playeridx])
            current_score=0
            while True:
                should_roll=input("Would you like to roll (y)? " )
                if should_roll.lower()!="y":
                    break

                value=roll()
                if value == 1:
                    print("Youl rolled a 1, Your turn done!!")
                    current_score=0
                    break
                else:
                    current_score = current_score+value
                    print("You rolled a : ",value)

                print("Your score is:", current_score)

            player_scores[playeridx] = player_scores[playeridx]+current_score
            print("your total score is", player_scores[playeridx])

    
max_score=max(player_scores)
winningidx=player_scores.index(max_score)
print("Player number ", winningidx+1,"is the winner with a score of : ", max_score)

