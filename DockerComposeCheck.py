#!/usr/bin/python3

"""
This script will scan docker-compose.yml files in a path and check for basic settings, as well as output common "nice to know" items

TODO List - p = planned, i = in progress, c = completed, x = rejected
  c Check for Static things
  . Check for Variable things
  . Output all Variable things
  . Enable command line switches to only output specific things
  . Enable command line switch to check only specific file/dir
  . Create help output
  . Implement quiet/verbose output for static things

"""

# Import classes
# import os
# import glob
from pathlib import Path  # to get list of files
import re  # for searching
import sys  # to open the files
import fnmatch  # to match filenames

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
for cfile in composefiles:
    # Re-init found vars for each loop
    puidfound = False
    pgidfound = False
    tzfound = False
    umaskfound = False
    print("\nNow inspecting ", cfile)
    openfile = open(cfile, "r")  # open the file for reading

    # Check PUID
    for puidline in openfile:
        if re.search(PUID, puidline):
            # print (line)
            puidfound = True
    if puidfound == False:
        print("No PUID defined!")

    # Check PGID
    openfile.seek(0)  # reset to top of file
    for pgidline in openfile:
        if re.search(PGID, pgidline):
            # print (line)
            pgidfound = True
    if pgidfound == False:
        print("No PGID defined!")

    # Check TZ
    openfile.seek(0)  # reset to top of file
    for tzline in openfile:
        if re.search(TZ, tzline):
            # print (line)
            tzfound = True
    if tzfound == False:
        print("No TZ defined!")

# Check UMASK - if not present, ignore
    openfile.seek(0)  # reset to top of file
    for umaskline in openfile:
        if re.search(UMASK_SET, umaskline):
            # print (line)
            umaskfound = True
    if umaskfound == False:
        print("No UMASK_SET defined! (Optional)")


# Port check
# grep [[:digit:]]:[[:digit:]] ~/docker/*/docker-compose.yml
# grep "^\s+\-" ~/docker/metube/docker-compose.yml

# -T.
