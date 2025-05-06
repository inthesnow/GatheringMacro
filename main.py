# main.py
import threading
import tkinter as tk
from tkinter import messagebox
from capture_coords import collect_coordinates
from get_interval import get_interval_seconds
from services.macro_runner import run_macro, on_stop

if __name__ == "__main__":
    # Tk 루트 창 생성 및 숨김
    root = tk.Tk()
    root.withdraw()

    # 1. 주기 입력
    print("🕒 주기를 입력 받습니다...")
    interval = get_interval_seconds()
    if interval is None:
        print("❌ 주기 입력이 취소되어 프로그램을 종료합니다.")
        root.destroy()
        exit()

    # 2. 진행 여부 확인
    proceed = messagebox.askyesno(
        "진행 확인",
        "📌 메크로를 계속 진행하시겠습니까?\n(취소 시 프로그램이 종료됩니다)"
    )
    if not proceed:
        print("🛑 사용자가 진행을 취소했습니다. 프로그램을 종료합니다.")
        root.destroy()
        exit()

    # 3. 좌표 수집
    print("🔍 좌표 수집을 시작합니다. 3회에 걸쳐 3개씩 총 9개의 좌표를 클릭하세요.")
    coord_sets = []
    for round_num in range(1, 4):
        print(f"\n🖱️ {round_num}번째 클릭 세트를 수집합니다...")
        coords = collect_coordinates(3, root)
        coord_sets.append(coords)

        group_str = ", ".join(f"({x}, {y})" for x, y in coords)
        print(f"{round_num}set {group_str}")

        if round_num < 3:
            confirm_next = messagebox.askyesno(
                "다음 세트 확인",
                f"{round_num + 1}번째 좌표 세트를 계속 수집하시겠습니까?"
            )
            if not confirm_next:
                print("🛑 사용자가 수집을 중단했습니다. 현재까지 수집된 세트만으로 메크로를 실행합니다.")
                break

    # 4. 중단 버튼 GUI 다시 활성화
    root.deiconify()
    root.title("메크로 중단")
    root.geometry("200x100")

    stop_button = tk.Button(
        root,
        text="중단",
        command=lambda: on_stop(stop_button),
        height=2,
        width=10,
        bg="red",
        fg="white"
    )
    stop_button.pack(expand=True)

    # 5. 백그라운드에서 매크로 실행
    threading.Thread(target=run_macro, args=(coord_sets, interval), daemon=True).start()

    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("🛑 프로그램이 사용자에 의해 종료되었습니다.")