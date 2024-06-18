
"use strict";

let Reboot = require('./Reboot.js')
let RobotInfo = require('./RobotInfo.js')
let TorqueEnable = require('./TorqueEnable.js')
let OperatingModes = require('./OperatingModes.js')
let MotorGains = require('./MotorGains.js')
let RegisterValues = require('./RegisterValues.js')

module.exports = {
  Reboot: Reboot,
  RobotInfo: RobotInfo,
  TorqueEnable: TorqueEnable,
  OperatingModes: OperatingModes,
  MotorGains: MotorGains,
  RegisterValues: RegisterValues,
};
