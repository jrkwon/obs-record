# OBS Recorder: triggered by VICON signal

2/03/2023

## Software Installation

### Required Software

- Python3

  - https://www.python.org/downloads/windows/ 

- Anaconda

  - https://www.anaconda.com/products/individual

  - Quick Note to see if your Windows is 64-Bit.

    If the "C:\Program Files (32)” folder exists, you’re using 64-Bit Windows.

    

## Create a Conda Environment

- After installing Anaconda, create an environment for the capture software.
  - `$ conda env create -f environment.yml`
- Activate the environment.
  - `$ conda activate obs-record`

## Use obs-record.py

- First, make sure your Arduino board is connected and running.
- Second, start OBS and get ready for recording. The hotkey for recording start is F3 and stop is F4.
- The most important thing to do is that the OBS is your _focused_ window so that any keyboard inputs can go to the OBS program.

### How to use

#### Specify port name: Mandatory

ex) your Arduino board is connected to `COM1`
```shell
python obs-record.py COM1
```

#### All options

```shell
python obs-record.py -h
```

```
usage: obs-record.py [-h] [-v VERBOSE]
                     [-b {9600,14400,19200,28800,31250,38400,57600,115200}]
                     port

OBS Recorder: triggered by VICON ver 0.1 by Jaerock Kwon, 2023

positional arguments:
  port                  Serial port name. COM{#} or /dev/ttyUSB{#}

optional arguments:
  -h, --help            show this help message and exit
  -v VERBOSE, --verbose VERBOSE
                        increase output verbosity
  -b {9600,14400,19200,28800,31250,38400,57600,115200}, --baudrate {9600,14400,19200,28800,31250,38400,57600,115200}
                        baudrate
```

---
# Arudino program

Compile `vicon_trigger.ino` and upload it to your Arduino board. 

## Notes:
- Use PIN 7 for the signal.
- `baudrate` is 115200.