import maya.cmds as cmds

def create_car(name, length=4, width=2):
    # Create the car components
    body = create_body(length, width)
    tires = create_tires(length, width)
    
    # Group the car components
    final_name = assemble_car(name, body, tires)
    
    # Clear any selections in the scene
    cmds.select(clear=True)
    
    return final_name
    
def create_body(length=4, width=2):
    # Create a plane that represents the car body.
    # Return the transform node name.
    body = cmds.polyPlane(w=length, h=width, name="body")
    return body[0]
    
def create_tires(body_length, body_width):
    # Create four tires for the car.
    # Size and position are relative to the body dimensions.
    tire_width = 0.25 * body_width
    tire_depth = 0.25 * body_length
    x_pos = 0.5 * body_length
    z_pos = 0.5 * body_width + 0.5 * tire_width
    
    fl_tire = create_tire("front_left_tire", tire_width, tire_depth, x_pos, 0, -z_pos)
    fr_tire = create_tire("front_right_tire", tire_width, tire_depth, x_pos, 0, z_pos)
    rl_tire = create_tire("rear_left_tire", tire_width, tire_depth, -x_pos, 0, -z_pos)
    rr_tire = create_tire("rear_right_tire", tire_width, tire_depth, -x_pos, 0, z_pos)
    
    return [fl_tire, fr_tire, rl_tire, rr_tire]
    
def create_tire(name, width, depth, tx, ty, tz):
    # Create a cylinder that represents a tire.
    # Return the transform node name.
    tire = cmds.polyCube(h=width, d=depth, ax=(0,0,1), name=name)
    cmds.setAttr("{0}.translate".format(tire[0]), tx, ty, tz)
    return tire[0]
    
def assemble_car(name, body, tires):
    # Create groups for the body and tires and parent them
    # under the main car group.
    # Return the car group name.
    body_grp = cmds.group(body, name="body_grp")
    tires_grp = cmds.group(tires, name="tires_grp")
    
    car_grp = cmds.group(body_grp, tires_grp, name=name)
    return car_grp
    
if __name__ == "__main__":
    name = create_car("test_car")
    print("Car created: {0}".format(name))