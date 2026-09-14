# services/power.py

def calculate_power(voltage: float, current: float) -> float:
    """คำนวณกำลังไฟฟ้า P = V x I
    เงื่อนไข: V > 0 และ I >= 0 ถ้าผิดเงื่อนไขจะเกิด ValueError
    """
    if voltage <= 0:
        raise ValueError("แรงดันไฟฟ้า (Voltage) ต้องมากกว่า 0 โวลต์")
    if current < 0:
        raise ValueError("กระแสไฟฟ้า (Current) ต้องมากกว่าหรือเท่ากับ 0 แอมแปร์")
    
    return voltage * current


def classify_power(power_watt: float) -> str:
    """จำแนกสถานะจากกำลังไฟฟ้า (วัตต์)
    - น้อยกว่า 500 W -> NORMAL
    - 500 ถึง 1000 W -> WARNING
    - มากกว่า 1000 W -> CRITICAL
    """
    if power_watt < 500:
        return "NORMAL"
    elif power_watt <= 1000:
        return "WARNING"
    else:
        return "CRITICAL"
