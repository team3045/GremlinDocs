Vision in FRC
=============

What is Computer Vision?
-------------------------
Computer Vision is a technology that helps computers "see" and understand pictures and videos, just like how people use their eyes and brain to understand the world. 
It uses tools like math and computer programs to figure out what’s in an image, like recognizing faces, objects, or movement. 
Computer vision is used in many cool ways, like unlocking your phone with your face, helping cars drive themselves, spotting problems in factories, 
and even helping doctors find diseases in medical images. It’s all about teaching computers to make sense of what they see!

A Good Video introducing Computer Vision: `Computer Vision Crash Course <Computer Vision: Crash Course Computer Science #35>`_.

Why Use Vision in FRC?
----------------------
In **FIRST Robotics Competition (FRC)**, vision processing plays a critical role in helping robots interact with their environment by analyzing images and identifying 
important targets, objects, or game pieces. Vision systems can enhance robot accuracy, speed, and autonomy.

Vision systems are used to:

- Identify field elements like scoring targets, reflective tape, or game pieces.
- Align the robot accurately for tasks such as shooting or placing objects.
- Track and follow moving objects.
- Localize the position of the robot. Essentially using what the robot sees to make a guess at where it is on the field.

Most systems follow some general steps:

1. **Image Capture**: The camera captures an image of the field or target.
2. **Preprocessing**: The image is filtered, resized, or adjusted (e.g., color thresholding) to focus on the target.
3. **Target Detection**: The vision pipeline identifies key features such as contours, shapes, or colors.
4. **Processing**: Depending on the goal, the computer uses target detections to compute useful information, such as the distance to a target, the location of the robot, or the state of a game piece etc.
5. **Feedback**: The vision system sends information to the robot's code (e.g., angles or distances) to make decisions and execute tasks.

Due to the high overhead of processing images, most FRC teams choose to run any vision algorithms on a co-processor \
like a Raspberry Pi, Jetson Nano, or a Orange Pi 5, and only send the relevant information to the Roborio over 
`Network Tables <https://docs.wpilib.org/en/stable/docs/software/networktables/networktables-intro.html>`_.

Similarly due to the increasing complexity and necessity of fast, robust, and accurate vision, many FRC teams opt to use COTS solutions
such as `Photon Visiomn <https://photonvision.org/>`_, or `Limelight <https://limelightvision.io/>`_.

Apriltags
---------

AprilTags are a type of fiducial marker similar to QR codes but specifically designed for robust detection and 
pose estimation in robotics. They consist of black-and-white square patterns that encode unique IDs, allowing robots to identify the tag and 
calculate its position and orientation relative to the robot. In FRC, AprilTags are often used to assist with precise navigation and alignment during autonomous routines. By placing AprilTags on the field, robots can use cameras and vision processing software to quickly determine their location, align with targets, or interact with game pieces more effectively, improving accuracy and

For more Information on Apriltags visit the `WPIlib Docs <https://docs.wpilib.org/en/stable/docs/software/vision-processing/apriltag/apriltag-intro.html>`_.

Camera Calibration
------------------
Camera calibration is the process of determining a camera’s intrinsic properties (like focal length and optical center) and distortion parameters. This allows the camera to accurately interpret real-world measurements from images. Calibration is crucial in applications like robotics, where precise measurements are needed to calculate distances, angles, and positions. Without proper calibration, even small distortions caused by the lens or perspective can lead to significant errors. In systems like FRC vision processing, calibration ensures the robot can correctly estimate the location and orientation of field elements, making tasks like alignment, targeting, and navigation reliable and accurate.

For more Information on Camera Calibration visit the `Limelight Docs <https://docs.limelightvision.io/docs/docs-limelight/getting-started/performing-charuco-camera-calibration>`_.

Stereo Vision
-------------

Stereo vision is a technique that uses two cameras to create a 3D representation of the environment. 
By capturing images from two slightly different viewpoints, stereo vision systems can calculate the depth and distance of objects in the scene. 
This depth information is valuable in robotics for tasks like obstacle avoidance, object tracking, and localization. In FRC, stereo vision can help robots navigate complex environments, 
interact with game elements, and make precise movements with depth perception.

`A Simple explanation of Stereo Vision <https://www.youtube.com/watch?v=yfjMJfXMBcY>`_.

`A detailed explanation of the Math <https://www.youtube.com/watch?v=hUVyDabn1Mg>`_.

We have in the past used the Luxonis OAK D camera for stereo vision, and it has worked well for us.

Read the OAK-D page for docs on how to use our current system. 

Pose Estimation
--------------

Pose estimation is the process of determining an object's position (x, y, z) and orientation (roll, pitch, yaw) in space. In robotics, this is essential for understanding the robot’s location and movement relative to its environment. To improve accuracy, different position measurements from sensors like encoders, gyroscopes, cameras, and LIDAR can be fused using techniques such as Kalman filters, which combine sensor data while accounting for uncertainties, or sensor fusion algorithms like complementary filters. By blending data from multiple sources, robots can reduce noise and handle sensor inaccuracies, resulting in more reliable and precise pose estimation, critical for tasks like autonomous navigation and alignment.

Kalman filters are mathematical algorithms used to estimate the state of a system, such as a robot’s position or velocity, by combining noisy measurements from multiple sensors. They work by predicting the system’s next state based on a model (e.g., motion equations) and then correcting that prediction using actual sensor data. The Kalman filter accounts for uncertainties in both the model and the measurements, finding the best estimate of the system’s state over time. In robotics, Kalman filters are widely used for tasks like pose estimation, navigation, and object tracking, as they enable robots to make accurate decisions even with imperfect sensor data.

To learn more about Kalman Filters check out `this book <https://www.kalmanfilter.net/default.aspx>`_ and `this github repository <https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python>`_.

For an example on how to use a kalman filter to fuse vision and odomtery measurements to estimate our pose, check out our 2025 codebase.

Resources
---------
- [PhotonVision Documentation](https://docs.photonvision.org/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Limelight Documentation](https://docs.limelightvision.io/)

