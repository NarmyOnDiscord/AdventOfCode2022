# Rock Paper Scissors
# https://adventofcode.com/2022/day/2

from enum import Enum

class Result(Enum):
    win = 6
    draw = 3
    loose = 0

class Move(Enum):
    rock = 1 # Rock
    paper = 2 # Paper
    scissors = 3 # Scissors

total_points = 0

input_ = open("Day 2/input.txt", "r")
for line, content in enumerate(input_, 1):
    content = content.removesuffix("\n")
    enemy_play, _, needed_outcome = content.partition(" ")

    match needed_outcome:
        case "X": # Loose
            total_points += Result.loose.value

            match enemy_play:
                case "A":
                    total_points += Move.scissors.value
                case "B":
                    total_points += Move.rock.value
                case "C":
                    total_points += Move.paper.value

        case "Y": # Draw
            total_points += Result.draw.value

            match enemy_play:
                case "A":
                    total_points += Move.rock.value
                case "B":
                    total_points += Move.paper.value
                case "C":
                    total_points += Move.scissors.value
                    
        case "Z": # Win
            total_points += Result.win.value

            match enemy_play:
                case "A":
                    total_points += Move.paper.value
                case "B":
                    total_points += Move.scissors.value
                case "C":
                    total_points += Move.rock.value

print(total_points)