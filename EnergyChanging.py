from manim import *
class EnergyScene(Scene):
    def construct(self):
        energies=VGroup(
            Tex('Energía').scale(1.3),
            Tex('Energía Potencial Gravitatoria'),
            Tex('Energia Potencial Elástica'),
            Tex('Energía Potencial Eléctrica'),
            Tex('Energía Potencial Magnética'),
            Tex('Energía Potencial Química'),
            Tex('Energía Cinética'),
        ).arrange(DOWN)
        ul=Underline(energies[0])
        self.play(Write(energies[0]),run_time=3)
        self.wait(2)
        for mob in energies[1:]:
            self.play(TransformFromCopy(energies[0], mob), run_time=3)
            self.add(mob)
            self.wait(2)
        self.wait()