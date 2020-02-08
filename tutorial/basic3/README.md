# <center>Raven-Storm</center>

Using investigation you can view the targets status and gather information.

## Port scanning:
You can perform port scanns using:
- ```get port i {target ip}```
- ```get port w {target domain}```

## Pre-Stress testing:
You can test for the amount of threads the target can handle without complications:
- First run ```stress``` . to activate the mode.
- Values like threads will be used for this mode as well.
- You can define the time between each test level using:
- ```st wait {2}```

## Get IP using domain:
You can get the IP by domain using:
- ```hbi {domain}```

## Lan scan:
You can get the IP and Hostname of all devices in you network using:
- ```lan scan```

# Speed test:
You can mesure the speed using:
- ```speed down {domain}``` , for the download speed.
- ```speed ping {domain}``` , get the ping speed.

![render1581120587345](https://user-images.githubusercontent.com/36562445/74074890-7751c080-4a10-11ea-9f21-8fca114e3b97.gif)
