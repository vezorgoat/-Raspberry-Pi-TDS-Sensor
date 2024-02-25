## CQRobot Ocean TDS Meter Sensor ##
Overview (**Note: I do not own all the images seen here**)

The CQRobot Ocean TDS Meter Sensor is a reliable tool designed to measure Total Dissolved Solids (TDS) in water. This sensor is widely used in various applications such as water quality monitoring, hydroponics, aquariums, and industrial processes.

## Requirements

Before using the CQRobot Ocean TDS Meter Sensor, ensure you have the following:
* [CQRobot Ocean: TDS Meter Sensor](https://www.amazon.com/CQRobot-Ocean-Compatible-Scientific-Laboratory/dp/B08KXRHK7H/)
* [ADS1115 16-Bit Sensor Analog Signal](https://www.amazon.com/CQRobot-Ocean-Acquisition-Conversion-Motherboards/dp/B08KFZ3PVT/)

### Connection
Follow the image below to connect your TDS sensor to the Pie.
![image](https://m.media-amazon.com/images/I/914mvtbb-vL._SX522_.jpg)

### Software Requirements

You will need the following software installed on your Raspberry Pi or microcontroller:

- **Python**: Ensure Python is installed on your system. You can download it from the official Python website: [Python.org](https://www.python.org/downloads/)
- **smbus Library**: Install the `smbus` library for I2C communication. You can install it using the package manager on your system. For Raspberry Pi, use the following command:

    ```
    sudo apt-get install python3-smbus
    ```

    If you're using Python 2, replace `python3-smbus` with `python-smbus`.

### Enabling I2C

If you're using a Raspberry Pi or similar microcontroller, you need to enable the I2C interface. Follow these steps to enable it:

1. Boot your Raspberry Pi and log in to the terminal or desktop environment.

2. Launch the Raspberry Pi Configuration tool by running the following command:

    ```
    sudo raspi-config
    ```

3. Use the arrow keys to navigate to `Interfacing Options` and press Enter.

4. Navigate to `I2C` and press Enter.

5. Select `<Yes>` when asked if you want to enable the I2C interface.

6. Press Enter to confirm and then select `<Finish>`.

7. Reboot your Raspberry Pi by running the following command:

    ```
    sudo reboot
    ```

8. After rebooting, you can verify that I2C is enabled by running the following command:

    ```
    ls /dev/i2c*
    ```

    You should see `/dev/i2c-1` listed, indicating that the I2C interface is enabled.

## Files Required

To get started with the CQRobot Ocean TDS Meter Sensor, you'll need to download the following files from this repository:

1. **[TDS Data](https://github.com/vezorgoat/-Raspberry-Pi-TDS-Sensor/blob/main/TDS_Data.py)**: The script enables you to obtain voltage readings directly from the sensor in real-time, allowing for accurate monitoring of water quality.

2. **[Read Voltage](https://github.com/vezorgoat/-Raspberry-Pi-TDS-Sensor/blob/main/ReadVoltage.py)**: The Script enables data from the sensor to be read and formated([Note: this is not my script](http://www.cqrobot.wiki/index.php/TDS_(Total_Dissolved_Solids)_Meter_Sensor_SKU:_CQRSENTDS01))

### Running the Script




