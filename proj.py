import math
import matplotlib.pyplot as plt

#Main Function call
if __name__ == "__main__":
    #Constants (may need to pull from user input)
    m_b = 0.0059375 #mass of ball
    m_s = 0.01 #mass of launcher follower thing
    g = 32.174 #gravitational constant
    k = 600 #update with new .h file
    d = 0.0833 #update with .h file
    L_tube = 0.5 #Length of Launch tube (ft) (UPDATE BASED ON CAD MODEL)
    h_launch = 0 #Height at launch position (UPDATE BASED ON CAD MODLE)
    x_f = 25 #Desired launcher distance (UPDATE BASED ON USER INPUT)
    #Variables (iterate for angles 0 -> 45 degrees, accepting only if the y_1 and y_2 values have a very small difference (i.e. 0.01)
    lowest_diff = 100 #Dummy variable, actual values will be very small, positive non zero differences between y_1 and y_2 equations
    optimal_angle = 45
    y= 0
    #While loop to iterate through angles 0-pi/4 and find optimal launch angle
    while y < (math.pi/4):
        y_delta = math.sin(y) * d
        V_act = math.sqrt(((k * (d**2))/(m_b + m_s)) - (2 * g * y_delta))
        v_i = V_act
        y_i = L_tube * math.sin(y) + h_launch
        #First function easy, isolate x
        x_1 = x_f / (math.cos(y) * v_i)
        #Second function more difficult, need to take quadratic equation and get roots (a,b,and c)? (take only the negative answer?)
        a = -4.9
        b = math.sin(y) * v_i
        c = y_i
        x_2p = (-b + math.sqrt((b**2) - (4 * a * c)))/(2 * a)
        x_2m = (-b - math.sqrt((b**2) - (4 * a * c)))/(2 * a)
        current_diff = abs(x_1 - x_2m)
        if(current_diff < lowest_diff):
            lowest_diff = current_diff
            optimal_angle = y
            optimal_speed = v_i
        y += 0.05 #can change step for more accurate results if needed
    launch_angle = optimal_angle * (180/math.pi)
    print("Ideal launch angle:")
    print(launch_angle)
    print("Projectile Speed:")
    print(optimal_speed)
    #Generate plot values
    x_values = []
    y_values = []
    time = 0
    while (1):
        height = (-4.9 * (time ** 2)) + (math.sin(optimal_angle) * optimal_speed * time)
        distance = math.cos(optimal_angle) * optimal_speed * time
        time += .05 #increase step by 1 foot
        if height < 0:
            break
        x_values.append(distance)
        y_values.append(height)
    #Plot the trajectory in a graph
    plt.plot(x_values, y_values)
    # naming the x axis
    plt.xlabel("Horizontal Distance (ft)")
    # naming the y axis
    plt.ylabel("Vertical Height (ft)")
    # giving a title
    plt.title("Projectile Motion Trajectory Graph!")
    # function to show the plot
    plt.show()


