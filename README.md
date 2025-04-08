# Python-ThermocoupleReader
THE-373 K/J/T Thermocouple Thermometer

This Python script reads temperature data from a 4-channel thermocouple module via a serial connection (typically over USB). It communicates with the device using a predefined byte protocol and parses the response to extract the temperature values.

<img src="https://cd50.net/wp-content/uploads/2023/05/THE-373.jpg" alt="Thermocouple Module" height="400"/>

[https://cd50.net/wp-content/uploads/2023/05/THE-373.jpg](https://cd50.net/wp-content/uploads/2023/05/THE-373.jpg)

The code is based on [https://cd50.net/37/](https://cd50.net/37/) and also works under linux and windows.

## Requirements

- Python 3.x  
- [pyserial](https://pypi.org/project/pyserial/)

Install the required library with:

```bash
pip install pyserial
```

## Usage
Run the script:

```bash
python thermocouple_reader.py
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
- Port: /dev/ttyUSB0
- Baudrate: 9600