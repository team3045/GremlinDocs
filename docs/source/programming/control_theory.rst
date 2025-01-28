Introduction to Control Theory in FRC
====================================

Control theory is a cornerstone of robotics, providing the mathematical and systematic tools needed to manage the behavior of dynamic systems. In the context of FRC (FIRST Robotics Competition), control theory is essential for tasks such as driving mechanisms, controlling arm movements, maintaining stable robot orientations, and tracking trajectories. Effective use of control theory enables robots to operate more accurately, efficiently, and predictably.

What is Control Theory?
-----------------------

At its core, control theory is the study of how to influence the behavior of a system to achieve a desired outcome. This involves designing controllers that adjust inputs to the system based on feedback from sensors, enabling the system to meet specified goals even in the presence of disturbances or uncertainties.

In FRC, control theory commonly applies to:

- **Drivetrain control** (swerve, tank, or mecanum drives).
- **Manipulator systems** (arms, elevators, and claws).
- **Shooter mechanisms** (flywheels for consistent velocities).
- **Autonomous path following** (trajectory generation and tracking).

Key Components of a Control System
-----------------------------------

1. **System/Plant**: The physical mechanism you want to control (e.g., a motor driving a wheel).
2. **Sensor**: Provides feedback about the system’s state (e.g., encoders, gyroscopes, or vision systems).
3. **Controller**: Computes the adjustments needed to meet the desired state. In FRC, this is often a combination of feedforward and feedback control.
4. **Actuator**: The device that applies the controller’s output to the system (e.g., motor controllers like TalonFX or Spark MAX).

Feedforward and Feedback Control
---------------------------------

Effective control often combines both **feedforward** and **feedback** control methods.

Feedforward Control
~~~~~~~~~~~~~~~~~~~

Feedforward control predicts the input needed to achieve the desired system behavior without relying on feedback. This requires a mathematical model of the system and is typically used for tasks where precise, predictable motion is needed.

For example, in FRC, feedforward can calculate the voltage needed to:

- Overcome static friction.
- Achieve a specific velocity.
- Maintain a constant acceleration.

The basic feedforward model is:

.. math::

   u = k_s + k_v \times v + k_a \times a

Where:

- \( u \): feedforward voltage.
- \( k_s \): static gain constant (accounts for static friction).
- \( k_v \): velocity gain constant (converts velocity to voltage).
- \( k_a \): acceleration gain constant (converts acceleration to voltage).
- \( v \): desired velocity.
- \( a \): desired acceleration.

To tune feedforward constants, FRC teams typically use tools like WPILib’s **System Identification Tool**, which helps derive accurate \( k_s \), \( k_v \), and \( k_a \) values through experimental data.

Feedback Control
~~~~~~~~~~~~~~~~

Feedback control corrects errors by adjusting the system’s inputs based on the difference between the desired and actual system states. The most common type of feedback controller in FRC is the **PID controller**.

A PID controller consists of three components:

1. **Proportional (P)**: Corrects based on the current error.

   .. math::

      u_p = k_p \times e

2. **Integral (I)**: Corrects based on the accumulation of past errors.

   .. math::

      u_i = k_i \times \int e

3. **Derivative (D)**: Corrects based on the rate of change of error.

   .. math::

      u_d = k_d \times \frac{de}{dt}

The total control output is:

.. math::

   u = u_p + u_i + u_d

Where:

- \( e \): error (difference between desired and measured state).
- \( k_p, k_i, k_d \): tunable PID constants.

Combining Feedforward and Feedback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In practice, feedforward provides a baseline input to achieve desired behavior, while feedback compensates for disturbances and inaccuracies. The combined control signal is:

.. math::

   u_{total} = u_{feedforward} + u_{feedback}

Tuning Feedforward and Feedback Constants
-----------------------------------------

Feedforward Tuning
~~~~~~~~~~~~~~~~~~

1. **Static Gain (\( k_s \))**: Apply a low voltage to overcome static friction and just barely move the system. This value becomes \( k_s \).
2. **Velocity Gain (\( k_v \))**: Command different velocities and measure the steady-state voltage required to maintain each. Use the slope of the voltage vs. velocity graph to calculate \( k_v \).
3. **Acceleration Gain (\( k_a \))**: Measure the voltage required to accelerate the system at different rates. Use these values to derive \( k_a \).
4. **Gravity Gain (\( k_g \))**: If the system is affected by gravity, add a gravity term to the feedforward model: 
   For an elevator this would be a constant value (\( k_g \)) added to the output, but for a single jointed arm, this would be a function of the angle of the arm.
   g = (\(k_g \times cos(\theta)\)) where \(\theta\) is the angle of the arm. In this case, \(\theta\) should be zero when the arm is horizontal. As an excercise, think about why this is, and how one might go about tuning the gravity gain for a simple arm (Hint: You determine the gravity gain and the static gain at the same time).

   .. math::

      u = k_s + k_v \times v + k_a \times a + k_g \times A

.. note::

   There is no perfect way, nor solution, to tuning a control loop. A control loop only ever needs to be as good as you specific task requires. 
   For example, while not optimal, an often effective enough strategy to tune a simple single jointed arm is to calculate k_g and k_s by hand, and then use theoretical k_v and k_a values through a tool such as recalc. 

WPILib’s tools like Sysid simplify these steps by automating data collection and fitting the model.

PID Feedback Tuning
~~~~~~~~~~~~~~~~~~~

Tuning PID controllers typically involves the following steps:

1. **Proportional Gain (\( k_p \))**:
   - Start with \( k_p \) at a low value and increase it until the system responds quickly without significant oscillations.
2. **Integral Gain (\( k_i \))**:
   - Add \( k_i \) to eliminate steady-state error. Start small and increase carefully to avoid oscillations.
3. **Derivative Gain (\( k_d \))**:
   - Add \( k_d \) to dampen oscillations. Too much \( k_d \) can cause the system to respond sluggishly.

Further Reading
~~~~~~~~~~~~~~~~

Controls Theory is a very large and complex field. This document only scratches the surface of what is possible, here are some additional resources if you wish to learn more.

- `Controls Engineering in FRC <https://file.tavsys.net/control/controls-engineering-in-frc.pdf>`_
- `WPILib Controls Theory <https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/index.html>`_
- `Everything You Need to Know about Controls Theory <https://www.youtube.com/watch?v=lBC1nEq0_nk>`_
- `Brian Douglas Classical Control Theory <https://www.youtube.com/playlist?list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk>`_

Enjoy!

