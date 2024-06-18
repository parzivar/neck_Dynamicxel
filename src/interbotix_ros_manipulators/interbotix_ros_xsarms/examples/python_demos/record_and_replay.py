from interbotix_xs_modules.arm import InterbotixManipulatorXS
from time import sleep
import numpy as np
import csv

def test_real_teleop():
    # record
    # Record = True
    # Replay = False

    # replay
    Record = False
    Replay = True


    master_bot_neck = InterbotixManipulatorXS("puppet_neck", "arm")

    def torque_off(bot):
        bot.dxl.robot_torque_enable("group", "arm", False)

    def torque_on(bot):
        bot.dxl.robot_torque_enable("group", "arm", True)
    def get_action(master_bot_neck):
        action = np.zeros(3)  # 3 joint, for single arm
        action[:3] = master_bot_neck.dxl.joint_states.position[:3]
        return action
    def step(master_bot_neck, action):
        master_bot_neck.arm.set_joint_positions(action[:3], blocking=False)
        sleep(0.02)

    actions =[]
    torque_off(master_bot_neck)
    while Record:
        print("begin recording")
        for t in range(1000):
            action = get_action(master_bot_neck)
            actions.append(action)
            sleep(0.02)  # 控制记录频率

        # 保存记录的数据到epsoid.csv文件
        with open('episode.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(actions)
        Record = False
        print("finish record")
        sleep(2)

    if Replay:
        # 读取记录的数据
        with open('episode.csv', 'r') as file:
            reader = csv.reader(file)
            actions = [list(map(float, row)) for row in reader]
        print("open file success")
        torque_on(master_bot_neck)
        print("begin replaying")
        for action in actions:
            step(master_bot_neck, action)
        print("finish replaying")

if __name__ == '__main__':
    test_real_teleop()