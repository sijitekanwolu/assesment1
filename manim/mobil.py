from manim import *

class MobilBerjalan(Scene):
    def construct(self):
        # Buat badan mobil (kotak)
        body = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=1).shift(UP*0.5)

        # Buat roda mobil (lingkaran)
        roda_kiri = Circle(radius=0.3, color=BLACK, fill_opacity=1).shift(LEFT*1 + DOWN*0.5)
        roda_kanan = Circle(radius=0.3, color=BLACK, fill_opacity=1).shift(RIGHT*1 + DOWN*0.5)

        # Gabungkan komponen menjadi satu objek mobil
        mobil = VGroup(body, roda_kiri, roda_kanan)

        # Mulai dari sisi kiri layar
        mobil.move_to(LEFT * 6)

        # Tampilkan mobil
        self.play(FadeIn(mobil))

        # Animasi: gerakkan mobil ke kanan
        self.play(mobil.animate.shift(RIGHT * 12), run_time=5, rate_func=linear)

        self.wait(1)
