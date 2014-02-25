import sys
import csv
sys.path.append('../BusinesObjects/')
from RequestResult import RequestResult


class ResultParser:

    def __init__(self):
        return

    @staticmethod
    def ParseRequestFile(fileList):
        results = []

        if len(fileList) > 0:
            for fileName in fileList:
                with open(fileName) as fin:
                    csvin = csv.reader(fin)
                    next(csvin)
                    for row in csvin:
                        if row[1].lower() == 'post':
                            result = RequestResult(row[0], row[1], row[2], None, row[3], row[4])
                        else:
                            result = RequestResult(row[0], row[1], None, row[2], row[3], row[4])

                        results.append(result)
        return results


