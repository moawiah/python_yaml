import yaml
import logging
import os
import sys
from power import Power2
from add import AD

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class System(yaml.YAMLObject):
    yaml_tag = '!system'

    def __init__(self):
        super().__init__()
        logging.info('Creating System...')
        self.inputs = []
        self.outputs = []
        self.algorithm = None
        self.modules = {}

    def listInputs(self):
        """ List the available inputs in the system """
        for item in self.inputs:
            logging.info('input: ' + item)
            
    def addInput(self, input_value):
        """ Adding an input to the system """
        self.inputs.append(input_value)
 
    def addModule(self, module, imp):
        """ Adding a module to the system """
        imps = []
        if module not in self.modules.keys():
            self.modules[module] = imp
        else:
            imps.append(self.modules[module])
            imps.append(imp)
            self.modules[module] = imps

    def listModules(self):
        logging.info(self.modules)

    def runSystem(self):
        """ Running the system after collecting and parsing YAML Data """
        needed_imps = []
        ## Get Chosen Implementations
        if self.algorithm == 'Pythagorean':
            for module in self.modules.keys():
                if module == "Power2":
                    needed_imps = self.modules[module]
        
        ## Apply needed implementations to inputs --> Run module with chosen implementation(s)
        for index, imp in enumerate(needed_imps):
            power2_obj = Power2(self.inputs[index])
            if imp == 'power_by_addition':
                self.outputs.append(power2_obj.power_by_addition())
            elif imp == 'power_by_self_mul':
                self.outputs.append(power2_obj.power_by_self_mul())
        
        ## Get final addition output --> Run the final module
        for module in self.modules.keys():
                if module == "add":
                    needed_imps = self.modules[module]
                if needed_imps == 'normal_add':
                    add_obj = AD(self.outputs[0],self.outputs[1])
                    logging.info('Final Result: '+ str(add_obj.normal_add()))

    @classmethod
    def to_yaml(cls, dumper, data):
        dict_modules = {}
        for key, value in data.modules.items():
            dict_modules[str(key)] = value
        dict_representation = {
            'modules' : dict_modules,
            'inputs' : data.inputs,
            'algorithm': data.algorithm
        }
        return dumper.represent_mapping(cls.yaml_tag, dict_representation)  

    @classmethod
    def from_yaml(cls, loader, node): ## A function to parse our YAML configuration
        data = System()
        for n in node.value :
            s = loader.construct_scalar(n[0]) # Get the mapping name
            if s == 'modules':
                        for m in n[1].value:
                            module = loader.construct_scalar(m[0])
                            if isinstance(m[1], yaml.nodes.SequenceNode):
                                for item in m[1].value:
                                    imp = loader.construct_scalar(item)
                                    data.addModule(str(module),str(imp))
                            else:
                                imp = loader.construct_scalar(m[1])
                                data.addModule(str(module),str(imp))
            elif s == 'algorithm':
                data.algorithm = str(n[1].value)
            elif s == 'inputs':
                for m in n[1].value:
                            input_value = loader.construct_scalar(m[0])
                            data.addInput(input_value)
        return data