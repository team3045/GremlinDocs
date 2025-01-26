Programming in FRC
===================

Programming is a vital part of building a successful FRC (FIRST Robotics Competition) robot. 
It enables your team to bring your hardware to life, implementing autonomous behaviors, 
teleoperated controls, and complex strategies. 
This guide introduces the basics of programming for FRC robots and how to get started.

What is FRC Programming?
-------------------------
FRC programming involves not just writing the code that controls your robot throughout each match, but a variety of other 
big and small, and often times annoying tasks. In general, as part of the Software team your responsibilites will include

1. **Programming the Robot**: The most obvious of our responisibilites is writing the code that controls the robot throughout our matches.
    We'll talk a lot about this later, but this requires a good understanding of motors and actuators, sensors, and control theory.
2. **Maintaining Firmware**: Another responability of the Software team is keeping all necessary firmware 
    (Software internal to a device, provided by the vendor) of devices up to date. It's important to stay on top of updating devices
    because new firmware releases often include critical fixes or breaking changes, which are always better to learn about sooner rather than later.
    Imagine how bad it would be if you updated a motor in the middle of a competition, and the robot no longer drove. 
3. **Auxiliary Software**: Apart from code that runs on the robot, we also create and maintain other tools that are generally useful to the team.
    For example, this docs site is one such project. Other exmaples include an app for the CNC machine, a scouting app, a driver dashboard
    and much more. 
4. **Electrical**: While technically two different departments, it is incredibly helpful to have electrical knowledge when working on software. 
    As many issues could be attributed to either wiring or code, having knowledge and experience with both is immeasurably helpful.  

Programming Languages
----------------------
There are countless different programming languages in the world, with heated debates over which ones are better, faster, prettier etc. 
While the syntax (the grammer of each language) is different, general programming concepts are applicable across any and every language.
In FRC we generally use the following few languages. 

- **Java**: The most commonly used language in FRC due to its extensive support and documentation.
- **C++**: More prevalently used outside of FRC for robotics as it offers fine-grained control but requires more experience.
- **Python**: A easy to learn, yet still very powerful language. Python is often used for machine learning or computer vision. 
- **Dart**: Dart is a programming language to create cross-platform apps. We use it for some of the Auxiliary software mentioned earlier. 

Getting Started
---------------
To begin programming your FRC robot, follow these steps:

1. **Set Up WPILib**:
   WPILib is the official library for programming FRC robots. Install WPILib from the [FRC Documentation](https://docs.wpilib.org/), which includes tools and libraries for robot programming.

2. **Choose an IDE**:
   - **Visual Studio Code**: Recommended by FRC, with pre-configured extensions for WPILib.

3. **Create a New Robot Project**:
   Use WPILib’s project generator to create a new robot project. You can choose from templates like "TimedRobot" or "Command-Based".

4. **Understand the Project Structure**:
   - **src/main/java**: Contains your robot’s code.
   - **Robot.java**: The entry point of your robot’s code.

Basic Programming Concepts
---------------------------
Here are some key concepts to understand:

- **Motors and Actuators**:
  Use motor controllers (e.g., Talon FX, Spark MAX) to drive motors. WPILib provides classes to interface with these controllers.

- **Sensors**:
  Incorporate sensors like encoders, gyros, and cameras to provide feedback and improve control.

- **Command-Based Programming**:
  Organize your code into commands and subsystems for modularity and reusability.

- **Field-Oriented Drive**:
  For advanced teams using swerve or mecanum drives, implement field-oriented control for improved driver experience.

Learning Resources
-------------------
Here are some resources to help you learn:

- **FRC Documentation**: [https://docs.wpilib.org/](https://docs.wpilib.org/)
- **Chief Delphi Forums**: Community discussions and troubleshooting.
- **WPILib Examples**: Pre-built example projects to learn specific features.

Tips for Success
-----------------
- **Start Early**: Begin learning and coding as soon as the game is released.
- **Version Control**: Use Git to manage your code and collaborate with your team.
- **Test Often**: Test your code on the robot regularly to catch issues early.
- **Ask for Help**: Don’t hesitate to reach out to mentors, forums, or other teams for guidance.

Programming in FRC is a rewarding challenge that combines creativity, logic, and teamwork. With practice and dedication, you can create code that takes your team’s robot to the next level!

