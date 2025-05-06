# get_interval.py
import tkinter as tk
from datetime import datetime

def get_interval_seconds():
    interval_value = None

    def validate_input(value_if_allowed):
        return value_if_allowed.isdigit() or value_if_allowed == ""

    def on_confirm():
        nonlocal interval_value
        value = entry.get()
        if value.isdigit() and int(value) > 0:
            interval_value = int(value)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] ⏱️ 입력된 주기: {interval_value}초")
            window.destroy()
        else:
            label.config(text="⚠️ 양의 정수를 입력해주세요")

    window = tk.Tk()
    window.title("주기 입력")

    label = tk.Label(window, text="주기를 입력해주세요 (초 단위):")
    label.pack(pady=10)

    vcmd = (window.register(validate_input), '%P')
    entry = tk.Entry(window, validate='key', validatecommand=vcmd)
    entry.pack(pady=5)
    entry.focus()

    button = tk.Button(window, text="확인", command=on_confirm)
    button.pack(pady=10)

    window.mainloop()

    return interval_value
