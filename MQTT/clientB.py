import paho.mqtt.client as mqtt

# MQTT 클라이언트 생성
client = mqtt.Client()

# MQTT 서버에 연결
client.connect("192.168.111.130", 1883)

# 메시지 수신 이벤트 핸들러 등록
def on_message(client, userdata, message):
    # 메시지 출력
    action = message.payload.decode("utf-8")
    if action == "Action1 Start":
        print("동작1이 시작되었습니다")
    elif action == "Action2 Start":
        print("동작2가 시작되었습니다")
    elif action == "Action1 Stop":
        print("동작1 멈춤")
    elif action == "Action2 Stop":
        print("동작2 멈춤")

# 메시지 수신 이벤트 핸들러 등록
client.on_message = on_message

# MQTT 서버에 구독
client.subscribe("/action")

# MQTT 서버 연결 종료
#client.disconnect()
client.loop_forever()
