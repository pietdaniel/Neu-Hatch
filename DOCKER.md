# Running the Docker Environment

## Requirements

* `ENVVAR` file in root of repo

## Process

### 1. Install [Docker](https://www.docker.com)

OS X users will also need VirtualBox installed

### 2. Install [Fig](http://www.fig.sh)

### 3. Start Docker daemon

#### Arch
* `sudo systemctl start docker`
* You can avoid needing to prefix `docker`/`fig` commands with `sudo`
by adding yourself to the `docker` group with `sudo gpasswd -a <user> docker`
and then logging out and back in.

#### OS X
* `boot2docker init` (only needed once)
* `boot2docker start` (starts the VM)
* `$(boot2docker shellinit)` (sets necessary environment variables, will
want to add this to your shell profile/rc file)

#### Verify Docker is running

* (OS X only) `boot2docker status`
* `[sudo] docker version`
* `[sudo] docker run hello-world`
* `[sudo] fig --version`

### 4. Build containers

Run `[sudo] fig build`

### 5. Start containers

#### NOTE: MAKE SURE YOU SOURCE `ENVVAR` BEFORE RUNNING 

#### NOTE

You'll need to rename the folder this repo is in from `Neu-Hatch`
to `hatch` or something, [Docker doesn't allow capital letters in container
names](https://github.com/docker/fig/issues/655)

Alternatively, you can add an alias for fig or export an environment variable:
* `alias fig='fig -p hatch'`
*`export FIG_PROJECT_NAME="hatch"`

#### OS X:

`source ENVVAR` and then run `fig up`

#### Arch:
`source ENVVAR` and then run `[sudo] fig up`. 
* If you're not part of the `docker` group, you'll need to prefix the
commands with `sudo`. Since some of the environment variables in the
`fig.yml` are sourced from the host that `fig` is running on, you'll
need to use a small helper script that you can use `sudo` with that
will source your `ENVVAR` file and then run `fig up`

### 6 The Hatch backend should now be running and available at:

* Arch: `localhost:5000`
* OS X: `$(boot2docker ip):5000`

# Making Changes

If you make changes to the code, they should be detected automatically
and get reloaded live if the environment is running in the background.

## IF YOU MAKE CHANGES TO THE DATA MODEL

You'll need to write a new alembic migration for the change and add it to
the migrations folder. See the alembic documentation for more information.

# TODO
* SSL certificates
* Production-ize fig environment (e.g through some `fig-prod.yml`)
* Audit configuration for security (i.e. no ports exposed unecessarily)
