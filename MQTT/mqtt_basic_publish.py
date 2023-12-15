# 가장 기본적은 메시지 출력 파이썬 코드
# 파이썬 가상화를 아나콘다를 사용하고 있어서 모듈은 콘다를 이용해서 받았다.
# conda install -c conda-forge paho-mqtt

import paho.mqtt.client as mqtt

# MQTT 클라이언트 생성
client = mqtt.Client()

# MQTT 서버에 연결
client.connect("192.168.111.130", 1883) #localhost라 적으면 혼자서 테스트 가능하다.

# 윈도우에서 다음과 같이 실행 mosquitto_sub.exe -h localhost -t /test/topic
# 외부에서 접근이 되게 하려면 윈도우의 경우 C:\Program Files\mosquitto.conf 에서 
# listener 1883 0.0.0.0 (열기)
# allow_anonymous true (열기)
# 설정을 해주면 외부에서 접근할 수 있다. 그렇지 않으면 로컬에서 밖에 동작하지 않는다.

# 메시지 객체 생성
message = mqtt.MQTTMessage()
message.topic = "/test/topic".encode("utf-8") #토픽이름
message.payload = "Hello, world!".encode("utf-8") #메시지 내용

# 주제 확인
if message.topic is None or message.topic == "":
    print("주제가 없습니다.")
else:
    print(message.topic)
        
# MQTT 메시지 발행
#client.publish("/test/topic", "HELLO")
#주제방에 메시지 내용이 출력된다.
client.publish(message.topic, message.payload)
    
# MQTT 서버 연결 종료
client.disconnect()
