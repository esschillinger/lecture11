from manimlib.imports import *

class TestTransform(ThreeDScene):
    def construct(self):
        t1 = TextMobject("t")
        t2 = TextMobject("r")
        t3 = TextMobject("s")

        self.add_fixed_in_frame_mobjects(t1)
        # self.add_fixed_in_frame_mobjects(t3)
        # self.add_fixed_in_frame_mobjects(t2)

        self.play(Write(t1))
        self.wait()
        self.play(ReplacementTransform(t1, t2))
        self.wait()
        self.play(ReplacementTransform(t2, t3))


class VisualizationTest(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=25*DEGREES)

        radians = PI/180

        coordinates_r1 = ParametricFunction(
            lambda t : np.array([
                0,
                0,
                2.5 * t
            ]), t_min=0, t_max=1, color=PINK
        )

        coordinates_r2 = ParametricFunction(
            lambda t : np.array([
                t * np.cos(0) * np.sin(PI/6),
                t * np.sin(0) * np.sin(PI/6),
                t * np.cos(PI/6)
            ]), t_min=0, t_max=2.5, color=PINK
        )

        coordinates_r = ParametricFunction(
            lambda t : np.array([
                (2.5 * np.cos(PI/4) * np.sin(PI/6)) * t,
                (2.5 * np.sin(PI/4) * np.sin(PI/6)) * t,
                (2.5 * np.cos(PI/6)) * t
            ]), t_min=0, t_max=1, color=PINK
        )

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                2.5 * np.cos(t),
                2.5 * np.sin(t),
                0
            ]), t_min=0, t_max=PI/4, color=WHITE
        )

        coordinates_s1 = ParametricFunction(
            lambda t : np.array([
                (2.5 * np.sin(t)),
                0,
                (2.5 * np.cos(t))
            ]), t_min=0, t_max=PI/6, color=RED
        )

        coordinates_s = ParametricFunction(
            lambda t : np.array([
                (2.5 * np.cos(PI/4) * np.sin(t)),
                (2.5 * np.sin(PI/4) * np.sin(t)),
                (2.5 * np.cos(t))
            ]), t_min=0, t_max=PI/6, color=RED
        )

        cone = ParametricSurface(
            lambda u, v : np.array([
                u * np.cos(v) * np.sin(PI/6),
                u * np.sin(v) * np.sin(PI/6),
                u * np.cos(PI/6)
            ]), u_min=0, u_max=2.5, v_min=0, v_max=TAU, checkerboard_colors=[YELLOW_D, YELLOW_E]
        )

        angle = DecimalNumber(0, num_decimal_places=0)
        time = ValueTracker(0)
        angle.add_updater(lambda num:num.set_value(time.get_value()))

        self.play(ShowCreation(coordinates_r2), ShowCreation(coordinates_s1))
        self.wait()

        #self.begin_ambient_camera_rotation()

        #self.play(ShowCreation(coordinates_r1))
        #self.wait()
        #self.play(ShowCreation(coordinates_s1), ReplacementTransform(coordinates_r1, coordinates_r2))
        #self.wait()
        #self.play(ShowCreation(coordinates_t), ReplacementTransform(coordinates_r2, coordinates_r), ReplacementTransform(coordinates_s1, coordinates_s))
        #self.remove(coordinates_s1, coordinates_r2)
        #self.play(ShowCreation(cone))
        #self.wait(2)


class TRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=25*DEGREES)

        coordinates_s1 = ParametricFunction(
            lambda t : np.array([
                (2.5 * np.sin(t)),
                0,
                (2.5 * np.cos(t))
            ]), t_min=0, t_max=PI/6, color=RED
        )

        coordinates_r2 = ParametricFunction(
            lambda t : np.array([
                t * np.cos(0) * np.sin(PI/6),
                t * np.sin(0) * np.sin(PI/6),
                t * np.cos(PI/6)
            ]), t_min=0, t_max=2.5, color=PINK
        )

        coordinates_s = ParametricSurface(
            lambda u, v : np.array([
                (2.5 * np.cos(t) * np.sin(PI/6)),
                (2.5 * np.sin(t) * np.sin(PI/6)),
                (2.5 * np.cos(PI/6))
            ]), t_min=0, t_max=TAU, color=RED
        )

        coordinates_r = ParametricFunction(
            lambda t : np.array([
                t * np.cos(0) * np.sin(PI/6),
                t * np.sin(0) * np.sin(PI/6),
                t * np.cos(PI/6)
            ]), t_min=0, t_max=2.5, color=PINK
        )

        coordinates_t = ParametricFunction(
            lambda t : np.array([
                t * np.cos(0) * np.sin(PI/6),
                t * np.sin(0) * np.sin(PI/6),
                t * np.cos(PI/6)
            ]), t_min=0, t_max=2.5, color=PINK
        )

        '''
        radians = PI/180

        angle = DecimalNumber(0, num_decimal_places=0)
        time = ValueTracker(0)
        angle.add_updater(lambda num:num.set_value(time.get_value()))

        self.play(ShowCreation(coordinates_r2), ShowCreation(coordinates_s1))
        self.play(
            ApplyMethod(time.increment_value, 360, rate_func=smooth, run_time=2)
        )
        '''
        #self.play(ShowCreation(coordinates_r2), ShowCreation(coordinates_s1))
        self.play(ShowCreation(coordinates_s))


        self.wait()


class AngleTest(ThreeDScene):
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
            ApplyMethod(time_1.increment_value, 360, rate_func=smooth, run_time=5-duration_s)
        )


class ThreeDTest(ThreeDScene):
    CONFIG = {
        "x_min":-5,
        "x_max": 5,
        "y_min":-5,
        "y_max": 5,
        "z_min":-5,
        "z_max": 5,
    }

    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # angle counter
        degree = TextMobject(
            "Angle:",
            tex_to_color_map={"Angle:":GREEN}
        ).scale(0.8)
        degreeNum = DecimalNumber(0, num_decimal_places=0)
        # put the angle next to degreeNum left side
        degree.next_to(degreeNum, LEFT)

        # time object used to count
        time = ValueTracker(0)
        degreeNum.add_updater(lambda num:num.set_value(time.get_value()))

        # rotate the group to the positive y-axis
        angleGroup = VGroup(degree, degreeNum)
        angleGroup.move_to(UP * 2 + OUT / 2)
        angleGroup.rotate(PI / 2, axis=RIGHT)
        angleGroup.rotate(PI / 2, axis=OUT)

        # a dot for showing angle chaning
        testDot = Dot(np.array((1, 0, 0)))
        self.add(degreeNum)
        self.play(Write(degree))
        self.play(
            Rotate(testDot, PI / 6, run_time=3, about_point=ORIGIN),
            ApplyMethod(time.increment_value, 30.0, rate_func=smooth, run_time=3)
        )


class ThreeDTest2(ThreeDScene):
    CONFIG = {
        "x_min":-5,
        "x_max": 5,
        "y_min":-5,
        "y_max": 5,
        "z_min":-5,
        "z_max": 5,
    }

    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # angle counter
        degree = TextMobject(
            "Angle:",
            tex_to_color_map={"Angle:":GREEN}
        ).scale(0.8)
        degreeNum = DecimalNumber(0, num_decimal_places=0)
        # put the angle next to degreeNum left side
        degree.next_to(degreeNum, LEFT)

        # time object used to count
        time = ValueTracker(0)
        def numUpdater(num):
            center = num.get_center()
            num.set_value(time.get_value())
            num.move_to(ORIGIN)
            num.rotate(PI / 2, axis=RIGHT)
            num.rotate(PI / 2, axis=OUT)
            num.move_to(center)

        degreeNum.add_updater(numUpdater)
        # degreeNum.add_updater(lambda num:num.set_value(time.get_value()))

        # rotate the group to the positive y-axis
        angleGroup = VGroup(degree, degreeNum)
        angleGroup.move_to(UP * 2 + OUT / 2)
        angleGroup.rotate(PI / 2, axis=RIGHT)
        angleGroup.rotate(PI / 2, axis=OUT)

        # a dot for showing angle chaning
        testDot = Dot(np.array((1, 0, 0)))
        self.add(degreeNum)
        self.play(Write(degree))
        self.play(
            Rotate(testDot, PI / 6, run_time=3, about_point=ORIGIN),
            ApplyMethod(time.increment_value, 30.0, rate_func=smooth, run_time=3)
        )


class TestParameterization(Scene):
    def construct(self):
        CONFIG = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -4,
            "y_max": 4,
            "graph_origin": ORIGIN,
            "function_color": WHITE,
            "axes_color": BLUE
        }

        simple_closed_curve = ParametricFunction(
            lambda u : np.array([
                1.0 * np.sin(u),
                1.0 * np.cos(u),
                0
            ]), t_min=0, t_max=PI, color=RED
        )

        axes = ThreeDAxes()
        self.add(axes)
        self.play(ShowCreation(simple_closed_curve))


class SphereParameterization(ThreeDScene):
    def construct(self):
        sphereplot = ParametricSurface(
            lambda u, v : np.array([
                2.0 * np.cos(u) * np.sin(v),
                2.0 * np.sin(u) * np.sin(v),
                2.0 * np.cos(v)
            ]), u_min=0, u_max=TAU, v_min=0, v_max=PI, color=RED
        )

        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=80*DEGREES,theta=15*DEGREES)
        self.begin_ambient_camera_rotation()
        self.wait()
        self.play(ShowCreation(sphereplot), run_time=3)
        self.wait(2)


class ThreeDTThenS(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=105*DEGREES,theta=-15*DEGREES, gamma=180*DEGREES)
        text3d=TextMobject("Spherical Coordinates")

        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]), u_min=-PI/2, u_max=PI/2, v_min=0, v_max=TAU, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(LaggedStart(ShowCreation(sphere)))
        self.wait(2)


class ThreeDSThenT(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES, distance=20)
        text3d=TextMobject("Spherical Coordinates")

        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Write(text3d))

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)*np.sin(v),
                1.5*np.cos(v)
            ]), u_min=0, u_max=TAU, v_min=0, v_max=PI, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(LaggedStart(ShowCreation(sphere)))
        self.wait(2)
