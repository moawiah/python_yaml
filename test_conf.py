import sys
import time
import yaml
import os
import logging
from power import Power2
from system import System
from add import ADD

## Logging Level Configuration
logging.basicConfig(level=logging.INFO)

## Obtaining Configuration Path as an argument
if len(sys.argv) > 1:
	configuration_path = sys.argv[1]
else:
    logging.error('No system specification provided, system will be empty')
    sys.exit(0)
logging.info('Loading config from {}'.format(configuration_path))

## Using YAML loader to get 
try:
	with open(configuration_path, 'r') as conf:
		sys = yaml.load(conf, Loader=yaml.Loader)
except Exception as e :
	print(e)

## Ability to list Inputs and Modules as parsed by conf. file
#sys.listInputs() 
#sys.listModules()

## Running the modules based on the configuration file
sys.runSystem()

