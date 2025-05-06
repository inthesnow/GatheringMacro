# capture_coords.py
import pyautogui
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime

def collect_coordinates(num_clicks, master):
    click_points = []

    def on_click(event):
        x, y = event.x, event.y
        click_points.append((x, y))
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] 클릭 {len(click_points)}/{num_clicks}: ({x}, {y})")
        if len(click_points) == num_clicks:
            top.destroy()

    # 스크린샷 캡처
    screenshot = pyautogui.screenshot()
    img = screenshot.copy()
    photo = ImageTk.PhotoImage(img, master=master)

    # Toplevel 창 생성 (루트와 독립된 창)
    top = tk.Toplevel(master)
    top.overrideredirect(True)
    top.attributes("-topmost", True)

    canvas = tk.Canvas(top, width=img.width, height=img.height)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo  # 이미지 참조 유지

    canvas.bind("<Button-1>", on_click)
    top.grab_set()  # 이 창에 포커스 고정
    master.wait_window(top)  # 창이 닫힐 때까지 대기

    return click_points
