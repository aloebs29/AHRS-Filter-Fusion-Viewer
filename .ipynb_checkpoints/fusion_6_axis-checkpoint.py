import numpy as np
import math

def madgwick_update_6(quat_in, accel, gyro, delta_t, beta, zeta):
    # Normalize accel data
    a_norm = np.linalg.norm(accel)
    if (a_norm == 0.0):
        return quat_in # invalid accel data, return previous orientation   
    a_hat = (accel / a_norm)

    # Compute & normalize gradient
    gradient = _compute_gradient_6(quat_in, a_hat)
    gradient_norm = np.linalg.norm(gradient)
    if (gradient_norm == 0.0):
        return quat_in # invalid gradient, return previous orientation
    gradient_hat = (gradient / gradient_norm)
    
    # Correct gyroscope measurement
    gyro_corrected = _compute_gyro_corrected_6(quat_in, gradient_hat, gyro, delta_t, zeta)
    
    # Compute q dot, update quaternion
    q_dot = _compute_q_dot_6(quat_in, gradient_hat, gyro_corrected, beta)
    quat = [(quat_i + (q_dot_i * delta_t)) for quat_i, q_dot_i in zip(quat_in, q_dot)]
    quat_norm = np.linalg.norm(quat)
    if (quat_norm == 0.0):
        return quat_in # invalid update, return previous orientation
    
    return (quat / quat_norm)

# Helper functions
def _compute_gradient_6(quat, a_hat):
    # Compute the objective function and jacobian
    obj_1 = (2.0 * quat[1] * quat[3]) - (2.0 * quat[0] * quat[2]) - a_hat[0]
    obj_2 = (2.0 * quat[0] * quat[1]) - (2.0 * quat[2] * quat[3]) - a_hat[1]
    obj_3 = 1.0 - (2.0 * (quat[1] ** 2)) - (2.0 * (quat[2] ** 2)) - a_hat[2]
    
    j_11_and_24 = 2.0 * quat[2]
    j_12_and_23 = 2.0 * quat[3]
    j_13_and_22 = 2.0 * quat[0]
    j_14_and_21 = 2.0 * quat[1]
    j_32 = 4.0 * quat[1]
    j_33 = 4.0 * quat[2]
    
    gradient = [
        (j_14_and_21 * obj_2) - (j_11_and_24 * obj_1),
        (j_12_and_23 * obj_1) + (j_13_and_22 * obj_2) - (j_32 * obj_3),
        (j_12_and_23 * obj_2) - (j_33 * obj_3) - (j_13_and_22 * obj_1),
        (j_14_and_21 * obj_1) + (j_11_and_24 * obj_2)
    ]
    
    return gradient

def _compute_gyro_corrected_6(quat, gradient_hat, gyro, delta_t, zeta):
    gyro_bias = [
        ((2.0 * quat[0] * gradient_hat[1]) -
         (2.0 * quat[1] * gradient_hat[0]) -
         (2.0 * quat[2] * gradient_hat[3]) +
         (2.0 * quat[3] * gradient_hat[2])),
        
        ((2.0 * quat[0] * gradient_hat[2]) +
         (2.0 * quat[1] * gradient_hat[3]) -
         (2.0 * quat[2] * gradient_hat[0]) -
         (2.0 * quat[3] * gradient_hat[1])),
        
        ((2.0 * quat[0] * gradient_hat[3]) -
         (2.0 * quat[1] * gradient_hat[2]) +
         (2.0 * quat[2] * gradient_hat[1]) -
         (2.0 * quat[3] * gradient_hat[0]))
    ]
    return [(gyro_i - (bias_i * delta_t * zeta)) for gyro_i, bias_i in zip(gyro, gyro_bias)]

def _compute_q_dot_6(quat, gradient_hat, gyro_corrected, beta):    
    q_dot = [
        -((0.5 * quat[1] * gyro_corrected[0]) -
          (0.5 * quat[2] * gyro_corrected[1]) -
          (0.5 * quat[3] * gyro_corrected[2]) -
          (gradient_hat[0] * beta)),
        
        ((0.5 * quat[0] * gyro_corrected[0]) +
          (0.5 * quat[2] * gyro_corrected[1]) -
          (0.5 * quat[3] * gyro_corrected[2]) -
          (gradient_hat[1] * beta)),
        
        ((0.5 * quat[0] * gyro_corrected[0]) -
          (0.5 * quat[1] * gyro_corrected[1]) +
          (0.5 * quat[3] * gyro_corrected[2]) -
          (gradient_hat[2] * beta)),
        
        ((0.5 * quat[0] * gyro_corrected[0]) +
          (0.5 * quat[1] * gyro_corrected[1]) -
          (0.5 * quat[2] * gyro_corrected[2]) -
          (gradient_hat[3] * beta))        
    ]
    
    return q_dot