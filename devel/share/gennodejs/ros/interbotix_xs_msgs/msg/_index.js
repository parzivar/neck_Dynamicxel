
"use strict";

let HexJoy = require('./HexJoy.js');
let JointTemps = require('./JointTemps.js');
let JointGroupCommand = require('./JointGroupCommand.js');
let JointTrajectoryCommand = require('./JointTrajectoryCommand.js');
let LocobotJoy = require('./LocobotJoy.js');
let JointSingleCommand = require('./JointSingleCommand.js');
let ArmJoy = require('./ArmJoy.js');
let TurretJoy = require('./TurretJoy.js');

module.exports = {
  HexJoy: HexJoy,
  JointTemps: JointTemps,
  JointGroupCommand: JointGroupCommand,
  JointTrajectoryCommand: JointTrajectoryCommand,
  LocobotJoy: LocobotJoy,
  JointSingleCommand: JointSingleCommand,
  ArmJoy: ArmJoy,
  TurretJoy: TurretJoy,
};
