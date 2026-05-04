import tkinter as tk
from tkinter import messagebox
import winsound # For Windows alert sound

# Experience table for Old Maple (Level 1 to 200)
EXP_TABLE = {
    1: 15, 2: 34, 3: 57, 4: 92, 5: 135, 6: 372, 7: 560, 8: 840, 9: 1242, 10: 1716,
    11: 2360, 12: 3216, 13: 4200, 14: 5460, 15: 7050, 16: 8840, 17: 11040, 18: 13716, 19: 16680, 20: 20216,
    21: 24402, 22: 28980, 23: 34320, 24: 40512, 25: 47216, 26: 54900, 27: 63666, 28: 73080, 29: 83720, 30: 95700,
    31: 108480, 32: 122760, 33: 138666, 34: 155540, 35: 174216, 36: 194832, 37: 216600, 38: 240500, 39: 266682, 40: 294216,
    41: 324240, 42: 356916, 43: 391160, 44: 428280, 45: 468450, 46: 510420, 47: 555680, 48: 604416, 49: 655200, 50: 709716,
    51: 748608, 52: 789631, 53: 832902, 54: 878545, 55: 926689, 56: 977471, 57: 1031036, 58: 1087536, 59: 1147132, 60: 1209994,
    61: 1276301, 62: 1346242, 63: 1420016, 64: 1497832, 65: 1579913, 66: 1666492, 67: 1757815, 68: 1854143, 69: 1955750, 70: 2062925,
    71: 2175973, 72: 2295216, 73: 2420993, 74: 2553663, 75: 2693603, 76: 2841212, 77: 2996910, 78: 3161140, 79: 3334370, 80: 3517093,
    81: 3709829, 82: 3913127, 83: 4127566, 84: 4353756, 85: 4592341, 86: 4844001, 87: 5109452, 88: 5389449, 89: 5684790, 90: 5996316,
    91: 6324914, 92: 6671519, 93: 7037118, 94: 7422752, 95: 7829518, 96: 8258575, 97: 8711144, 98: 9188514, 99: 9692044, 100: 10223168,
    101: 10783397, 102: 11374327, 103: 11997640, 104: 12655110, 105: 13348610, 106: 14080113, 107: 14851703, 108: 15665576, 109: 16524049, 110: 17429566,
    111: 18384706, 112: 19392187, 113: 20454878, 114: 21575805, 115: 22758159, 116: 24005306, 117: 25320796, 118: 26708375, 119: 28171993, 120: 29715818,
    121: 31344244, 122: 33061908, 123: 34873700, 124: 36784778, 125: 38800583, 126: 40926854, 127: 43169645, 128: 45535341, 129: 48030677, 130: 50662758,
    131: 53439077, 132: 56367538, 133: 59456479, 134: 62714694, 135: 66151459, 136: 69776558, 137: 73600313, 138: 77633610, 139: 81887931, 140: 86375389,
    141: 91108760, 142: 96101520, 143: 101367883, 144: 106922842, 145: 112782213, 146: 118962678, 147: 125481832, 148: 132358236, 149: 139611467, 150: 147262175,
    151: 155332142, 152: 163844343, 153: 172823012, 154: 182293713, 155: 192283408, 156: 202820538, 157: 213935103, 158: 225658746, 159: 238024845, 160: 251068606,
    161: 264827165, 162: 279339693, 163: 294647508, 164: 310794191, 165: 327825712, 166: 345790561, 167: 364739883, 168: 384727628, 169: 405810702, 170: 428049128,
    171: 451506220, 172: 476248760, 173: 502347192, 174: 529875818, 175: 558913012, 176: 589541445, 177: 621848316, 178: 655925603, 179: 691870326, 180: 729784819,
    181: 769777027, 182: 811960808, 183: 856456260, 184: 903390063, 185: 952895838, 186: 1005114529, 187: 1060194805, 188: 1118293480, 189: 1179575962, 190: 1244216724,
    191: 1312399800, 192: 1384319309, 193: 1460180007, 194: 1540197871, 195: 1624600714, 196: 1713628833, 197: 1807535693, 198: 1906588648, 199: 2011069705, 200: 2121276324
}

class MapleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("플래닛 레벨업 계산기 by Raeyu")
        self.root.geometry("350x700") # Height increased for new button
        self.root.resizable(False, False)

        # --- Top: Calculator Section ---
        tk.Label(root, text="[ 레벨업 계산기 ]", font=("맑은 고딕", 12, "bold")).pack(pady=15)
        
        input_frame = tk.Frame(root)
        input_frame.pack()

        self.create_input(input_frame, "현재 레벨:", "ent_cur_lv", 0, "1") #currnet level
        self.create_input(input_frame, "목표 레벨:", "ent_tar_lv", 1, "2") #Goal level
        self.create_input(input_frame, "현재 보유 경험치 (%):", "ent_cur_pct", 2, "0")
        self.create_input(input_frame, "10분당 획득 경험치:", "ent_rate", 3, "0")

        self.btn_calc = tk.Button(root, text="계산하기", width=20, bg="#f0f0f0", command=self.calculate)
        self.btn_calc.pack(pady=15)

        self.lbl_result = tk.Label(root, text="결과가 여기에 표시됩니다.", fg="blue", font=("맑은 고딕", 10))
        self.lbl_result.pack()

        tk.Label(root, text="-"*40, fg="gray").pack(pady=15)

        # --- Bottom: Timer Section ---
        tk.Label(root, text="[ 10분 사냥 타이머 ]", font=("맑은 고딕", 12, "bold")).pack(pady=5)
        
        self.remain_sec = 600
        self.is_running = False
        self.timer_id = None

        self.lbl_timer = tk.Label(root, text="10:00", font=("Consolas", 40, "bold"), fg="#e74c3c")
        self.lbl_timer.pack(pady=10)

        timer_btn_frame = tk.Frame(root)
        timer_btn_frame.pack()

        self.btn_start = tk.Button(timer_btn_frame, text="시작 (Start)", width=10, command=self.toggle_timer)
        self.btn_start.pack(side=tk.LEFT, padx=5)

        self.btn_reset = tk.Button(timer_btn_frame, text="초기화 (Reset)", width=10, command=self.reset_timer)
        self.btn_reset.pack(side=tk.LEFT, padx=5)

        # --- NEW: Cheer Button Section ---
        self.btn_cheer = tk.Button(root, text="화이팅", width=22, bg="#FFF9C4", command=self.show_cheer)
        self.btn_cheer.pack(pady=20)

    def create_input(self, frame, label_text, var_name, row, default_val):
        tk.Label(frame, text=label_text).grid(row=row, column=0, sticky="e", pady=5)
        entry = tk.Entry(frame)
        entry.insert(0, default_val)
        entry.grid(row=row, column=1, padx=5)
        setattr(self, var_name, entry)

    def calculate(self):
        try:
            cur_lv = int(self.ent_cur_lv.get())
            tar_lv = int(self.ent_tar_lv.get())
            cur_pct = int(self.ent_cur_pct.get())
            rate = int(self.ent_rate.get())

            if not (0 <= cur_pct <= 99):
                messagebox.showwarning("오류", "경험치 퍼센트는 0에서 99 사이여야 합니다.")
                return

            if cur_lv >= tar_lv:
                messagebox.showwarning("오류", "목표 레벨은 현재보다 커야 합니다.")
                return

            exp_from_pct = EXP_TABLE.get(cur_lv, 0) * (cur_pct / 100)
            total_req = sum(EXP_TABLE.get(lv, 0) for lv in range(cur_lv, tar_lv))
            final_needed = total_req - exp_from_pct

            if rate <= 0:
                messagebox.showwarning("오류", "경험치 획득량은 0보다 커야 합니다.")
                return

            total_mins = (final_needed / rate) * 10
            h = int(total_mins // 60)
            m = int(total_mins % 60)

            self.lbl_result.config(text=f"필요 경험치: {int(final_needed):,}\n예상 소요 시간: {h}시간 {m}분")
        except ValueError:
            messagebox.showerror("오류", "숫자만 입력해주세요.")

    def toggle_timer(self):
        if self.is_running: self.stop_timer()
        else: self.start_timer()

    def start_timer(self):
        self.is_running = True
        self.btn_start.config(text="정지 (Stop)")
        self.update_timer()

    def stop_timer(self):
        self.is_running = False
        self.btn_start.config(text="시작 (Start)")
        if self.timer_id: self.root.after_cancel(self.timer_id)

    def update_timer(self):
        if self.is_running and self.remain_sec > 0:
            self.remain_sec -= 1
            mins, secs = divmod(self.remain_sec, 60)
            self.lbl_timer.config(text=f"{mins:02d}:{secs:02d}")
            self.timer_id = self.root.after(1000, self.update_timer)
        elif self.remain_sec <= 0:
            self.stop_timer()
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
            messagebox.showinfo("완료", "10분 사냥 측정이 끝났습니다!")

    def reset_timer(self):
        self.stop_timer()
        self.remain_sec = 600
        self.lbl_timer.config(text="10:00")

    def show_cheer(self):
        # NEW: Fun cheer message
        messagebox.showinfo("comment!", "Comment!")

if __name__ == "__main__":
    window = tk.Tk()
    app = MapleApp(window)
    window.mainloop()