import serial
import time


def listen_on_virtual_serial_port(serial_port):
    """Listen for incoming data on the specified serial port."""

    with serial.Serial(serial_port, baudrate=9600, timeout=1) as ser:
        print(f"Listening on {serial_port}...")

        while True:
            data = ser.readline()  # Reads a line of data
            if data:
                decoded_data = data.decode('utf-8').strip()
                print(f"Received packet: {decoded_data} \n")

                # Log the received packet to a file with a timestamp
                with open('received_data_log.txt', 'a') as log_file:
                    log_file.write(f"{time.ctime()}: {decoded_data}\n")

                # Sending back a response (for testing echo)
                ser.write(f"Echo: {decoded_data}".encode())
                print(f"Sent packet: Echo: {decoded_data}")
            time.sleep(1)

if __name__ == '__main__':
    # Replace with your virtual port (Linux example)
    serial_port = '/tmp/ttyV0'  # Emulator listens here
    listen_on_virtual_serial_port(serial_port)
