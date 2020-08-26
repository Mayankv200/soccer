from controller import Supervisor

 

TIME_STEP = 32

 

supervisor = Supervisor()


# do this once only
robot_node = supervisor.getFromDef("ball")
trans_field = robot_node.getField("translation")

 

while supervisor.step(TIME_STEP) != -1:
    values = trans_field.getSFVec3f()
    print("BALL is at position: %g %g %g" % (values[0], values[1], values[2]))
    if ((values[0]>4.5 and values[2]>-0.75 and values[2]<0.75) or (values[0]<-4.5 and values[2]>-0.75 and values[2]<0.7)):
        INITIAL = [0, 0.112, 0]
        trans_field.setSFVec3f(INITIAL)
        robot_node.resetPhysics()
    elif( values[0]>4.5):
        trans_field.setSFVec3f([4.5, 0.112, values[2]])
        robot_node.resetPhysics()
    elif( values[0]<-4.5):
        trans_field.setSFVec3f([-4.5, 0.112, values[2]])
        robot_node.resetPhysics()
    elif( values[2]>3):
        trans_field.setSFVec3f([values[0], 0.112, 3])
        robot_node.resetPhysics()
    elif( values[2]<-3):
        trans_field.setSFVec3f([values[0], 0.112, -3])
        robot_node.resetPhysics()


