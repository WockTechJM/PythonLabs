# PythonLabs Notes

**Objective:**  
Practice basic Python scripting on Mac, learn how to use virtual environments, input/output, and log outputs to a file.

---

## What I Did

1. Created a folder called `PythonLabs`.
2. Set up a Python virtual environment (`venv`) in the folder.
3. Created my first Python script `test.py`.
4. Practiced:
   - `print()` to display output
   - `input()` to accept user input
   - Variables and strings
5. Ran the script in VS Code terminal with virtual environment activated.
6. Logged outputs to `command_log.txt`.

---

## Observations

- The `(venv)` in the terminal prompt indicates the virtual environment is active.
- Using `input()` pauses the script until I type something, then continues execution.
- Output can be logged to a file using Python for later reference.
- Running scripts in VS Code terminal is straightforward once the virtual environment is active.

---

## Next Steps

- Practice lists, loops, and conditionals.
- Start creating functions.
- Organize scripts in a `scripts/` folder.
- Log more complex outputs to files for practice.


## Secure Linux VM Lab - SSH Hardening, NSG, Monitoring, Backups

### SSH Hardening
sudo adduser labadmin
sudo usermod -aG sudo labadmin
sudo mkdir -p /home/labadmin/.ssh
sudo cp ~/.ssh/authorized_keys /home/labadmin/.ssh/
sudo chown -R labadmin:labadmin /home/labadmin/.ssh
sudo chmod 700 /home/labadmin/.ssh
sudo chmod 600 /home/labadmin/.ssh/authorized_keys

sudo nano /etc/ssh/sshd_config
# Add at bottom:
PermitRootLogin no
PasswordAuthentication no
sudo sshd -t
sudo systemctl restart ssh

### NSG / Firewall
Check inbound rules: only your public IP allowed on port 22
Test from Mac:
ssh -i ~/Documents/AzureKeys/vm-secure-linux_key.pem labadmin@<public-ip>

### Monitoring / Backup
Enable Azure Monitor / Insights
Enable VM Backup in Recovery Services Vault