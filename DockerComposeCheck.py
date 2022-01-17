#!/usr/bin/python3

"""
This script will scan docker-compose.yml files in a path and check for basic settings, as well as output common "nice to know" items

TODO List - p = planned, i = in progress, c = completed, x = rejected
  i Check for Static things
  . Check for Variable things
  . Output all Variable things
  . Enable command line switches to only output specific things
  . Create help output
  . Implement quiet/verbose output for static things

"""

# Import classes
#import os
#import glob
from pathlib import Path # to get list of files
import re # for searching
import sys # to open the files
import fnmatch # to match filenames

# Static things to check for
# PUID, GUID, TZ, UMASK, restart

# Variable things to check for and output
# volumes, ports, networks

# User Variables
# Parent docker compose directory
dockerdir = "/usr/local/docker"
PUID = "1000"
PGID = "995"
TZ = "America/New_York"
UMASK_SET = "022"
# Ignore "example" docker-compose files
ignoreexample = True



# Get list of docker-compose.yml files
composefiles = []
for file_path in Path(dockerdir).glob('**/docker-compose.yml'):
    if fnmatch.fnmatch(file_path, '*example*'):
      if ignoreexample == True:
        continue
    else:
      composefiles.append(file_path)
    # Start looping through and checking things
    #### Right now this is looping multiple times and I don't know why yet.
    #### I've confirmed that composefiles is only a single list of the files found
    for cfile in composefiles:
      # Re-init found vars for each loop
      puidfound = False
      guidfound = False
      tzfound = False
      umaskfound = False
      print("Now inspecting ",cfile)
      openfile = open(cfile, "r") # open the file for reading
      # Check PUID
      for line in openfile:
        if re.search(PUID, line):
          #print (line)
          puidfound = True
      if puidfound == False:
        print ("No PUID defined!")
  
  
  # Check GUID
  
  # Check TZ
  
  # Check UMASK - if not present, ignore
  

# Port check
#grep [[:digit:]]:[[:digit:]] ~/docker/*/docker-compose.yml
#grep "^\s+\-" ~/docker/metube/docker-compose.yml

#-T.


