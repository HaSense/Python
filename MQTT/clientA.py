import paho.mqtt.client as mqtt

# MQTT 클라이언트 생성
client = mqtt.Client()

# MQTT 서버에 연결
client.connect("192.168.111.130", 1883)

# 메시지 객체 생성
def make_message(action):
    if action == "Action1 Start":
        return "Action1 Start"
    elif action == "Action2 Start":
        return "Action2 Start"
    elif action == "Action1 Stop":
        return "Action1 Stop"
    else:
        return None

# MQTT 메시지 발행
message = make_message("Action1 Stop")
client.publish("/action", message)

# MQTT 서버 연결 종료
client.disconnect()
#client.loop_forever()
