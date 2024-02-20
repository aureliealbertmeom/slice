#! /usr/bin/env python

"""
This is an example dataset definition
=====================================
This is where the user defines what he/she wants to extract and where
A beginner user may look at the params.py file to see what is available and where
An advanced user modifies params.py file to match their needs
Written in 2024-01-19 by Aurelie Albert aurelie.albert@univ-grenoble-alpes.fr
"""

# Machine where the extration is done and hopefully the raw data are stored
# It can be only one above adastra, jean-zay, irene
machine='adastra'

# Name of the configuration
# It must be one of the configuration outputs stored on the above machine
configuration='eNATL60'

# Name of the simulation, experiment or run
# It must be one of the simulations for the above configuration stored on the above machine
simulations=['BLB002']

# Name of the regions considered for extraction
# It must have been defined for the selected configuration
regions=['eNATL60']

# Name of the variables considered for extraction
# It must be in the list of acceptable variables
variables=['SST']

# Frequency of the output
# It must be compatible for the simulation and variable
frequency='1h'

# Extra operation after extraction of raw outputs
operation='1d-mean'

# Period of the extraction
# Must be in the format yyyy-mm-dd
date_init='2009-07-01'
date_end='2010-06-30'


