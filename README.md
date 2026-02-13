# Swamp Sentinel 

An all-powerful toolset for Swamp.

Sentinel is an autonomous agent for persisting, processing and automating Swamp V2 governance objects and tasks.

Sentinel is implemented as a Python application that binds to a local version 2 swampd instance on each Swamp V2 Masternode.

This guide covers installing Sentinel onto an existing V2 Masternode for Debian 12+ and Ubuntu 23.03+ as Python 3.11+ is required.

## Installation

### 1. Install Prerequisites

Make sure Python version 3.11.x or above is installed:

    python3 --version

Update system packages and ensure virtualenv is installed:

    sudo apt-get update
    sudo apt-get -y install python3-venv git
    sudo apt install virtualenv

Make sure the local Swamp daemon running is at least version 2 (2000003)

    swamp-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    git clone https://github.com/Swampthing-SwampCoin/Sentinel-py3.git && cd Sentinel-py3
    virtualenv ./venv
    ./venv/bin/pip install -r requirements.txt

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    crontab -e

In the crontab editor, add the lines below, replacing '~/Sentinel-py3' to the path where you cloned sentinel to:

    * * * * * cd ~/Sentinel-py3 && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### 4. Test the Configuration

Test the config by runnings all tests from the sentinel folder you cloned into

    ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with swampd and the installation is complete

## Configuration

An alternative (non-default) path to the `swamp.conf` file can be specified in `sentinel.conf`:

    swamp_conf=/path/to/swamp.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py
