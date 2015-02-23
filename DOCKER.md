# Running the Docker Environment

1. Install [Docker](https://www.docker.com)
2. Install [Fig](http://www.fig.sh)
3. Start Docker daemon
    * Arch:
        - `sudo systemctl start docker`
        - You can avoid needing to prefix `docker`/`fig` commands with `sudo`
        by adding yourself to the `docker` group with
        `sudo gpasswd -a <user> docker` and then logging out and back in.
    * OS X:
        - Unsure off top of my head, something to do with `boot2docker`
4. Start containers
    * NOTE: You'll need to rename the folder this repo is in from `Neu-Hatch`
    to `hatch` or something, [Docker doesn't allow capital letters in container
    names](https://github.com/docker/fig/issues/655)
    * Arch:
        - If you're not part of the `docker` group, you'll need to prefix the
        commands with `sudo`. Since some of the environment variables in the
        `fig.yml` are sourced from the host that `fig` is running on, you'll
        need to use a small helper script that you can use `sudo` with that
        will source your `ENVVAR` file and then run `fig up`
5. If this was your first time building the DB container, you'll need to run:
    * `fig run server python manage.py db init`
    * `fig run server python manage.py db migrate`
    * `fig run server python manage.py db upgrade`
6. You will now be able to view Hatch by visiting `localhost:8000` in your
web browser. OAuth v1 is believed to be working

# Making Changes

## Client

If you have the collection of containers running (`db`, `server`, `client`),
and want to test your changes to the client code, you should do the following:

1. Open a new terminal / session in the same directory as this repo
2. Make your changes (they may already have been made)
3. Run `fig stop client` to stop the existing `client` container
4. Run `fig rm client` to remove the existing `client` container
5. Run `fig build client` to create a new `client` container with your most
recent changes.
6. Run `fig up client` to start the `client` container

## Backend (db and server)

If you make changes to the back end code, it's easiest to do the following:

1. Run `fig stop` or press `Ctrl+C` in the terminal window where `fig` is
running to stop the containers.
2. Run `fig rm` to remove the old containers
3. Run `fig build` to build new containers with the latest changes
4. Run `fig up`. You will need to re-run the database migrations (`migrate`
and `upgrade`, `init` most likely will not need to be run).

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
