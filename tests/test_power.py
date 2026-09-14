# tests/test_power.py
import pytest
from services.power import calculate_power, classify_power

def test_calculate_power_success():
    """ทดสอบการคำนวณกำลังไฟฟ้าในกรณีที่ถูกต้อง"""
    assert calculate_power(220, 2) == 440.0
    assert calculate_power(110, 0) == 0.0

def test_calculate_power_invalid_voltage():
    """ทดสอบกรณี Voltage น้อยกว่าหรือเท่ากับ 0 ต้องเกิด ValueError"""
    with pytest.raises(ValueError):
        calculate_power(0, 5)
    with pytest.raises(ValueError):
        calculate_power(-10, 5)

def test_calculate_power_invalid_current():
    """ทดสอบกรณี Current น้อยกว่า 0 ต้องเกิด ValueError"""
    with pytest.raises(ValueError):
        calculate_power(220, -1)

def test_classify_power_normal():
    """ทดสอบสถานะ NORMAL (< 500 W)"""
    assert classify_power(499.9) == "NORMAL"
    assert classify_power(0) == "NORMAL"

def test_classify_power_warning():
    """ทดสอบสถานะ WARNING (500 - 1000 W)"""
    assert classify_power(500) == "WARNING"
    assert classify_power(1000) == "WARNING"

def test_classify_power_critical():
    """ทดสอบสถานะ CRITICAL (> 1000 W)"""
    assert classify_power(1000.1) == "CRITICAL"
    assert classify_power(1500) == "CRITICAL"
1213้