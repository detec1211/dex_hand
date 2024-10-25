from proto_util import ctrl_command_pb2 as command
import time


def set_test_impedance_control():
    new_impedance_control = command.ImpedanceControl()
    new_impedance_control.Thumb.Stiffness = 0.5  # 0-1,stand for hardness of the force,0 stand for no force
    new_impedance_control.Thumb.SetPoint = 0.3  # 0-1,stand for position of the force,sign stand for direction,positive number for inward,minus number for outward
    new_impedance_control.Index.Stiffness = 0.9
    new_impedance_control.Index.SetPoint = 0.2
    new_impedance_control.Middle.Stiffness = 0.5
    new_impedance_control.Middle.SetPoint = -0.8
    new_impedance_control.Ring.Stiffness = 0.5
    new_impedance_control.Ring.SetPoint = 0.5
    new_impedance_control.Pinky.Stiffness = 0.5
    new_impedance_control.Pinky.SetPoint = 0.5
    new_impedance_control.has_index = True  # true stand for the command cannot be ignore,false stand for the command can be ignore
    return new_impedance_control


def test_worker(command_write_worker):
    while True:
        new_impedance_control = set_test_impedance_control()
        command_write_worker.add_new_impedance_control(1344418560,
                                                       new_impedance_control)  # the id need to be the id of your hands
        time.sleep(2)
