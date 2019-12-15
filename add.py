import yaml
import logging
import os
import sys

class AD(yaml.YAMLObject):
    yaml_tag = '!add'

    def __init__(self, input_value_1, input_value_2):
        super().__init__()
        self.input_value_1 = input_value_1
        self.input_value_2 = input_value_2


    def normal_add(self):
        logging.info('Normal addition implementation is used for Out1: ' + str(self.input_value_1) + ' and Out2: ' + str(self.input_value_2))
        out = self.input_value_1 + self.input_value_2
        return out
