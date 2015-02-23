#!/bin/bash

# This is a helper script to ensure fig commands
# are run with the necessary environment variables
# set when run via "sudo"

source ENVVAR
fig restart $1
