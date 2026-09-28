#take n as an input with n = minutes.
#you have a robot in a triangle; FIndout where your robots wil be after n minutes. The robot moves in a triangle with vertices A, B, C. The robot starts at vertex A and moves to vertex B in the first minute, then to vertex C in the third minute, then back to vertex A in the sixth minute, and so on. Find if it is at vertex A, B, or C or in-between after n minutes. In-between means that the robot is moving from one vertex to another and has not reached the next vertex yet.
def robot_position(n):
    # The robot moves in a cycle of 3 minutes: A -> B -> C -> A
    # We can use modulo operation to determine the position of the robot after n minutes.
    
    # Calculate the position in the cycle
    position_in_cycle = n % 3
    
    if position_in_cycle == 0:
        return "A"  # Robot is at vertex A
    elif position_in_cycle == 1:
        return "B"  # Robot is at vertex B
    else:
        return "C"  # Robot is at vertex C 
    #Now we will check if the robot is in-between the vertices. The robot is in-between if it is moving from one vertex to another and has not reached the next vertex yet. This happens when n is not a multiple of 3. 
    return "in-between"

n = int(input("Enter the number of minutes: "))
position = robot_position(n)
print(f"The robot is at vertex: {position}")

def robot_position(n):
    r = n % 6

    if r == 0:
        return "A"
    elif r == 1:
        return "B"
    elif r == 3:
        return "C"
    elif r == 2:
        return "in-between (B -> C)"
    else:  # r == 4 or r == 5
        return "in-between (C -> A)"


n = int(input("Enter the number of minutes: "))
print(robot_position(n))