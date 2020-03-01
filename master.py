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

        self.add(coordinates_s1_sphere, coordinates_s1_cylinder, coordinates_r_sphere, coordinates_r1_cylinder)
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


class AngleTThenS(ThreeDScene):
    def construct(self):
        degree_num_t = DecimalNumber(0, num_decimal_places=0)
        time_0 = ValueTracker(0)
        degree_num_t.add_updater(lambda num:num.set_value(time_0.get_value()))

        degree_num_s = DecimalNumber(0, num_decimal_places=0)
        time_1 = ValueTracker(0)
        degree_num_s.add_updater(lambda num:num.set_value(time_1.get_value()))

        degree_num_t.to_corner(UL + [-2, 0, 0])
        degree_num_s.move_to(degree_num_t.get_center() + [0, -3/4, 0])

        text_t = TextMobject("t:")
        text_s = TextMobject("s:")

        text_t.next_to(degree_num_t, LEFT)
        text_s.next_to(degree_num_s, LEFT)

        self.add_fixed_in_frame_mobjects(degree_num_t, degree_num_s, text_t, text_s)

        duration_t = 1.15

        self.play(
            ApplyMethod(time_0.increment_value, 360, rate_func=smooth, run_time=duration_t)
        )
        self.play(
            ApplyMethod(time_1.increment_value, 180, rate_func=smooth, run_time=5-1-duration_t)
        )
        self.wait(3)


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


class AngleSThenT(ThreeDScene):
    def construct(self):
        degree_num_s = DecimalNumber(0, num_decimal_places=0)
        time_0 = ValueTracker(0)
        degree_num_s.add_updater(lambda num:num.set_value(time_0.get_value()))

        degree_num_t = DecimalNumber(0, num_decimal_places=0)
        time_1 = ValueTracker(0)
        degree_num_t.add_updater(lambda num:num.set_value(time_1.get_value()))

        degree_num_s.to_corner(UL + [-2, 0, 0])
        degree_num_t.move_to(degree_num_s.get_center() + [0, -3/4, 0])

        text_s = TextMobject("s:")
        text_t = TextMobject("t:")

        text_s.next_to(degree_num_s, LEFT)
        text_t.next_to(degree_num_t, LEFT)

        self.add_fixed_in_frame_mobjects(degree_num_s, degree_num_t, text_s, text_t)

        duration_s = 1.15

        self.play(
            ApplyMethod(time_0.increment_value, 180, rate_func=smooth, run_time=duration_s)
        )
        self.play(
            ApplyMethod(time_1.increment_value, 360, rate_func=smooth, run_time=5-1-duration_s)
        )
        self.wait(3)


class BadS(ThreeDScene):
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
            ]), u_min=0, u_max=TAU, v_min=0, v_max=TAU, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32))

        self.play(LaggedStart(ShowCreation(sphere)), run_time=5)
        self.wait(2)


class AngleBadSThenT(ThreeDScene):
    def construct(self):
        degree_num_s = DecimalNumber(0, num_decimal_places=0)
        time_0 = ValueTracker(0)
        degree_num_s.add_updater(lambda num:num.set_value(time_0.get_value()))

        degree_num_t = DecimalNumber(0, num_decimal_places=0)
        time_1 = ValueTracker(0)
        degree_num_t.add_updater(lambda num:num.set_value(time_1.get_value()))

        degree_num_s.to_corner(UL + [-2, 0, 0])
        degree_num_t.move_to(degree_num_s.get_center() + [0, -3/4, 0])

        text_s = TextMobject("s:")
        text_t = TextMobject("t:")

        text_s.next_to(degree_num_s, LEFT)
        text_t.next_to(degree_num_t, LEFT)

        self.add_fixed_in_frame_mobjects(degree_num_s, degree_num_t, text_s, text_t)

        duration_s = 1.15

        self.play(
            ApplyMethod(time_0.increment_value, 360, rate_func=smooth, run_time=duration_s)
        )
        self.play(
            ApplyMethod(time_1.increment_value, 360, rate_func=smooth, run_time=5-1-duration_s)
        )
        self.wait(3)


class ChangeOfCoords(Scene):
    def construct(self):
        description_0 = TextMobject("Cylindrical Coordinates")
        description_0.to_corner(UL)

        #cylindrical = TexMobject("\\DeclarePairedDelimiter\\set\\{ x[r_1, s_1, t], y[r_1, s_1, t], z[r_1, s_1, t] \\} = \\DeclarePairedDelimiter\\set\\{ ", "r_1","Cos[t],", "r_1", "Sin[t],", "s_1", " \\}")
        #cylindrical[1].set_color(BLUE)
        #cylindrical[3].set_color(BLUE)
        #cylindrical[5].set_color(GREEN)

        cylindrical_0 = TexMobject("\\{x[r_1, s_1, t], y[r_1, s_1, t], z[r_1, s_1, t]\\} = \\{r_1 Cos[t], r_1 Sin[t], s_1\\}")
        cylindrical_1 = TexMobject("\\{x[r_1, s_1, t], y[r_1, s_1, t], z[r_1, s_1, t]\\} = \\{r_1 Cos[t], r_1 Sin[t], s_1\\}")

        cylindrical_1.move_to(UP)

        self.add(description_0)
        self.add(cylindrical_0)
        self.wait(2)
        self.play(Transform(cylindrical_0, cylindrical_1), run_time=2)
        self.wait()


class CylinderToSphere(ThreeDScene):
    def construct(self):
        # THIS ANIMATION SHOULD PLAY DIRECTLY AFTER THE TRIGONOMETRIC CONVERSION FROM CYLINDRICAL TO SPHERICAL IS COMPLETE
        # The animation is mostly for fun, tbh... I just want to have a cool-looking anim in there so that people are impressed :D
        # It doesn't have any intrinsic teaching value, just looks nice--adding it because Logan said he liked the SphereSThenT anim
        # And Jack thought the 3D ReplacementTransform was satisfying, so I'll incorporate ReplacementTransform in a relevant way (THIS!)

        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES,theta=-60*DEGREES)

        self.add(axes)
        self.begin_ambient_camera_rotation()

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        cylinder = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(TAU * v),
                1.5*np.sin(TAU * v),
                3 * (1 - u)
            ]), checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(6, 32))#.fade(0.5)

        self.add(cylinder)
        self.wait(2)
        self.play(ReplacementTransform(cylinder, sphere), run_time=3)
        self.wait(2)


class CylinderToSphereMappings(Scene):
    def construct(self):
        c_x = TextMobject("x[r, s, t] = r Cos[t]").scale(0.9)
        c_y = TextMobject("y[r, s, t] = r Sin[t]").scale(0.9)
        c_z = TextMobject("z[r, s, t] = s").scale(0.9)

        s_x = TextMobject("x[r, s, t] = r Cos[t] Sin[s]").scale(0.9)
        s_y = TextMobject("y[r, s, t] = r Sin[t] Sin[s]").scale(0.9)
        s_z = TextMobject("z[r, s, t] = r Cos[s]").scale(0.9)

        c_x.move_to([-4.95, 3.5, 0])
        c_y.move_to([-5, 2.5, 0])
        c_z.move_to([-5.6, 1.5, 0])

        s_x.move_to([-4.45, 3.5, 0])
        s_y.move_to([-4.5, 2.5, 0])
        s_z.move_to([-5.05, 1.5, 0])

        self.add(c_x, c_y, c_z)
        self.wait(2)
        self.play(
            ReplacementTransform(c_x, s_x), ReplacementTransform(c_y, s_y), ReplacementTransform(c_z, s_z), run_time=3
        )
        self.wait(2)
