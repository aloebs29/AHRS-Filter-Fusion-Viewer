import os
import numpy as np

data_source = "./sample_data"
NUM_HEADER_LINES = 4 # number of header lines in the file
TIME_INDEX = 0
ACCEL_INDEX = 1
GYRO_INDEX = 4

TIME_SCALE = 0.000000001 # nanoseconds to seconds
ACCEL_SCALE = 1.0
GYRO_SCALE = 0.01745329251994329576923690768489 # degrees to radians

CORRECTION_VEC = np.array([
    0,
    0.0, 0.0, 0.0, # accelerometer x,y,z corrections
    -0.035, -0.018, -0.015, # gyro x,y,z corrections
])

SCALE_VEC = np.array([
    TIME_SCALE,
    ACCEL_SCALE, ACCEL_SCALE, ACCEL_SCALE,
    GYRO_SCALE, GYRO_SCALE, GYRO_SCALE,
])


raw_data_list = {} # dictionary to hold our data sets / file names


# Loop through our files to parse data
for root, dirs, files in os.walk(data_source, topdown=False):
    for name in files:
        # Fill in our array
        unscaled_data = np.genfromtxt(os.path.join(root, name), delimiter=',', dtype='f4', 
                                          skip_header=NUM_HEADER_LINES, encoding='ascii')
        scaled_data = np.multiply(unscaled_data[:, 0:7], SCALE_VEC[None, :])
        raw_data_list[name] = np.add(scaled_data, CORRECTION_VEC[None, :])

# Secure output folder
dir_path = "./sample_data_out/"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Save files
for key, val in raw_data_list.items():
  np.savetxt(dir_path + key[:-4] + '.csv', val, header="Blaaaah", delimiter=",")