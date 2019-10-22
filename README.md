# AHRS Filter/Fusion Viewer

This is a notebook for evaluating the performance of filter/fusion methods on tests performed with 9-DOF motion detectors. 

![Fused Data Plots](/screenshots/fused_plots.PNG?raw=true "Fused Data Plots")

Sample data is included to display the basic functionality of the notebook. Simply change the path where the data is loaded from to view your own data sets. The 0'th column of the data is expected to be the time column, 1-3 for accelerometer x/y/z, 4-6 for gyroscope x/y/z, and 7-9 for magnetometer x/y/z.

This notebook allows you to quickly change filter/fusion conditions and see the results of those changes. These conditions include:
  - accelerometer, gyroscope, and magnetometer calibration values
  - beta and zeta inputs into the Madgwick filter/fusion algorithm
  - 6-axis (accel & gyro) or 9-axis (accel, gyro, magnetometer) fusion
  
![Un-fused Data Plots](/screenshots/unfused_plots.PNG?raw=true "Un-fused Data Plots")

More fusion algorithms to be added in the future.
