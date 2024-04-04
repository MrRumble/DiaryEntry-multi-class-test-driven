from lib.diary import *

def test_diary_initialised():
    diary = Diary()
    result = diary.entries
    assert result == []
