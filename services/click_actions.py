# services/click_actions.py
import pyautogui
import time
import keyboard

def run_click_sequence(coords):
    if len(coords) != 3:
        print("⚠️ 세트는 반드시 3개의 좌표여야 합니다.")
        return

    x1, y1 = coords[0]
    x2, y2 = coords[1]
    x3, y3 = coords[2]

    # 1번 좌표 클릭
    print(f"→ 1번 좌표 클릭: ({x1}, {y1})")
    pyautogui.moveTo(x1, y1)
    pyautogui.click()
    time.sleep(0.3)

    # 'j' 입력
    print("→ 키보드 'j' 입력")
    keyboard.press_and_release('j')
    time.sleep(0.3)

    # 2번 좌표 클릭
    print(f"→ 2번 좌표 클릭: ({x2}, {y2})")
    pyautogui.moveTo(x2, y2)
    pyautogui.click()
    time.sleep(0.3)

    # 3번 좌표 클릭
    print(f"→ 3번 좌표 클릭: ({x3}, {y3})")
    pyautogui.moveTo(x3, y3)
    pyautogui.click()
    time.sleep(0.3)

    # Shift 누른 채 1, 2 키 입력 5회 반복
    print("→ Shift + (1, 2) 키 입력 반복 시작 (5회, 0.5초 간격)")
    keyboard.press('shift')
    for i in range(5):
        keyboard.press_and_release('1')
        time.sleep(0.5)
        keyboard.press_and_release('2')
        time.sleep(0.5)
    keyboard.release('shift')

    # 다시 2번 좌표 클릭
    print(f"→ 2번 좌표 다시 클릭: ({x2}, {y2})")
    pyautogui.moveTo(x2, y2)
    pyautogui.click()
    time.sleep(0.3)
