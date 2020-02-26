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
        circle = Circle(color=BLUE, radius=2.63)

        self.play(Write(circle))


class CylinderHeight(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES)
        self.begin_ambient_camera_rotation()
        base = ParametricFunction(
            lambda t : np.array([
                1.5 * np.cos(t),
                1.5 * np.sin(t),
                0
            ]), t_min=0, t_max=TAU, color=BLUE
        )

        height = ParametricFunction(
            lambda t : np.array([
                1.5 * np.cos(PI/4),
                1.5 * np.sin(PI/4),
                (3 / 4) * t
            ]), t_min=0, t_max=2, color=GREEN
        )

        self.add(base)
        self.play(ShowCreation(height), run_time=5)
        self.wait(2)


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
            ]), u_min=0, u_max=2, v_min=0, v_max=TAU, checkerboard_colors=[GREEN_D, GREEN_E], resolution=(15, 32)
        )

        self.play(ShowCreation(cylinder), run_time=5)
        self.wait(2)


class CylindricalCoordinates(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=5*DEGREES)

        coordinates_r1 = ParametricFunction(
            lambda t : np.array([
                3 * t,
                0,
                0
            ]), t_min=0, t_max=1, color=BLUE
        )

        coordinates_r = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4)) * t,
                (3 * np.sin(PI/4)) * t,
                0
            ]), t_min=0, t_max=1, color=BLUE
        )

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(t),
                3 * np.sin(t),
                0
            ]), t_min=0, t_max=PI/4, color=WHITE
        )

        coordinates_s = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(PI/4),
                3 * np.sin(PI/4),
                (3 / 4) * t
            ]), t_min=0, t_max=2, color=GREEN
        )

        text_t = TextMobject("t", color=WHITE)
        text_r = TextMobject("r", color=BLUE)
        text_s = TextMobject("s", color=GREEN)

        text_t.move_to(np.array([1/4, -3/2, 0]))
        text_r.move_to(np.array([-1/2, -1/2, 0]))
        text_s.move_to(np.array([9/4, 0, 0]))

        self.begin_ambient_camera_rotation()
        self.add_fixed_in_frame_mobjects(text_r)
        self.play(ShowCreation(coordinates_r1), Write(text_r))
        self.wait()
        self.play(ShowCreation(coordinates_t), Transform(coordinates_r1, coordinates_r), ReplacementTransform(text_r, text_t))
        self.add_fixed_in_frame_mobjects(text_t)
        self.wait()
        self.play(ShowCreation(coordinates_s), ReplacementTransform(text_t, text_s))
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
            ]), t_min=0, t_max=1, color=PINK
        )

        coordinates_r2 = ParametricFunction(
            lambda t : np.array([
                (math.sqrt(3) * 3 / 2) * t,
                0,
                3 / 2 * t
            ]), t_min=0, t_max=1, color=PINK
        )

        coordinates_r = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=PINK
        )

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(t),
                3 * np.sin(t),
                0
            ]), t_min=0, t_max=PI/4, color=WHITE
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
                (3 * np.cos(PI/4) * np.sin(t)),
                (3 * np.sin(PI/4) * np.sin(t)),
                (3 * np.cos(t))
            ]), t_min=0, t_max=PI/3, color=RED
        )

        text_t = TextMobject("t", color=WHITE)
        text_r = TextMobject("r", color=PINK)
        text_s = TextMobject("s", color=RED)

        text_t.move_to(np.array([1/4, -3/2, 0]))
        text_r.move_to(np.array([-3/4, 3/2, 0]))
        text_s.move_to(np.array([-3/4, 9/4, 0]))

        self.begin_ambient_camera_rotation()
        self.add_fixed_in_frame_mobjects(text_r)
        self.play(ShowCreation(coordinates_r1), Write(text_r))
        self.wait()
        self.play(ShowCreation(coordinates_s1), ReplacementTransform(coordinates_r1, coordinates_r2), ReplacementTransform(text_r, text_s))
        self.add_fixed_in_frame_mobjects(text_s)
        self.wait()
        self.play(ShowCreation(coordinates_t), ReplacementTransform(coordinates_r2, coordinates_r), ReplacementTransform(coordinates_s1, coordinates_s), ReplacementTransform(text_s, text_t))
        self.add_fixed_in_frame_mobjects(text_t)
        self.wait(2)


class CombinedCoordinates(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=13*DEGREES)

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(t) * np.sin(PI/3),
                3 * np.sin(t) * np.sin(PI/3),
                0
            ]), t_min=0, t_max=PI/4, color=WHITE
        )

        coordinates_s_sphere = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(t)),
                (3 * np.sin(PI/4) * np.sin(t)),
                (3 * np.cos(t))
            ]), t_min=0, t_max=PI/3, color=RED
        )

        coordinates_s_cylinder = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(PI/4) * np.sin(PI/3),
                3 * np.sin(PI/4) * np.sin(PI/3),
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=GREEN
        )

        coordinates_r_sphere = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=PINK
        )

        coordinates_r_cylinder = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                0
            ]), t_min=0, t_max=1, color=BLUE
        )

        self.play(ShowCreation(coordinates_t), ShowCreation(coordinates_s_sphere), ShowCreation(coordinates_s_cylinder), ShowCreation(coordinates_r_sphere), ShowCreation(coordinates_r_cylinder))


class CombinedCoordinatesHighlighted(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=13*DEGREES)

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(t) * np.sin(PI/3),
                3 * np.sin(t) * np.sin(PI/3),
                0
            ]), t_min=0, t_max=PI/4
        )

        coordinates_s_sphere = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(t)),
                (3 * np.sin(PI/4) * np.sin(t)),
                (3 * np.cos(t))
            ]), t_min=0, t_max=PI/3
        )

        coordinates_s_cylinder = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(PI/4) * np.sin(PI/3),
                3 * np.sin(PI/4) * np.sin(PI/3),
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=GOLD
        )

        coordinates_r_sphere = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=GOLD
        )

        coordinates_r_cylinder = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                0
            ]), t_min=0, t_max=1, color=GOLD
        )

        self.play(ShowCreation(coordinates_t), ShowCreation(coordinates_s_sphere), ShowCreation(coordinates_s_cylinder), ShowCreation(coordinates_r_sphere), ShowCreation(coordinates_r_cylinder))


class CombinedCoordinatesOrthogonal(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=90*DEGREES, theta=-45*DEGREES)

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(t) * np.sin(PI/3),
                3 * np.sin(t) * np.sin(PI/3),
                0
            ]), t_min=0, t_max=PI/4, color=WHITE
        )

        coordinates_s_sphere = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(t)),
                (3 * np.sin(PI/4) * np.sin(t)),
                (3 * np.cos(t))
            ]), t_min=0, t_max=PI/3, color=RED
        )

        coordinates_s_cylinder = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(PI/4) * np.sin(PI/3),
                3 * np.sin(PI/4) * np.sin(PI/3),
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=GREEN
        )

        coordinates_r_sphere = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=PINK
        )

        coordinates_r_cylinder = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                0
            ]), t_min=0, t_max=1, color=BLUE
        )

        self.play(ShowCreation(coordinates_t), ShowCreation(coordinates_s_sphere), ShowCreation(coordinates_s_cylinder), ShowCreation(coordinates_r_sphere), ShowCreation(coordinates_r_cylinder))


class OrthogonalTransform(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=90*DEGREES, theta=-45*DEGREES)

        coordinates_s1_sphere = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(t)),
                (3 * np.sin(PI/4) * np.sin(t)),
                (3 * np.cos(t))
            ]), t_min=0, t_max=PI/3, color=RED
        )

        coordinates_s_sphere = ParametricFunction(
            lambda t : np.array([
                ((1 / 2) * np.cos(PI/4) * np.sin(t)),
                ((1 / 2) * np.sin(PI/4) * np.sin(t)),
                ((1 / 2) * np.cos(t))
            ]), t_min=0, t_max=PI/3, color=RED
        )

        coordinates_s1_cylinder = ParametricFunction(
            lambda t : np.array([
                3 * np.cos(PI/4) * np.sin(PI/3),
                3 * np.sin(PI/4) * np.sin(PI/3),
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=GREEN
        )

        coordinates_s_cylinder = ParametricFunction(
            lambda t : np.array([
                0,
                0,
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=GREEN
        )

        coordinates_r_sphere = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                (3 * np.cos(PI/3)) * t
            ]), t_min=0, t_max=1, color=PINK
        )

        coordinates_r1_cylinder = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                0
            ]), t_min=0, t_max=1, color=BLUE
        )

        coordinates_r_cylinder = ParametricFunction(
            lambda t : np.array([
                (3 * np.cos(PI/4) * np.sin(PI/3)) * t,
                (3 * np.sin(PI/4) * np.sin(PI/3)) * t,
                3 * np.cos(PI/3)
            ]), t_min=0, t_max=1, color=BLUE
        )

        text_s1 = TexMobject(r"s_1", color=GREEN)
        text_s2 = TexMobject(r"s_2", color=RED)
        text_r1 = TexMobject(r"r_1", color=BLUE)
        text_r2 = TexMobject(r"r_2", color=PINK)

        text_s1.move_to([-1/2, 3/4, 0])
        text_s2.move_to([1/2, 3/4, 0])
        text_r1.move_to([5/4, 7/4, 0])
        text_r2.move_to([3/2, 2/5, 0])

        self.play(ShowCreation(coordinates_s1_sphere), ShowCreation(coordinates_s1_cylinder), ShowCreation(coordinates_r_sphere), ShowCreation(coordinates_r1_cylinder))
        self.wait()
        self.play(ReplacementTransform(coordinates_r1_cylinder, coordinates_r_cylinder), ReplacementTransform(coordinates_s1_cylinder, coordinates_s_cylinder), ReplacementTransform(coordinates_s1_sphere, coordinates_s_sphere), run_time=3)
        self.wait()
        self.add_fixed_in_frame_mobjects(text_s1, text_s2, text_r1, text_r2)
        self.play(Write(text_s1), Write(text_s2), Write(text_r1), Write(text_r2))
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
        self.set_camera_orientation(phi=75*DEGREES,theta=-60*DEGREES)

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


class SphereToCube(ThreeDScene):
    def construct(self):
        sphere = Sphere(radius=1.3, checkerboard_colors=[RED_E, RED_E])
        cube = Cube(fill_color=PURPLE_A)

        self.set_camera_orientation(phi=60*DEGREES, distance=2.5)
        self.begin_ambient_camera_rotation(rate=0.2)

        self.play(ShowCreation(sphere))
        self.wait(2)
        self.play(ReplacementTransform(sphere, cube))
        self.wait(2)
