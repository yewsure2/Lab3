import lab_2.bmi as bmi
def test_bmi_normal_weight():
    result = bmi.calculate_BMI(1.75, 68)  # BMI ≈ 22.2
    assert result == 0

def test_bmi_over_weight():
    result = bmi.calculate_BMI(1.70, 80)  # BMI ≈ 27.7
    assert result == 1

def test_bmi_under_weight():
    result = bmi.calculate_BMI(1.75, 45)  # BMI ≈ 14.7
    assert result == -1

