import serial
# import time


class ThermocoupleReader:
    def __init__(self, port="/dev/ttyUSB0", baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def open(self):
        """Open the serial connection."""
        if not self.serial or not self.serial.is_open:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Serial port {self.port} opened.")

    def close(self):
        """Close the serial connection."""
        if self.serial and self.serial.is_open:
            self.serial.close()
            print(f"Serial port {self.port} closed.")

    def __del__(self):
        """Ensure the serial connection is closed when the object is destroyed."""
        self.close()

    def read_temperatures(self):
        """Read temperature values from up to 4 channels."""
        if not self.serial or not self.serial.is_open:
            print("Serial port is not open.")
            return

        # Send request command
        command = bytes([0xAA, 0x55, 0x01, 0x03, 0x03])
        self.serial.write(command)
        # time.sleep(0.2)
        response = self.serial.read(64)

        # print("Raw data (hex):", response.hex())

        # Find the start marker "55 aa"
        start = response.find(b"\x55\xaa")
        if start == -1 or len(response) < start + 13:
            print("No valid response.")
            return

        # Extract temperature data: 4 channels × 2 bytes
        temp_data = response[start + 4 : start + 4 + 8]

        temperatures = []
        for i in range(0, len(temp_data), 2):
            raw_bytes = temp_data[i : i + 2]
            raw = int.from_bytes(temp_data[i : i + 2], byteorder="little")
            # print(f"Channel {i//2+1} raw: {raw_bytes.hex()} -> {raw / 10.0}°C")
            if not raw == 28000:
                temperatures.append(raw / 10.0)
            else:
                temperatures.append(None)

        return temperatures


# Example usage
if __name__ == "__main__":
    reader = ThermocoupleReader("/dev/ttyUSB0")
    reader.open()
    for i in range(100):
        Channel1, Channel2, Channel3, Channel4 = reader.read_temperatures()
        print(
            f"Channel 1: {Channel1}°C, Channel 2: {Channel2}°C, Channel 3: {Channel3}°C, Channel 4: {Channel4}°C"
        )
    reader.close()
