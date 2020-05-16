import os

ABS_PATH = os.path.abspath(__file__) #path where conf.py is
BASE_DIR = os.path.dirname(ABS_PATH) #directory that it lives in

#path to directories that we just created
DATA_DIR = os.path.join(BASE_DIR, "data") 
SAMPLE_DIR = os.path.join(DATA_DIR, "samples")
SAMPLE_INPUTS = os.path.join(SAMPLE_DIR, "inputs")
SAMPLE_OUTPUTS = os.path.join(SAMPLE_DIR, 'outputs')