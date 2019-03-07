

import bin.icomRigSerialComms as rigComms
import bin.rigobj as rigobj
import bin.menu as menu

myRig = rigobj.MyRig()

rigComms.start(myRig)

