import numpy as np
import math

def quat_from_accel(accel):
    # Normalize accel data
    a_norm = np.linalg.norm(accel)
    if (a_norm == 0.0):
        return [1.0, 0.0, 0.0, 0.0] # invalid accel data, return base orientation
    a_hat = (accel / a_norm)
    
    # Get cross product of accel and z axis to obtain orthogonal vector
    z_hat = [0.0, 0.0, 1.0]
    orth_vec = np.cross(z_hat, a_hat)
    orth_norm = np.linalg.norm(orth_vec)
    if (orth_norm == 0.0):
        return [1.0, 0.0, 0.0, 0.0] # base orientation
    orth_hat = orth_vec / orth_norm
    
    # Get angle between accel and z axis
    theta = math.acos(np.dot(z_hat, a_hat))
    
    # Calculate quaternion orientation by rotation of theta about the orthogonal unit vector
    sin_over_2 = math.sin(theta / 2.0)
    quat = [
        (math.cos(theta / 2.0)),
        (-orth_hat[0] * sin_over_2),
        (-orth_hat[1] * sin_over_2),
        (-orth_hat[2] * sin_over_2)
    ]
    quat_norm = np.linalg.norm(quat)
    if (quat_norm == 0.0):
        return [1.0, 0.0, 0.0, 0.0] # error, return base orientation
    quat_hat = quat / quat_norm
    return quat_hat

def quat_to_tait_bryan(quat):
    roll = math.atan2(
        2.0 * (quat[0] + quat[1] + quat[2] + quat[3]),
        (quat[0] ** 2) - (quat[1] ** 2) - (quat[2] ** 2) + (quat[3] ** 2)
    )
    pitch = math.asin(2.0 * ((quat[0] * quat[2]) - (quat[1] * quat[3])))
    yaw = math.atan2(
        2.0 * ((quat[1] * quat[2]) + (quat[0] * quat[3])),
        (quat[0] ** 2) + (quat[1] ** 2) - (quat[2] ** 2) - (quat[3] ** 2)
    )
    
    return [roll, pitch, yaw]