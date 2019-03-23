import csv

"""
This class will be used for writing to files
"""


class FileHandler:

    """
    This method will take in a filename and an array of records, it will
    write to a csv file
    """
    @staticmethod
    def export(fileName, data):
        file = open(fileName + '.csv', 'w')
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(data)
        file.close()