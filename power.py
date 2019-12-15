import yaml
import logging
import os
import sys

class Power2(yaml.YAMLObject):
    yaml_tag = '!power'

    def __init__(self, input_value):
        super().__init__()
        self.input_value = input_value

    def power_by_addition(self):
        logging.info('Power by addition implementation is used for input value: '+ str(self.input_value))
        out = 0
        for i in range(0,int(self.input_value)):
            out = out + int(self.input_value)

        return out

    def power_by_self_mul(self):
        logging.info('Power by multiplication implementation is used for input value: '+ str(self.input_value))
        out = int(self.input_value) * int(self.input_value)
        return out
