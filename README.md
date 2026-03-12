## 🛡️ Swamp Sentinel

**The autonomous heartbeat of Swamp V2 Masternodes.**

Sentinel is an autonomous agent designed to persist, process, and automate Swamp V2 governance objects and tasks. It runs as a Python application, binding locally to a `swampd` instance on each Masternode.

---

## 📋 Prerequisites

Before installing, ensure your environment meets the following requirements:

* **OS:** Debian 12+, Ubuntu 23.04+, or CentOS/RHEL 9+
* **Python:** Version 3.11.x or higher
* **Swamp Daemon:** `swampd` version 2 (2000003) or higher

### Verify Requirements
```bash
# Check Python version
python3 --version

# Check Swamp version
swamp-cli getinfo | grep version
```

---

## 🚀 Installation & Setup

Choose the section that matches your environment. Ensure you are logged in as the user intended to run the Masternode (e.g., `root` or a dedicated service user).

### Option A: Debian / Ubuntu (with sudo)
*Recommended for most standard VPS setups.*
```bash
sudo apt-get update
sudo apt-get -y install python3-venv git virtualenv
git clone https://github.com/Swampthing-SwampCoin/Sentinel-py3.git ~/Sentinel-py3
cd ~/Sentinel-py3
virtualenv ./venv
./venv/bin/pip install -r requirements.txt
```

### Option B: Debian / Ubuntu (Root)
```bash
apt-get update
apt-get -y install python3-venv git virtualenv
git clone https://github.com/Swampthing-SwampCoin/Sentinel-py3.git ~/Sentinel-py3
cd ~/Sentinel-py3
virtualenv ./venv
./venv/bin/pip install -r requirements.txt
```

### Option C: CentOS / RHEL / AlmaLinux
*Tested on Enterprise Linux 9+ (uses `dnf`).*
```bash
sudo dnf install -y python3 git
git clone https://github.com/Swampthing-SwampCoin/Sentinel-py3.git ~/Sentinel-py3
cd ~/Sentinel-py3
python3 -m venv venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt
```

---

## ⏰ Automation (Cron Setup)

Sentinel must run every minute to maintain the Masternode state. We use the `~/` pathing to ensure it works for both root and standard users.

1. Open the cron editor:
   ```bash
   crontab -e
   ```
2. Append the following line to the file (ensure there is a newline at the end):
   ```cron
   * * * * * cd ~/Sentinel-py3 && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1
   ```
   > **Pro Tip:** If your specific cron environment doesn't resolve `~/`, replace it with the full path (e.g., `/home/username/Sentinel-py3` or `/root/Sentinel-py3`).

---

## 🧪 Verification

After installation, verify that Sentinel can communicate with your local `swampd` instance:

| Step | Command |
| :--- | :--- |
| **1. Run Tests** | `./venv/bin/py.test ./test` |
| **2. Manual Debug** | `SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py` |

**Expected Result:** The manual check should output the current status of the Swamp network and confirm it is synced with your local daemon.

---

## ⚙️ Configuration

By default, Sentinel looks for `swamp.conf` in the standard data directory. If you use a non-default path, edit `sentinel.conf`:

```ini
# sentinel.conf
swamp_conf=/path/to/your/custom/swamp.conf
```

---

## 🛠️ Troubleshooting

If you encounter issues, run the script manually with the debug flag enabled to see the raw output:

```bash
SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py
