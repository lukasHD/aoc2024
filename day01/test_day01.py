import day01 as day

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 142


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input")
    assert result == 55621


def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test2")
    assert result == 281


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input")
    assert result == 53592
