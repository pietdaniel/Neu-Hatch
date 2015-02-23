# Running the Docker Environment

## Requirements

* ENVVAR file in root of repo

### Process

1. Install [Docker](https://www.docker.com)
    * OS X: Will also need VirtualBox
2. Install [Fig](http://www.fig.sh)
3. Start Docker daemon
    * Arch:
        - `sudo systemctl start docker`
        - You can avoid needing to prefix `docker`/`fig` commands with `sudo`
        by adding yourself to the `docker` group with
        `sudo gpasswd -a <user> docker` and then logging out and back in.
    * OS X:
        - `boot2docker init` (only needed once)
        - `boot2docker start` (starts the VM)
        - `$(boot2docker shellinit)` (sets necessary environment variables, will
        want to add this to your shell profile/rc file)
    * verify working by running:
        - OS X: `boot2docker status`
        - `[sudo] docker version`
        - `[sudo] docker run hello-world`
        - `[sudo] fig --version`
4. Build containers
    * run `[sudo] fig build`
5. Start containers
    * Create a symlink to `fig.yml` from the corresponding platform-specific
    fig file
        - Arch: `ln -s fig.linux.yml fig.yml`
        - OS X: `ln -s fig.osx.yml fig.yml`
    * NOTE: You'll need to rename the folder this repo is in from `Neu-Hatch`
    to `hatch` or something, [Docker doesn't allow capital letters in container
    names](https://github.com/docker/fig/issues/655)
        - alternatively, you could prefix each `fig` command with `-p hatch`,
          but will get annoying.
    * OS X:
        - `source ENVVAR`
        - run `fig up`
    * Arch:
        - run `[sudo] fig up`
        - If you're not part of the `docker` group, you'll need to prefix the
        commands with `sudo`. Since some of the environment variables in the
        `fig.yml` are sourced from the host that `fig` is running on, you'll
        need to use a small helper script that you can use `sudo` with that
        will source your `ENVVAR` file and then run `fig up`
6. If this was your first time building the DB container, you'll need to run:
    * TODO: Figure out which of these can be moved into the container build step
    * `fig run server python manage.py db init`
    * `fig run server python manage.py db migrate`
    * `fig run server python manage.py db upgrade`
7. The Hatch backend should now be running and available at:
    * Arch: `localhost:5000`
    * OS X: `$(boot2docker ip):5000`

# Making Changes

## Backend (db and server)

* TODO: figure out process involved with data-only container holding postgres
data.

If you make changes to the back end code, it's easiest to do the following:

1. Run `fig stop` or press `Ctrl+C` in the terminal window where `fig` is
running to stop the containers.
2. Run `fig rm` to remove the old containers
3. Run `fig build` to build new containers with the latest changes
4. Run `fig up`. You will need to re-run the database migrations (`migrate`
and `upgrade`, `init` most likely will not need to be run).


## Client

### This is out dated as the client is moving to a separate repo

If you have the collection of containers running (`db`, `server`, `client`),
and want to test your changes to the client code, you should do the following:

1. Open a new terminal / session in the same directory as this repo
2. Make your changes (they may already have been made)
3. Run `fig stop client` to stop the existing `client` container
4. Run `fig rm client` to remove the existing `client` container
5. Run `fig build client` to create a new `client` container with your most
recent changes.
6. Run `fig up client` to start the `client` container

# TODO

* figure out how to avoid publishing ports `5432` and `5000` through container
linking
* DATABASE PERSISTENCE
    - Will involve some container that simply mounts/provides a volume where
    the database will live.
* SSL certificates
* Audit configuration for security (i.e. no ports exposed unecessarily)
* figure out production deployment
    - In theory should be simple matter of bringing up a server with Docker and
    Fig installed, cloning this repo, and running `fig up`
