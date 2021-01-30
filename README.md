# IceGauntlet Authentication server

This is a IceGauntlet authentication server. This server is used by IceGauntlet Map Service to authenticate users.

## How to install

A dedicated *Python3 virtual environment* is recommended. To install dependencies in a virtual environment run:

```bash
pip install -r requeriments.txt
```
Also you can add _--user_ to install dependencies for your current user.

## How to run

Just run with:

```bash
./auth_server --Ice.Config=auth_server.conf
```
The _proxy_ will be shown in _stdout_. Also you can add users with:

```bash
./add_user <user_name>
```
The last command reload user database stored in *users.json*. Reloading the database is a _long time consuming task_ so this command should not be used in a production environment.

## Known problems

This authentication server *is not secure* because an attacker could capture authentication tokens and also password hashes to _spoof_ users. In order to make this server more secure, switch endpoint protocol to *ssl* and configure it properly.
