#!/bin/bash
echo "[i] We will now uninstall Raven-Storm..."
echo "[i] This will delete all backups."
sudo rm -irf /usr/share/Raven-Storm
sudo rm -i /usr/bin/rst

echo "[i] Raven-Storm sucessfully uninstalled."
exit 0
