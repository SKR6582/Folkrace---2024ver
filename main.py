from math import *

class Robot:
    class Motor:
        def __init__(self):
            pass  # 모터 초기화 코드 작성

    def __init__(self):
        self.motor_A = None

    def set_motor_A(self, motor):
        self.motor_A = motor       


    class Sensor:
        def __init__(self):
            pass 
    def __init__(self):
        self.sensor_B = None

    def set_sensor_B(self, sensor):
        self.sensor_B = sensor
        
error = 0
p_fix = 0
target = 80 # 예시
# 예시 
bot = Robot() 
motor_A = bot.motor()
motor_B = bot.motor() 
motor_C = bot.motor() 
motor_D = bot.motor() 

sensor_A = bot.sensor()
sensor_B = bot.sensor()

motor_way = 0
# 상수값 설정. (벽 A ~ B 사이의 거리)

# 제어

body_length = 15
while True :
    # 주행 위치 = target/2
    # USS 두 센서의 합은 target - body_length    
    # 한 센서당 담당하는 길이 = (target - body_length) / 2  
    if sensor_A > sensor_B : # |-----ㅁ++|
        error += (((target - body_length) / 2 ) - sensor_B ) * -1 
        
    else :
        error += (((target - body_length) / 2 ) - sensor_A ) 



# error 값 가공



    motor_way = (error)# 기존값 +- error


    """
    way
    -------------A/B++++++++++++++
    
    """