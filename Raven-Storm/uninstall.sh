#!/bin/bash
echo "[i] We will now uninstall Raven-Storm..."
echo "[i] This will delete all backups."
sudo rm -i /usr/bin/rst
sudo rm -rf -i /usr/share/Raven-Storm

echo "[i] Raven-Storm sucessfully uninstalled."
exit 0
