from lib.diary import *
from lib.diary_entry import *

#Test to see if I can add two diary entries and list them back

def test_adds_and_lists_two_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1', 'Contents 1')
    entry2 = DiaryEntry('Entry 2', 'Contents 2')
    diary.add(entry1)
    diary.add(entry2)
    result = diary.all()
    assert result == [entry1, entry2]

def test_count_all_diary_entry_words_correct_with_two_entries():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1', 'Contents 1')
    entry2 = DiaryEntry('Entry 2', 'Contents 2')
    diary.add(entry1)
    diary.add(entry2)
    result = diary.count_words()
    assert result == 4

def test_count_all_diary_entry_words_correct_with_multiple_entries():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1', 'Contents 1')
    entry2 = DiaryEntry('Entry 2', 'Contents 2')
    entry3 = DiaryEntry('Entry 3', 'Contents 3 with some extra words')
    entry4 = DiaryEntry('Entry 4', 'Contents 4 with even more extra words.')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.add(entry4)
    result = diary.count_words()
    assert result == 17

def test_reading_time_for_two_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1', 'Contents 1')
    entry2 = DiaryEntry('Entry 2', 'Contents 2')
    diary.add(entry1)
    diary.add(entry2)
    result = diary.reading_time(1)
    assert result == 4 

def test_reading_time_for_two_diary_entries_differnt_wpm():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1', 'Contents 1 hello')
    entry2 = DiaryEntry('Entry 2', 'Contents 2 hello')
    diary.add(entry1)
    diary.add(entry2)
    result = diary.reading_time(6)
    assert result == 1

def test_find_best_entry_for_reading_time_one_entry():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1', 'Contents 1')
    diary.add(entry1)
    result = diary.find_best_entry_for_reading_time(1,5)
    assert result == entry1

def test_find_best_entry_for_reading_time_two_entries():
    diary = Diary()
    longer_string = " ". join(['Word' for i in range(50)])
    entry1 = DiaryEntry('Entry 1', 'Contents 1')
    entry2 = DiaryEntry('Entry 1', longer_string)
    diary.add(entry2)
    diary.add(entry1)
    result = diary.find_best_entry_for_reading_time(10, 5)
    assert result == entry2