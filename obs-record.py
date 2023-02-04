import serial
import argparse
import pyautogui

record_start_key = 's'
record_stop_key = 'e'
record_start_hotkey = 'f3'
record_stop_hotkey = 'f4'

def main(args):
    # init serial port
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = args.port
    ser.open()

    print('Monitoring VICON trigger signal...')
    print('** Make sure your OBS window is focused.')

    while(True):
        key = ser.read() # read one byte
        if key == record_start_key:
            pyautogui.press(record_start_hotkey)
            if args.verbose:
                print(f'{key} received. {record_start_hotkey} is pressed.')
        elif key == record_stop_key:
            pyautogui.press(record_stop_hotkey)     
            if args.verbose:
                print(f'{key} received. {record_stop_hotkey} is pressed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OBS Recorder: triggered by VICON ver 0.1 by Jaerock Kwon, 2023')
    parser.add_argument("port", type=str, help="Serial port name. COM{#} or /dev/ttyUSB{#}")
    parser.add_argument("-v", "--verbose", type=bool, default=True, help="increase output verbosity")
    parser.add_argument("-b", "--baudrate", type=int, default=115200, choices=[9600, 14400, 19200, 28800, 31250, 38400, 57600, 115200], help="baudrate")
    args = parser.parse_args()

    main(args)

