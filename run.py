import os, json, sys, requests
from datetime import datetime, timedelta
import confutil

# Logging
import logging
import logutil
logutil.initLog('watcher.log', logutil.MAIN_LOG_NAME, True)
logger = logging.getLogger(logutil.MAIN_LOG_NAME)

LOCATION = os.path.abspath(os.path.dirname(sys.argv[0]))
CONFIG = confutil.loadConfig(LOCATION + '/config.json')


if isinstance(CONFIG, int):
  sys.exit(0)

if not CONFIG.get('DeleteTime'):
  logger.error("DeleteTime key not available. Exitting...")
  sys.exit(0)

# Querying:
# Getting date DeleteTime days ago
DeleteTime = CONFIG.get("DeleteTime")
date = datetime.now() - timedelta(DeleteTime)

# Formatting into a string with YYYYMMDD
formattedDate = date.strftime('%Y%m%d')

# Getting response as json data list
resp = requests.post('http://localhost:8042/tools/find', json = {"Level":"Series","Query":{"StudyDate":"-"+formattedDate,"PatientID":"*"}})
respjson = resp.json()

# If we find any entries, delete them
if len(respjson) > 0:
  for seriesID in respjson:
    logger.warning("Deleting series " + seriesID)
    requests.delete('http://localhost:8042/series/' + seriesID)