import random
import time
from sys import exit

class Board():
    lst = []

    def __init__(self) -> None:
        self.lst = [i for i in range(1, 101)]


class Dice():

    def roll(self):
        return random.randint(1,6)


class Player():

    def __init__(self, name) -> None:
        self.position = 0
        self.name = name

    def getPosition(self):
        time.sleep(1)
        print(f"{self.name}'s postion: {self.position}")


class Snake():

    def __init__(self, head, tail) -> None:
        self.head = head
        self.tail = tail

class Ladder():

    def __init__(self, head, tail) -> None:
        self.head = head
        self.tail = tail


class Game():

    def diceRoll(self, player, dice):
        while True:
            should_roll = input("press y to roll the dice: ")

            if should_roll.lower() == 'y':
                steps = dice.roll()
                # steps = int(input("enter fake value: "))
                print("Rolling the dice...")
                time.sleep(1)
                print(steps)

                if player.position == 0:
                    if steps == 6 or steps == 1:
                        self.changePosition(player, 1)
                        print("Congrats your coin is unlocked...")
                        continue
                    else:
                        print("You are still locked..")
                        break
                else:
                    self.changePosition(player, steps)
                    break
            else:
                print("Enter valid input")


    def changePosition(self, player, steps):
        if player.position + int(steps) <= 100:
            player.position += int(steps)
        

    def has_won(self, player):

        if player.position == 100:
            print(f"{player.name} won...")
            return True

        return False 


    def checkSnake(self, player, snakes):
        for snake in snakes:
            if player.position == snake.head:
                time.sleep(1)
                print(f"\nOooopps... {player.name} is bitten by a snake. :(")
                player.position = snake.tail


    def checkLadder(self, player, ladders):
        for ladder in ladders:
            if player.position == ladder.tail:
                time.sleep(1)
                print(f"\nGreat!!! {player.name} found a ladder. :)")
                player.position = ladder.head


    def checkPlayerOverlap(self, player, players, dice):
        if player.position != 0:   
            for other_player in players:
                if player != other_player:
                    if player.position == other_player.position:
                        time.sleep(1)
                        print(f"{player.name} overlaped {other_player.name}.")
                        other_player.position = 0
                        
                        # if the player cuts another player's coin by overlaping
                        # they get a bonus chance
                        self.diceRoll(player, dice)


    def snakeOverlap(self, position, snakes):
        for snake in snakes:
            if snake.head == position or snake.tail == position:
                return True
        return False


    def usersPlaying(self):
        players = []
        while True:
            total_players = input("How many users will be playing? (2 or 3 or 4)\n")

            if total_players.isdigit() and (int(total_players) in [2, 3, 4]):
                for i in range(1, int(total_players) + 1):
                    name = input(f"please enter the name of player{i}: ")
                    player = Player(name)
                    players.append(player)
                break
            else:
                print("Please input valid value...")
        return players


    def configureSnakes(self):
        snakes = []
        default_snakes = input("\ndo you want to set the snakes or do you want to use the game default?\npress 'y' to user default. ")

        if default_snakes.lower() == 'y':
            snake1 = Snake(40, 3)
            snake2 = Snake(53, 10)
            snake3 = Snake(85, 27)
            snake4 = Snake(98, 6)
            snake5 = Snake(20, 10)
            snakes = [snake1, snake2, snake3, snake4, snake5]

        else:
            while True:
                no_of_snakes = input("How many snakes do you want to plant? (please input a value between 5 to 7)\n")

                if no_of_snakes.isdigit() and int(no_of_snakes) in [5, 6, 7]:
                    for i in range(1, int(no_of_snakes) + 1):
                        print(f"Please enter the values of snake{i}")
                        while True:
                            print("accepts values between 20 to 97")
                            head = input("head: ")

                            if head.isdigit() and (int(head) in range(20, 98)):
                                head = int(head)
                                for snake in snakes:
                                    if snake.head == head:
                                        print("A snake is already present at this head..")
                                        break
                                    elif snake.tail == head:
                                        print("A snake's tail is already present at this head...")
                                        break
                                else:
                                    break
                            else:
                                print("please enter a valid input...")

                        while True:
                            print("accepts values between 1 to 70")
                            tail = input("tail: ")

                            if tail.isdigit() and (int(tail) in range(1, 71)):
                                tail = int(tail)
                                if tail >= int(head):
                                    print("Tail can not be an equal or greater value than head...")
                                else:
                                    for snake in snakes:
                                        if snake.head == tail:
                                            print("A snake is already present at this tail..")
                                            break
                                        elif snake.tail == tail:
                                            print("A snake's tail is already present at this tail...")
                                            break
                                    else:
                                        break
                            else:
                                print("please enter a valid input...")

                        snake = Snake(int(head), int(tail))
                        snakes.append(snake)
                    break
                else:
                    print("please enter a valid input...")

            time.sleep(1)
            print("\n")
            for snake in snakes:
                print(f'snake[{snake.head}, {snake.tail}]')

        return snakes


    def configureLadders(self, snakes):
        ladders = []
        default_ladders = input("\ndo you want to set the ladders or do you want to use the game default?\npress 'y' to user default. ")

        if default_ladders.lower() == 'y':
            ladder1 = Ladder(42, 20)
            ladder2 = Ladder(58, 25)
            ladder3 = Ladder(79, 41)
            ladder4 = Ladder(95, 36)
            ladder5 = Ladder(71, 43)
            ladder6 = Ladder(20, 9)
            ladder7 = Ladder(48, 5)
            ladder8 = Ladder(94, 69)

            ladders = [ladder1, ladder2, ladder3, ladder4, ladder5, ladder6, ladder7, ladder8] 
            

        else:
            while True:
                no_of_ladders = input("How many ladders do you want to plant? (please input a value between 5 to 7)\n")

                if no_of_ladders.isdigit() and int(no_of_ladders) in [5, 6, 7]:
                    for i in range(1, int(no_of_ladders) + 1):
                        print(f"Please enter the values of ladder{i}")
                        while True:
                            print("accepts values between 20 to 97")
                            head = input("head: ")

                            if head.isdigit() and (int(head) in range(20, 98)):
                                head = int(head)
                                if self.snakeOverlap(head, snakes):
                                        print("A snake is present at this position...")
                                else:
                                    for ladder in ladders:
                                        if ladder.head == head:
                                            print("A ladder is already present at this head..")
                                            break
                                        elif ladder.tail == head:
                                            print("A ladder's tail is already present at this head...")
                                            break
                                        
                                    else:
                                        break
                            else:
                                print("please enter a valid input...")

                        while True:
                            print("accepts values between 1 to 70")
                            tail = input("tail: ")

                            if tail.isdigit() and (int(tail) in range(1, 71)):
                                tail = int(tail)
                                if tail >= int(head):
                                    print("Tail can not be an equal or greater value than head...")
                                elif game.snakeOverlap(tail, snakes):
                                    print("A snake is present at this postion...")
                                else:
                                    for ladder in ladders:
                                        if ladder.head == tail:
                                            print("A ladder is already present at this tail..")
                                            break
                                        elif ladder.tail == tail:
                                            print("A ladder's tail is already present at this tail...")
                                            break
                                    else:
                                        break
                            else:
                                print("please enter a valid input...")

                        ladder = Ladder(int(head), int(tail))
                        ladders.append(ladder)
                    break
                else:
                    print("please enter a valid input...")
            
            time.sleep(1)
            print("\n")
            for ladder in ladders:
                print(f'ladder[{ladder.head}, {ladder.tail}]')

        return ladders


if __name__ == "__main__":

    game = Game()
    board = Board()
    dice = Dice()

    # get the number of users playing
    players = game.usersPlaying()

    # configure snakes
    snakes = game.configureSnakes()

    # configure ladders
    ladders = game.configureLadders(snakes)
            
    while True:
        for player in players:
            time.sleep(1)
            print(f"\n{player.name}'s turn...")

            time.sleep(1)
            
            game.diceRoll(player, dice)

            game.checkSnake(player, snakes)

            game.checkLadder(player, ladders)

            game.checkPlayerOverlap(player, players, dice)

            # time.sleep(1)
            # print(f"{player.name}'s postion: {player.position}")

            player.getPosition()

            if game.has_won(player):
                # quit the game
                quit("Thank you for playing...")
