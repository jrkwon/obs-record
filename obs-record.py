import serial
import argparse
import pyautogui

# config
record_start_key = b's'
record_stop_key = b'e'
record_start_hotkey = 'f3'
record_stop_hotkey = 'f4'
baudrate = 115200

def main(args):
    # init serial port
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.port = args.port
    ser.open()

    pyautogui.alert('Click OK when you are ready. Make sure the OBS window to be focused.', 'VICON Trigger Monitor for OBS', button='OK')

    print('>>> OBS-RECORD via VICON trigger signals <<<')
    print('-- In OBS Studio, the function keys must be set with F3-Record and F4-Stop')
    print('** Make sure your OBS Studio window is focused **')

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
    parser = argparse.ArgumentParser(description='OBS Recorder: triggered by VICON ver 0.3 by Jaerock Kwon, 2023')
    parser.add_argument("port", type=str, help="Serial port name. COM{#} or /dev/ttyUSB{#}")
    parser.add_argument("-v", "--verbose", type=bool, default=True, help="increase output verbosity")
    parser.add_argument("-b", "--baudrate", type=int, default=115200, choices=[9600, 14400, 19200, 28800, 31250, 38400, 57600, 115200], help="baudrate")
    args = parser.parse_args()

    main(args)

