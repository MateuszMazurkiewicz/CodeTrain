'''
Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.
'''

def calcAngle(h, m):
    h_angle = (h % 12 + m/60)/12 * 360
    m_angle = m/60 * 360

    return max(h_angle, m_angle) - min(h_angle, m_angle)


print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165