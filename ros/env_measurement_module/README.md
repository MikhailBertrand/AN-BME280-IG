# ROS node for AN-301 environment measurement module

## Setup

- Install requirements and set permission.

  ```bash
  sudo apt install libhidapi-hidraw0 libudev-dev libusb-1.0-0-dev
  pip install hidapi

  # If hid is installed
  pip uninstall hid

  # If user is not included in dialout group
  sudo gpasswd -a ${user_name} dialout

  su root
  # Enter password for root (Create password for root first if not set)
  echo 'ATTRS{idVendor}=="04d8", ATTRS{idProduct}=="00dd", SYMLINK+="ttyEnvModule", GROUP="dialout", MODE="0666"' >> /etc/udev/rules.d/99-my.rules
  exit
  ```

  Rebooting may be necessary.

- Copy this package to your catkin workspace and build.


## Run

Connect your device to your PC and run the following launch file.

```
roslaunch env_measurement_module env_measurement.launch
```

Topics will appear (all of them have the datatype `Float32`).
```
$ rostopic list
...
/env_measurement/discomfort_index
/env_measurement/humidity
/env_measurement/pressure
/env_measurement/temperature
...
```
