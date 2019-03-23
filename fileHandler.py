import csv


class FileHandler:

    @staticmethod
    def export(fileName, data):
        file = open(fileName + '.csv', 'w')
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(data)
        file.close()