from manim import *
import datetime
import math

class JamAnalog(Scene):
    def construct(self):
        # Buat lingkaran jam
        clock_face = Circle(radius=2)
        self.play(Create(clock_face))

        # Buat angka-angka jam
        for i in range(1, 13):
            angle = math.radians(30 * i - 90)
            x = 1.7 * math.cos(angle)
            y = 1.7 * math.sin(angle)
            number = Text(str(i), font_size=24).move_to([x, y, 0])
            self.play(Write(number), run_time=0.1)

        # Ambil waktu saat ini
        now = datetime.datetime.now()
        jam = now.hour % 12
        menit = now.minute
        detik = now.second

        # Hitung sudut setiap jarum
        angle_hour = math.radians((jam + menit / 60) * 30 - 90)
        angle_minute = math.radians((menit + detik / 60) * 6 - 90)
        angle_second = math.radians(detik * 6 - 90)

        # Buat jarum jam
        hour_hand = Line(ORIGIN, [1 * math.cos(angle_hour), 1 * math.sin(angle_hour), 0], color=BLUE, stroke_width=8)
        minute_hand = Line(ORIGIN, [1.5 * math.cos(angle_minute), 1.5 * math.sin(angle_minute), 0], color=GREEN, stroke_width=5)
        second_hand = Line(ORIGIN, [1.8 * math.cos(angle_second), 1.8 * math.sin(angle_second), 0], color=RED, stroke_width=2)

        self.play(Create(hour_hand), Create(minute_hand), Create(second_hand))

        self.wait(3)  # Tahan tampilan selama 3 detik
