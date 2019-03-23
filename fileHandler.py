"""
Made by Ryan Wilson
https://github.com/onlinePB

This class will be used for writing to files
"""
import csv


class FileHandler:

    """
    This method will take in a filename and an array of records, it will
    write each record as a line in the file.
    """
    @staticmethod
    def export(fileName, data):
        file = open(fileName + '.csv', 'w')
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(data)
        file.close()