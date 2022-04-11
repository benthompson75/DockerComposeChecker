#!/usr/bin/python3

"""
This script will scan docker-compose.yml files in a path and check for basic settings, as well as output common "nice to know" items

TODO List - p = planned, i = in progress, c = completed, x = rejected
  c Check for Static things
  i Check for required Variable things
  i Check and Output all Variable things
  . Enable command line switches to only output specific things
  . Enable command line switch to check only specific file/dir
  . Create help output
  . Implement quiet/verbose output for static things

"""

# Import classes
# import os
# import glob
from pathlib import Path  # to get list of files
import re  # for regex searching
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
RESTART = "unless-stopped"
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
    restartfound = False
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

    # Check restart
    openfile.seek(0)  # reset to top of file
    for restartline in openfile:
        if re.search(RESTART, restartline):
            # print (line)
            restartfound = True
    if restartfound == False:
        print("No restart unless stopped defined!")

    # Find start of each section
    openfile.seek(0)  # reset to top of file
    openfiletxt = openfile.readlines()  # Read the whole file into 1 var
    # reset line counters
    sectionstart = 0
    sectionlinecount = 0
    for sectionline in openfiletxt:
        sectionlinecount = sectionlinecount + 1
        foundsection = re.search('[^:-].*?:\s*', sectionline)
        if foundsection:
            print(foundsection.group(0), sectionlinecount)
            # Add in if/elseif/elseif/else for wanted sections
            # Ports, Networks, Volumes, Environments




# Check for required varible stuff
    # Check ports
    openfile.seek(0)  # reset to top of file
    # reset line counters
    portlinecount = 0
    portlineinc = 0
    # Find start of ports section
    for portsline in openfile:
        portlinecount = portlinecount + 1
        section = re.search('[^:-].*?:\s*', portsline)
        if not isinstance(section, type(None)):
            print(section.group(0))
            if section.group(0).lstrip() == "ports:\n":
                portstart = portlinecount
                # Find start of next section
           if re.search('^\s+\w\:', portsline) and not re.search("ports:", portsline) and not re.search('\d+:\d+', portsline):
                portend = portlinecount
                print("junk")
                continue


# start_printing =0
# for line in AllLines
#    if line contains ^\s*\w+ -and start_printing -eq 1
#       start_printing = 0
#       break

#    if start_printing:
#        print_line()

#    if line contains ^\s+ports:
#    if line contains $\s+[environment|volumes|ports|networks]:$
#         start_printing = 1





        # Print all lines inbetween
    while portlineinc < portend:
        print(openfile)
        portlineinc = portlineinc + 1

    # Check for config volume



# Check and ouput additional variable stuff

    # Check all volumes


    # Check networks


    # Check environment vars




# Port check
# grep [[:digit:]]:[[:digit:]] ~/docker/*/docker-compose.yml
# grep "^\s+\-" ~/docker/metube/docker-compose.yml

# -T.
