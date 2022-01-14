#/bin/bash

# This script will scan docker-compose.yml files in a path and check for basic settings, as well as output common "nice to know" items

: <<'END_COMMENT'
TODO List
  . Check for Static things
  . Check for Variable things
  . Output all Variable things
  . Enable command line switches to only output specific things
  . Create help output

END_COMMENT

# Static things to check for
# PUID, GUID, TZ, UMASK, restart

# Variable things to check for and output
# volumes, ports, networks

# User Variables

# Parent docker compose directory
DOCKERDIR=/usr/local/docker
PUID=1000
PGID=995
TZ=America/New_York
UMASK_SET=022

COMPOSEFILES=`ls -r1 $DOCKERDIR/*/docker-compose.yml`

echo $COMPOSEFILES


# Port check
#grep [[:digit:]]:[[:digit:]] ~/docker/*/docker-compose.yml
#grep "^\s+\-" ~/docker/metube/docker-compose.yml

#-T.
