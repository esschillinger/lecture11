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
        circle = Circle(color=BLUE, radius=1.75)

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
        circle = Circle(color=BLUE, radius=2.63)

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

        self.set_camera_orientation(phi=75*DEGREES, theta=5*DEGREES)

        coordinates_r1 = ParametricFunction(
            lambda t : np.array([
                4 * t,
                0,
                0
            ]), t_min=0, t_max=1, color=BLUE
        )

        coordinates_r = ParametricFunction(
            lambda t : np.array([
                t * (math.sqrt(3) * 2),
                2 * t,
                0
            ]), t_min=0, t_max=1, color=BLUE
        )

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                4 * np.cos(t),
                4 * np.sin(t),
                0
            ]), t_min=0, t_max=PI/6, color=WHITE
        )

        coordinates_s = ParametricFunction(
            lambda t : np.array([
                2 * math.sqrt(3),
                2,
                t
            ]), t_min=0, t_max=2, color=RED
        )

        dashed_r1 = DashedVMobject(coordinates_r1)

        dashed_r = DashedVMobject(coordinates_r)
        dashed_t = DashedVMobject(coordinates_t)
        dashed_s = DashedVMobject(coordinates_s)

        text_t = TextMobject("t", color=WHITE)
        text_r = TextMobject("r", color=BLUE)
        text_s = TextMobject("s", color=RED)

        text_t.move_to(np.array([1/4, -2, 0]))
        text_r.move_to(np.array([-1/2, -1/2, 0]))
        text_s.move_to(np.array([2, 0, 0]))

        self.begin_ambient_camera_rotation()
        self.add_fixed_in_frame_mobjects(text_r)
        self.play(ShowCreation(dashed_r1), Write(text_r))
        self.wait()
        self.play(ShowCreation(dashed_t), Transform(dashed_r1, dashed_r), ReplacementTransform(text_r, text_t))
        self.add_fixed_in_frame_mobjects(text_t)
        self.wait()
        self.play(ShowCreation(dashed_s), ReplacementTransform(text_t, text_s))
        self.add_fixed_in_frame_mobjects(text_s)
        self.wait(2)


class CylinderConversionFactor(Scene):
    def construct(self):
        # TODO : MAKE A MATRIX WITH THE DIFFERENT COMPONENTS AND ANIMATE TO COMPUTE THE CONVERSION FACTOR
        print("TODO")


class SphericalCoordinates(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=5*DEGREES)

        coordinates_r1 = ParametricFunction(
            lambda t : np.array([
                0,
                0,
                3 * t
            ]), t_min=0, t_max=1, color=BLUE
        )

        coordinates_r2 = ParametricFunction(
            lambda t : np.array([
                (math.sqrt(3) * 3 / 2) * t,
                0,
                3 / 2 * t
            ]), t_min=0, t_max=1, color=BLUE
        )

        coordinates_r = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/6) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/6) * np.sin(PI/3)) * t,
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=BLUE
        )

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(t),
                3 * np.sin(t),
                0
            ]), t_min=0, t_max=PI/6, color=WHITE
        )

        coordinates_s1 = ParametricFunction(
            lambda t : np.array([
                (3 * np.sin(t)),
                0,
                (3 * np.cos(t))
            ]), t_min=0, t_max=PI/3, color=RED
        )

        coordinates_s = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/6) * np.sin(t)),
                (3 * np.sin(PI/6) * np.sin(t)),
                (3 * np.cos(t))
            ]), t_min=0, t_max=PI/3, color=RED
        )

        dashed_r1 = DashedVMobject(coordinates_r1)
        dashed_r2 = DashedVMobject(coordinates_r2)

        dashed_s1 = DashedVMobject(coordinates_s1)

        dashed_r = DashedVMobject(coordinates_r)
        dashed_t = DashedVMobject(coordinates_t)
        dashed_s = DashedVMobject(coordinates_s)

        text_t = TextMobject("t", color=WHITE)
        text_r = TextMobject("r", color=BLUE)
        text_s = TextMobject("s", color=RED)

        text_t.move_to(np.array([1/4, -3/2, 0]))
        text_r.move_to(np.array([-3/4, 2, 0]))
        text_s.move_to(np.array([-3/4, 3, 0]))

        self.begin_ambient_camera_rotation()
        self.add_fixed_in_frame_mobjects(text_r)
        self.play(ShowCreation(dashed_r1), Write(text_r))
        self.wait()
        self.play(ShowCreation(dashed_s1), ReplacementTransform(dashed_r1, dashed_r2), ReplacementTransform(text_r, text_s))
        self.add_fixed_in_frame_mobjects(text_s)
        self.wait()
        self.play(ShowCreation(dashed_t), ReplacementTransform(dashed_r2, dashed_r), ReplacementTransform(dashed_s1, dashed_s), ReplacementTransform(text_s, text_t))
        self.add_fixed_in_frame_mobjects(text_t)
        self.wait(2)


class SphereTThenS(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES,theta=15*DEGREES)

        self.add(axes)
        self.begin_ambient_camera_rotation()

        sphere = ParametricSurface(
            lambda u, v: np.array([
                3*np.cos(v)*np.sin(u),
                3*np.sin(v)*np.sin(u),
                3*np.cos(u)
            ]), u_min=0, u_max=PI, v_min=0, v_max=TAU, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32))

        self.play(LaggedStart(ShowCreation(sphere)), run_time=5)
        self.wait(2)

class SphereSThenT(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES,theta=-30*DEGREES)

        self.add(axes)
        self.begin_ambient_camera_rotation()

        sphere = ParametricSurface(
            lambda u, v: np.array([
                3*np.cos(u)*np.sin(v),
                3*np.sin(u)*np.sin(v),
                3*np.cos(v)
            ]), u_min=0, u_max=TAU, v_min=0, v_max=PI, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32))

        self.play(LaggedStart(ShowCreation(sphere)), run_time=5)
        self.wait(2)
