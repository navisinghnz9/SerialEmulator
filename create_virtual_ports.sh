#!/bin/bash


#######################################################################################
#
# Script to create virtual serial ports
#
#
# Linux/Mac:
#---------------------------------------------------------------------
# Use socat to create virtual serial ports.
# /tmp/ttyV0 is the port the emulator will listen on.
# /tmp/ttyV1 is the port the client will connect to and send packets.
#
#
# On Windows:
#---------------------------------------------------------------------
# Use com0com to create two virtual COM ports (e.g., COM5 and COM6).
# Install and configure com0com to create virtual COM ports.
#
#######################################################################################

# creating two virtual serial ports: /tmp/ttyV0 and /tmp/ttyV1
socat -d -d pty,link=/tmp/ttyV0 pty,link=/tmp/ttyV1

