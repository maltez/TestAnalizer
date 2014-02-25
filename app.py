import ConfigParser
import sys
from zipfile import ZipFile
sys.path.append('BusinesObjects/')
from RequestResult import RequestResult
sys.path.append('Workers/')
from DataParser import ResultParser
from GroupByUrl import GroupByUrl
from GroupByBodyParam import GroupByBodyParam
from ImportToText import ImportToText

# Prepare info from config
config = ConfigParser.RawConfigParser()
config.read('app.config')

# Unzip statistics files
zipFileArchive = ZipFile(config.get('Environment_Constants', 'ArchivePath'))
zipFileArchive.extractall(config.get('Environment_Constants', 'TemporaryFolder'))

# Get data from POST request statistic
paths = [config.get('Environment_Constants', 'SearchStatisticFileName'),
        config.get('Environment_Constants', 'MergeStatisticFileName'),
        config.get('Environment_Constants', 'MultiSearchStatisticFileName'),
        config.get('Environment_Constants', 'InitPopulationStatisticFileName')]

postResults = ResultParser.ParseRequestFile(paths)
groupedResults = GroupByUrl.grouped_by_url(postResults)
#paramGr = GroupByBodyParam.GroupByBodyParam(groupedResults)
ImportToText.import_report_to_text_file('Data\\report.txt', groupedResults)
ImportToText.import_report_to_json('Data\\report.json', groupedResults)
print(groupedResults[0])

#config.set('Environment_Constants', 'SearchStatisticFileName', 'Data\\performance_get_requests.csv')
#config.set('Environment_Constants', 'MergeStatisticFileName', 'Data\\Unziped\\Statistics\\megs_stats.csv')
#config.set('Environment_Constants', 'MultiSearchStatisticFileName', 'Data\\Unziped\\Statistics\\multitypesearch_stats.csv')
#config.set('Environment_Constants', 'InitPopulationStatisticFileName', 'Data\\Unziped\\Statistics\\es_initialpopulation_stats.csv')
#with open('app.config', 'wb') as configfile:
 #   config.write(configfile)