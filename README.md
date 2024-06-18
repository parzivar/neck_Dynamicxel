# Neck_Dynamicxel
Make your own robot using DNAMICXEL motors
```bash
cd ~/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_control/config
```
You need to create your own motor parameter document like **master_neck.yaml**
then revise the **modes.yaml** to define the motors operating mode

```bash
cd ~/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf
```
revise your robot URDF file like **master_neck.urdf**
You need a urdf file corresponding to your robot to initialize the ros node through the SDK

```bash
cd ~/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_ros_control/config
```
Here you need to modify three files： **xdof_controllers.yaml**、 **hardware.yaml**、 **modes.yaml**
Among **xdof_controllers.yaml**, x should correspond to the DOF of your motor

```bash
cd ~/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_ros_control/launch
```
Modify the DOF default value in **xsarm_ros_control.launch** to correspond to the x above

```bash
cd ~/interbotix_ws/src/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_modules/src
```
Add your robot in **mr_descriptions.py**
