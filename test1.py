#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class TestScene(Scene):
    def construct(self):
        base1 = TexMobject(
            r"\oint{E \bullet dA} = \frac{Q_{enc}}{\varepsilon_{0}}"
        )
        self.play(
            Write(base1),
        )


class TwoDTThenS(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        circle_t = ParametricFunction(
            lambda u : np.array([
                0.25 * np.cos(u),
                0.25 * np.sin(u),
                2
            ]), t_min=0, t_max=TAU
        )

        circle_s = ParametricFunction(
            lambda u : np.array([
                2 * np.sin(u),
                0,
                2 * np.cos(u)
            ]), t_min=0, t_max=PI
        )

        self.play(ShowCreation(axes))
        self.wait()
        self.play(ShowCreation(circle_t), run_time=3)
        self.wait()
        self.move_camera(phi=75*DEGREES, theta=-60*DEGREES, run_time=3)
        self.wait()
        self.play(ShowCreation(circle_s), run_time=3)


class SThenT(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES)
        text3d=TextMobject("Spherical Coordinates")

        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)*np.sin(v),
                1.5*np.cos(v)
            ]), u_min=0, u_max=TAU, v_min=0, v_max=PI, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(LaggedStart(ShowCreation(sphere)), run_time=5)
        self.wait(2)


class TThenS(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=105*DEGREES,theta=-45*DEGREES, gamma=180*DEGREES)
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
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(LaggedStart(ShowCreation(sphere)), run_time=5)
        self.wait(2)


#----- Surfaces
class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),v_min=-2,v_max=2,u_min=-2,u_max=2,checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)

        cone = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        hip_one_side = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u)*np.cos(v),
                np.cosh(u)*np.sin(v),
                np.sinh(u)
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

        ellipsoid=ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)*np.sin(v),
                1.5*np.cos(v)
            ]),v_min=0,v_max=PI,u_min=0,u_max=TAU,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere,ellipsoid))
        self.wait()
        self.play(ReplacementTransform(ellipsoid,cone))
        self.wait()
        self.play(ReplacementTransform(cone,hip_one_side))
        self.wait()
        self.play(ReplacementTransform(hip_one_side,para_hyp))
        self.wait()
        self.play(ReplacementTransform(para_hyp,paraboloid))
        self.wait()
        self.play(ReplacementTransform(paraboloid,cylinder))
        self.wait()
        self.play(FadeOut(cylinder))
