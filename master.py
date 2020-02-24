from manimlib.imports import *
from math import sqrt

class UnitCircle(GraphScene):
    CONFIG = {
        "x_min" : -2,
        "x_max" : 2,
        "y_min" : -2,
        "y_max" : 2,
        "x_axis_width" : 7,
        "y_axis_height" : 7,
        "x_tick_frequency" : 1,
        "y_tick_frequency" : 1,
        "graph_origin" : np.array((0, 0, 0))
    }

    def construct(self):
        self.setup_axes()
        circle = Circle(color=WHITE, radius=1.75)

        self.play(Write(circle))


class UnitCircle2(GraphScene):
    CONFIG = {
        "x_min" : -2,
        "x_max" : 2,
        "y_min" : -2,
        "y_max" : 2,
        "x_axis_width" : 7,
        "y_axis_height" : 7,
        "x_tick_frequency" : 1,
        "y_tick_frequency" : 1,
        "graph_origin" : np.array((0, 0, 0))
    }

    def construct(self):
        self.setup_axes()
        circle = Circle(color=RED, radius=2.63)

        self.play(Write(circle))


class Cylinder(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES)
        self.begin_ambient_camera_rotation()
        cylinder = ParametricSurface(
            lambda u, v : np.array([
                1.5 * np.cos(v),
                1.5 * np.sin(v),
                u
            ]), u_min=0, u_max=2, v_min=0, v_max=TAU, checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)
        )

        self.play(ShowCreation(cylinder), run_time=3)
        self.wait(2)


class CylindricalCoordinates(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=15*DEGREES)

        coordinates_r = ParametricFunction(
            lambda t : np.array([
                t * (math.sqrt(3) * 2),
                2 * t,
                0
            ]), t_min=0, t_max=1, color=RED
        )

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                4 * np.cos(t),
                4 * np.sin(t),
                0
            ]), t_min=0, t_max=PI/6, color=RED
        )

        coordinates_s = ParametricFunction(
            lambda t : np.array([
                2 * math.sqrt(3),
                2,
                t
            ]), t_min=0, t_max=2, color=RED
        )

        dashed_r = DashedVMobject(coordinates_r)
        dashed_t = DashedVMobject(coordinates_t)
        dashed_s = DashedVMobject(coordinates_s)

        # text_begin = TextMobject("t")
        # text_middle = TextMobject("r")
        # text_end = TextMobject("s")

        # self.add_fixed_in_frame_mobjects(text_begin)
        # text_begin.move_to(np.array([0, -2, 0]))
        # self.add_fixed_in_frame_mobjects(text_middle)
        # text_middle.move_to(np.array([3/4, -1/4, 0]))
        # self.add_fixed_in_frame_mobjects(text_end)
        # text_end.move_to(np.array([7/4, 0, 0]))

        # self.add_fixed_in_frame_mobjects(text_middle)
        # text_middle.move_to(UL)

        # self.add_fixed_in_frame_mobjects(text_end)
        # text_end.move_to(UL)

        self.play(ShowCreation(dashed_t))
        self.play(Write(TextMobject("t").move_to(np.array([0, -2, 0]))))
        self.wait()
        self.play(ShowCreation(dashed_r))
        self.play(Write(TextMobject("r").move_to(np.array([3/4, -1/4, 0]))))
        self.wait()
        self.play(ShowCreation(dashed_s))
        self.play(Write(TextMobject("s").move_to(np.array([7/4, 0, 0]))))
        self.wait(2)
