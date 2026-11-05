def time_to_collision(distance_m, ego_speed, lead_speed):
    closing_speed = ego_speed - lead_speed
    if closing_speed <= 0:
        return float("inf")
    return distance_m / closing_speed

def warning_level(ttc):
    if ttc < 1.5:
        return "BRAKE"
    if ttc < 3.0:
        return "WARN"
    return "OK"