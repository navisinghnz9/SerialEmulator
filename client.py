import serial
import time
import threading

def read_echo_response(serial_port):
    """Read incoming echo responses from the emulator and print them."""
    with serial.Serial(serial_port, baudrate=9600, timeout=1) as ser:
        while True:
            # Read a line of data (echo response)
            data = ser.readline()
            if data:
                decoded_data = data.decode('utf-8').strip()
                print(f"Received echo: {decoded_data}")
            time.sleep(1)

def send_packets_to_emulator(serial_port):
    """Connect to the emulator and send data packets."""
    with serial.Serial(serial_port, baudrate=9600, timeout=1) as ser:
        print(f"Connected to emulator at {serial_port}")

        # Send multiple data packets to the emulator
        packets = [
            "Packet 1: Hello, Serial Emulator!",
            "Packet 2: Testing a dummy packet",
            "Packet 3: Good bye Emulator!"
        ]

        for packet in packets:
            print(f"Sending packet: {packet}")
            ser.write(f"{packet}\n".encode())  # Send the packet followed by a newline character
            time.sleep(1)  # Wait for a while before sending the next packet

if __name__ == '__main__':
    # Define the virtual port where the client connects (Linux example)
    serial_port = '/tmp/ttyV1'  # Change this to your actual virtual port (e.g., COM5 for Windows)

    # Create a thread to read echo responses from the emulator
    read_thread = threading.Thread(target=read_echo_response, args=(serial_port,))
    read_thread.daemon = True  # Allow thread to exit when the main program exits
    read_thread.start()

    # Send packets to the emulator in the main thread
    send_packets_to_emulator(serial_port)

    read_thread.join()
