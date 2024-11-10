

def normalize_to_servo_range(x_max, y_max, x_val, y_val, servo_min, servo_max):
    norm_x = x_val/x_max
    norm_y = y_val/y_max

    x_servo_val = (norm_x * (servo_max-servo_min)) + servo_min
    y_servo_val = (norm_y * (servo_max-servo_min)) + servo_min



    return (int(x_servo_val), int(y_servo_val))