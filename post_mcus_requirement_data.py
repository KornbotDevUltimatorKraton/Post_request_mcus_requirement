import requests 
reqdat = requests.post("http://192.168.50.247:5978/mcus_post_processing",json={'email':"kornbot380@hotmail.com",'project_name':'Smart_Robots','Spec_requirement':'Robotics arm joint motor control',
                                                                               'components_pin':{'UART_pin':3,'Analog_pin':4,'Servo_pin':5,'PWM':8}})
