#!/bin/bash
echo "[i] Installation"
if [[ "$OSTYPE" == "linux-gnu" ]]; then
        sudo apt-get -y upgrade > /dev/null 2>&1
        git --help > /dev/null 2>&1 || sudo apt-get -y install git || echo "[!] Could not install git"
        python3 --help > /dev/null 2>&1 || sudo apt-get -y install python3 || echo "[!] Could not install python3"
        command -v ping > /dev/null 2>&1 || sudo apt-get -y install iputils-ping || echo "[!] Could not install ping"
        nmap --help > /dev/null 2>&1 || sudo apt-get -y install nmap || echo "[!] Could not install nmap"
        git clone https://github.com/Taguar258/Raven-Storm/ > /dev/null 2>&1
        cd Raven-Storm > /dev/null 2>&1 || echo "[i] Could not clone repository"
        python3 -m pip install -r requirements.txt > /dev/null 2>&1 || echo "[i] Could not install requirements"
        echo "[i] Done"
        python3 main.py || echo "[i] Run: >cd Raven-Storm ; python3 main.py< to start"
elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew --help > /dev/null 2>&1 || /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        git --help > /dev/null 2>&1 || brew install git || echo "[!] Could not install git"
        python3 --help > /dev/null 2>&1 || brew install python3 || echo "[!] Could not install python3"
        command -v ping > /dev/null 2>&1 || brew install iputils-ping || echo "[!] Could not install ping"
        nmap --help > /dev/null 2>&1 || brew install nmap || echo "[!] Could not install nmap"
        git clone https://github.com/Taguar258/Raven-Storm/ > /dev/null 2>&1
        cd Raven-Storm > /dev/null 2>&1 || echo "[i] Could not clone repository"
        python3 -m pip install -r requirements.txt > /dev/null 2>&1 || echo "[i] Could not install requirements"
        echo "[i] Done"
        python3 main.py || echo "[i] Run: >cd Raven-Storm ; python3 main.py< to start"
elif [ -f "/etc/arch-release" ]; then
        git --help > /dev/null 2>&1 || sudo pacman -S git || echo "[!] Could not install git"
        python3 --help > /dev/null 2>&1 || sudo pacman -S python3 || echo "[!] Could not install python3"
        command -v ping > /dev/null 2>&1 || sudo pacman -S iputils-ping || echo "[!] Could not install ping"
        nmap --help > /dev/null 2>&1 || sudo pacman -S nmap || echo "[!] Could not install nmap"
        git clone https://github.com/Taguar258/Raven-Storm/ > /dev/null 2>&1
        cd Raven-Storm > /dev/null 2>&1 || echo "[i] Could not clone repository"
        python3 -m pip install -r requirements.txt > /dev/null 2>&1 || echo "[i] Could not install requirements"
        echo "[i] Done"
        python3 main.py || echo "[i] Run: >cd Raven-Storm ; python3 main.py< to start"
else
        echo "[i] Please install some things manually"
        git clone https://github.com/Taguar258/Raven-Storm/ > /dev/null 2>&1 || echo "[!] Please install git"
        python3 --help > /dev/null 2>&1 || echo "[!] Please install python3"
        command -v ping > /dev/null 2>&1 || echo "[!] Please install ping"
        nmap --help > /dev/null 2>&1 || echo "[!] Please install nmap"
        cd Raven-Storm > /dev/null 2>&1 || echo "[i] Could not clone repository"
        python3 -m pip install -r requirements.txt > /dev/null 2>&1 || echo "[i] Could not install requirements"
        echo "[!] PRESS ENTER TO TRY TO RUN THE SCRIPT"
        read
        python3 main.py || echo "[i] Could not run script"
        echo "[i] Done"
fi
