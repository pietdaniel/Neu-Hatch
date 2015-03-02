# Deploying Hatch API

The below describes how to deploy the latest version of hte master
branch of this repo to the Hatch staging server.

## Requirements

* [Fabric](fabfile.org) - `pip install fabric`
* Sent your SSH public key to Isaac
* Have exported the following environment variable:
`HATCH_API_URL="<user>@<host>:<port>"`. Ask Isaac for
the specific details.

## Steps

* Push your changes to github and run:

`fa
