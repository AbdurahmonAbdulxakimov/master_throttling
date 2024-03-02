from datetime import datetime


def request_allowed(hour_from: int = 12, hour_to: int = 20) -> bool:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_hour = current_time.split(":")[0]

    if current_hour >= str(hour_from) and current_hour <= str(hour_to):
        return True

    return False
