import sys
import inspect
import re
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2024\\')
from helper import loadingUtils, pretty

DAY = 2
def get_path():
    return "day{:02d}".format(DAY)

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

class SingleDraw:
    def __init__(self, in_red=0, in_green=0, in_blue=0) -> None:
        self.red = in_red
        self.green = in_green
        self.blue = in_blue
    
    def add_blue(self, num: int):
        self.blue = num
    
    def add_green(self, num: int):
        self.green = num
    
    def add_red(self, num: int):
        self.red = num

    def __repr__(self) -> str:
        return f"r{self.red} g{self.green} b{self.blue}"

class GameDraw:
    def __init__(self, id: int) -> None:
        self.game_id = id
        self.draws: list[SingleDraw] = []

    def add_draw(self, draw: SingleDraw) -> None:
        self.draws.append(draw)
    
    def valid(self) -> bool:
        valid = True
        for draw in self.draws:
            if draw.green > MAX_GREEN:
                valid = False
                return valid
            if draw.red > MAX_RED:
                valid = False
                return valid
            if draw.blue > MAX_BLUE:
                valid = False
                return valid
        return valid
    
    def get_minimun(self) -> int:
        min_blue = 0
        min_red = 0
        min_green = 0
        for draw in self.draws:
            if draw.blue > min_blue:
                min_blue = draw.blue
            if draw.red > min_red:
                min_red = draw.red
            if draw.green > min_green:
                min_green = draw.green
        return min_green * min_blue * min_red

def parse_line(line: str, debug = False) -> GameDraw:
    # first_split = line.split(":")
    first_split = re.split(":|;", line)
    # print(first_split)
    game_id = int(first_split[0].split(" ")[-1])
    game = GameDraw(id=game_id)
    for draw_line in first_split[1:]:
        # print(draw_line)
        balls = draw_line.split(",")
        draw = SingleDraw()
        # print(balls)
        for ball in balls: 
            # parse balls
            num, col = ball.strip().split(" ")
            if col == "red":
                draw.add_red(int(num))
            elif col == "blue":
                draw.add_blue(int(num))
            elif col == "green":
                draw.add_green(int(num))
            else:
                print(f"unknown color {col}")
        # add draw to game
        game.add_draw(draw)
    if debug: print(f"game_id {game.game_id}: draws = {game.draws}")
    return game

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    # code here
    lines = loadingUtils.importToArray(in_file)
    for line in lines:
        game = parse_line(line, debug)
        if game.valid():
            if debug: print(f"game {game.game_id} valid !!!! ")
            result = result + game.game_id

    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    # code here
    lines = loadingUtils.importToArray(in_file)
    for line in lines:
        game = parse_line(line, debug)
        result += game.get_minimun()
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
