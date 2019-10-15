# AHRS Filter/Fusion Viewer

This is a notebook for evaluating filter/fusion methods on tests performed with 9-DOF motion detectors in real-time. The 0'th column is expected to be the time column, 1-3 for accelerometer x/y/z, 4-6 for gyroscope x/y/z, and 7-9 for magnetometer x/y/z.

This notebook allows you to quickly change filter/fusion conditions and see the results of those changes. These conditions include:
  - accelerometer, gyroscope, and magnetometer calibration values
  - beta and zeta inputs into the Madgwick filter/fusion algorithm
  - 6-axis (accel & gyro) or 9-axis (accel, gyro, magnetometer) fusion

More fusion algorithms to be added in the future.
