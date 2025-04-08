# Python-ThermocoupleReader
THE-373 K/J/T Thermocouple Thermometer

This Python script reads temperature data from a 4-channel thermocouple module via a serial connection (typically over USB). It communicates with the device using a predefined byte protocol and parses the response to extract the temperature values.

<img src="https://cd50.net/wp-content/uploads/2023/05/THE-373.jpg" alt="Thermocouple Module" height="400"/>

[https://cd50.net/wp-content/uploads/2023/05/THE-373.jpg](https://cd50.net/wp-content/uploads/2023/05/THE-373.jpg)

The code is based on [https://cd50.net/37/](https://cd50.net/37/) and also works under linux and windows.

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/Steffen-W/Python-ThermocoupleReader.git
```

## Example

```python
from thermocouple_reader import ThermocoupleReader

reader = ThermocoupleReader("/dev/ttyUSB0")
reader.open()

Channel1, Channel2, Channel3, Channel4 = reader.read_temperatures()
print(f"Channel 1: {Channel1}°C, Channel 2: {Channel2}°C, Channel 3: {Channel3}°C, Channel 4: {Channel4}°C")

reader.close()
```

Example Output

```
Channel 1: 24.5°C, Channel 2: 24.0°C, Channel 3: 25.1°C, Channel 4: 28.9°C
```

## Configuration

You can configure the serial port and baud rate when initializing the reader:

```python
reader = ThermocoupleReader(port='/dev/ttyUSB0', baudrate=9600)
```

Default values:
- Port: /dev/ttyUSB0 or COM1
- Baudrate: 9600