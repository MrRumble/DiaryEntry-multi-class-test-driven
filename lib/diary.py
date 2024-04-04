from lib.diary_entry import *
import math

class Diary(DiaryEntry):
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries

    def count_words(self):
        total_word_count = 0
        for entry in self.entries:
            total_word_count += entry.count_words()
            
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        return total_word_count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total_world_count = self.count_words()
        return round(total_world_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        target_word_amount_in_entry = wpm * minutes
        readable_entries = []
        for entry in self.entries:
            if entry.count_words() <= target_word_amount_in_entry:
                readable_entries.append(entry)
            
            


            
        return self.entries[0]


