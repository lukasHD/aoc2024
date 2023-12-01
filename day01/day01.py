import sys
import inspect
import re
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 1
def get_path():
    return "day{:02d}".format(DAY)

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    # code here
    arr = loadingUtils.importToArray(in_file)

    if debug: print(arr)
    numbers = []
    for line in arr:
        for char in line:
            try:
                first = int(char)
            except ValueError:
                continue
            break
        for char in reversed(line):
            try:
                last = int(char)
            except ValueError:
                continue
            break
        combined = int(str(first) + str(last))
        numbers.append(combined)
        if debug: print(f"first = {first}; last = {last}; combined = {combined}")
    result = sum(numbers)
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0

    arr = loadingUtils.importToArray(in_file)
    allowed_keys = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    joined = "|".join(allowed_keys.keys())
    restring = r"(?=("+ joined + "))"
    print(restring)
    pattern = re.compile(restring)
    intermediate_results = []
    for line in arr:
        matches = pattern.findall(line)
        numbers = [allowed_keys[x] for x in matches]
        first = numbers[0]
        last = numbers[-1]
        line_result = int(str(first) + str(last))
        intermediate_results.append(line_result)
        if debug: print(f"{matches} ==> {numbers} ==> {line_result}")
    # code here
    result = sum(intermediate_results)
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input")
    run_part_2(get_path() + "/test2", True)
    run_part_2(get_path() + "/input")
