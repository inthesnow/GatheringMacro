# services/macro_runner.py
import time
from services.click_actions import run_click_sequence

# 중단 상태를 전역 변수로 관리
stop_macro = False

def on_stop(button_widget):
    global stop_macro
    stop_macro = True
    print("🛑 사용자에 의해 중단 버튼이 눌렸습니다.")
    button_widget.config(text="중단됨", state="disabled")

def run_macro(coord_sets, interval):
    global stop_macro
    print("🚀 메크로 실행을 시작합니다.\n중단 버튼을 누르면 언제든지 종료할 수 있습니다.")

    loop_count = 1
    while not stop_macro:
        print(f"\n🔁 {loop_count}회차 메크로 실행 시작")

        for i, coords in enumerate(coord_sets, start=1):
            if stop_macro:
                break
            print(f"\n▶ {i}세트 실행")
            run_click_sequence(coords)

        if stop_macro:
            break

        print(f"⏳ {interval}초 대기 후 다음 루프 실행...")
        for remaining in range(interval, 0, -1):
            if stop_macro:
                break
            print(f"  다음 실행까지: {remaining}초 남음", end="\r")
            time.sleep(1)

        loop_count += 1

    print("\n✅ 메크로가 종료되었습니다.")
