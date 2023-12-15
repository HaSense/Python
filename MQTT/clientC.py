import paho.mqtt.client as mqtt
import os

# MQTT 클라이언트 생성
client = mqtt.Client()

# MQTT 서버에 연결
client.connect("192.168.111.130", 1883)

# 메시지 객체 생성
def make_message(action):
    if action == "1":
        return "Action1 Start"
    elif action == "2":
        return "Action1 Stop"
    elif action == "3":
        return "Action2 Start"
    elif action == "4":
        return "Action2 Stop"
    elif action == "5":
        os.system("exit")
    else:
        return None

# 메뉴 출력
def print_menu():
    print("메뉴를 선택하세요.")
    print("1. Action1 Start")
    print("2. Action1 Stop")
    print("3. Action2 Start")
    print("4. Action2 Stop")
    print("5. 종료")

# 메뉴 선택
def get_menu_choice():
    return input("입력: ")

# 메시지 발행
def publish_message(action):
    message = make_message(action)
    client.publish("/action", message)

# 메인 함수
def main():
    # 메뉴 출력
    print_menu()

    # 메뉴 선택
    choice = get_menu_choice()

    # MQTT 서버에 연결
    client.connect("192.168.111.130", 1883)

    # 메뉴 처리
    while choice != "5" and choice != "q":
        # MQTT 서버에 구독
        client.subscribe("/action")

        # 메시지 발행
        publish_message(choice)

        # 메뉴 출력
        print_menu()

        # 메뉴 선택
        choice = get_menu_choice()

    # MQTT 서버 연결 종료
    #client.loop_forever()
    client.disconnect()
    
# 메인 함수 호출
if __name__ == "__main__":
    main()
