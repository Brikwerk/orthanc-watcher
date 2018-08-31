import json, os, sys

# Logging
import logging
import logutil
logger = logging.getLogger(logutil.MAIN_LOG_NAME)

# Constants
DEFAULT_CONFIG = {
  "DeleteTime" : 30
}


# Attempts to load json config named/specced from path
# Returns the JSON config or -1 (Bad validation)
def loadConfig(path):
  CONFIG = openConfig(path)
  if CONFIG == -1:
    return CONFIG
  elif CONFIG == 0:
    createConfig(path)
    return CONFIG
  
  return CONFIG


def openConfig(path):
  CONFIG = None
  try:
    with open(path) as f: # Attempt to load the config file
      CONFIG = json.load(f)
      f.close()
  except FileNotFoundError: # If the file cannot be found, return 0
    return 0
  except json.decoder.JSONDecodeError:
    logger.error("Config file could not be decoded. Please provide a valid JSON file.")
    return -1
  
  return CONFIG

def createConfig(path):
  logger.error("Creating config...")
  try:
    with open(path, 'w') as outfile:
      json.dump(DEFAULT_CONFIG, outfile, indent=2)
      outfile.close()
  except FileNotFoundError:
    logger.error("Could not create config. The path specified is inavlid")
    return -1
  
  logger.error("Config file was created. Please fill it out with your settings.")