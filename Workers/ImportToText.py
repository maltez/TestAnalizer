__author__ = 'nickolay.lototskiy'
import json


class ImportToText:
    def __init__(self):
        pass

    @staticmethod
    def import_report_to_text_file(path, report_list):
        report_file = open(path, 'w')
        report_file.write("---------------------------------------Test Result---------------------------------------")
        report_file.write("\n\n")
        count = 1
        for item in report_list:
            report_file.write(
                str(count) + ') ' + str(item) + ' max: ' + str(item.get_maximum) + ' min: ' + str(item.get_minimum) + ' median: ' + str(item.get_median))
            report_file.write('\n')
            count += 1

        report_file.close()

    @staticmethod
    def import_report_to_json(path, report_list):
        report_file = open(path, 'w')
        json.dump([rep.to_json() for rep in report_list], report_file, indent=4)
        report_file.close()