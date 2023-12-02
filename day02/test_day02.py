import day02 as day

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 8


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 2149


def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 2286


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 71274
