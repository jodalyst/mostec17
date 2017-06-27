# mites17

This repository is the operational distribution for the MITES and MOSTEC 2017 Raspberry Pi's to hook into the currently-existing hardware manager (separate repo <a href="https://github.com/jodalyst/hardware_synchronizer" target="_blank">here</a>  which itself hooks into the online learning platform <a href="https://cat-soop.org/website">CAT-SOOP</a>
files for mites raspberry pi's

## Quick Setup:
This repo should live in the `pi` user's home directory.  Inside of the repo is a hidden file called `catsoop_login` that must have the user's credentials entered like so:

```
user
password
```

Code was written assuming >Python3.4, so no promises if it doesn't work on earlier versions. No non-standard libraries are needed. One-time use of the code can be started simply by running the program with Python.  

For more standard operation, so that it is always running, we'll use `systemd/systemctl`.  First cp the file `pyrunner.service` file into `/lib/systemd/system/`.  Then give proper permissions with the following command (we'll call it `pyrunner`, but you can call it whatever)

```
sudo chmod 644 /lib/systemd/system/pyrunner.service
```

Then turn on daemon-reload:

```
sudo systemctl daemon-reload
```

Then enable the service:

```
sudo systemctl enable pyrunner.service
```

Then you might as well reboot:

```
sudo reboot
```

When the computer comes back, check to see if stuff is running. No errors is a good thing:

```
sudo systemctl status pyrunner.service
```

There's a `audio` directory where example files will live

