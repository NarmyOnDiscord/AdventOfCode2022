# Rock Paper Scissors
# https://adventofcode.com/2022/day/2

from enum import Enum

class Result(Enum):
    win = 6
    draw = 3
    loose = 0

class MovePoints(Enum):
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissors

total_points = 0

input_ = open("Day 2/input.txt", "r")
for line, content in enumerate(input_, 1):
    content = content.removesuffix("\n")
    enemy_play, _, my_play = content.partition(" ")

    match my_play:
        case "X": # Rock
            total_points += MovePoints.X.value

            match enemy_play:
                case "A":
                    total_points += Result.draw.value
                case "B":
                    total_points += Result.loose.value
                case "C":
                    total_points += Result.win.value

        case "Y": # Paper
            total_points += MovePoints.Y.value

            match enemy_play:
                case "A":
                    total_points += Result.win.value
                case "B":
                    total_points += Result.draw.value
                case "C":
                    total_points += Result.loose.value
        case "Z":
            total_points += MovePoints.Z.value

            match enemy_play:
                case "A":
                    total_points += Result.loose.value
                case "B":
                    total_points += Result.win.value
                case "C":
                    total_points += Result.draw.value

print(total_points)