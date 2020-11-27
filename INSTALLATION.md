# Raven-Storm

<a style="color: white;" href="https://github.com/Taguar258/Raven-Storm/blob/master/INSTALLATION.md#lazy-installer">Advanced</a> - <a style="color: white;" href="https://github.com/Taguar258/Raven-Storm/blob/master/INSTALLATION.md#or-start-your-unix-terminal-and-type-in-following">Expert</a> - <a style="color: white;" href="https://github.com/Taguar258/Raven-Storm/blob/master/INSTALLATION.md#other-operating-systems">Other operating systems</a> - <a style="color: white;" href="https://github.com/Taguar258/Raven-Storm/blob/master/INSTALLATION.md#uninstall">Uninstall</a>

## Lazy installer
(Advanced)

To install Raven-Storm enter the following command:

(You might need to install curl)

```curl -s https://raw.githubusercontent.com/Taguar258/Raven-Storm/master/install.sh | sudo bash -s```

![render1604868703436](https://user-images.githubusercontent.com/36562445/98484164-d0ec5300-220d-11eb-8fe5-0c9d4d2103e6.gif)

## Or start your Unix terminal and type in following

(Expert)

```sudo pkg/pacman/apt-get/brew install git python3 nmap python3-setuptools bluez dsniff iputils-ping aircrack-ng```

```git clone https://github.com/Taguar258/Raven-Storm/```

```cd Raven-Storm```

```sudo bash install_to_bin.sh```

```sudo rst```

## Other Operating Systems

(Unix based systems like Linux and MacOS/OSX run Raven-Storm nativly.)
(In case you want to use Raven-Storm on Windows, you will just need to perform the steps listed below, but keep in mind that it will not run as stable and not every module will work.)

Just install python 3.8 and download this repository.

You will then need to install the requirements (requirements.txt) and execute main.py.

0. Install Python (3.8) (3.6 should work as well.) (On windows, make sure to enable add to PATH.)

1. Download Zip

2. Unzip

3. Open terminal in the Raven-Storm folder. (On windows you should be able to just right click the folder while holding down the shift key, you can then click on open in Powershell (administrator).)

4. Install the requirements.

`pip install -r requirements.txt`

5. Execute Raven-Storm.

`python main.py`

(You might need to add a 3 directly after python and pip.)

## Uninstall

Just execute the folowing:

```
sudo bash /usr/share/Raven-Storm/uninstall.sh
```
