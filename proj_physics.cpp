#include <iostream>
#include <cmath>
#include "spring_class.h"
using namespace std;


int main(){
cout << "Main function call" << endl;
//Springs (test values from Desmos for now)
Spring s("spring 1", 30, 0.083333);
cout << s.get_name() << " " << s.get_spring_constant() << " " << s.get_compression() << endl;
//Constants
double m_b =0.0059375; //mass of ball
double m_s = 0.01; //mass of launcher follower thing
double g = 32.174; //gravitational constant
double k = s.get_spring_constant();
double d = s.get_compression();
double L_tube = 0.5; //Length of Launch tube (ft) (UPDATE BASED ON CAD MODEL)
double h_launch = 0; //Height at launch position (UPDATE BASED ON CAD MODLE)
double x_f = 25; //Desired launcher distance (UPDATE BASED ON USER INPUT)
//Variables (iterate for angles 0 -> 45 degrees, accepting only if the y_1 and y_2 values have a very small difference (i.e. 0.01)
double lowest_diff = 100; //Dummy variable, actual values will be very small, positive non zero differences between y_1 and y_2 equations
double optimal_angle = 45;
double y_delta, V_act, v_i, y_i, x_1, x_2, y_1, y_2, current_diff;
for(double y = 0;  y < 45; y += .1){
    for(double x = 0; x < 5; x += .1){
        y_delta = sin(y) * d;
        V_act = sqrt(((k * pow(d, 2))/(m_b + m_s)) - (2 * g * y_delta));
        v_i = V_act;
        y_i = L_tube * sin(y) + h_launch;
        //PROBLEM: can't really find intersection of these functions
        //y_1 = acos((x_f)/(v_i * x));
        //y_2 = asin(((4.9 * pow(x, 2)) - y_i)/(v_i * x));
        current_diff = abs(y_1 - y_2);
        if(current_diff < lowest_diff){
            lowest_diff = current_diff;
            optimal_angle = y;
        }
    }
}
cout << "Optimal Angle for launch: " << optimal_angle << endl;

}


/*
//For all of these, update based on class file for data type (short, long, float etc.)
0 = (cos(y) * v_i * x) - x_f
0 = -4.9 * (pow(x, 2)) + (sin(y) * v_i * x) + y_i
y_i = L_tube * sin(y) + h_launch
y_delta = sin(y) * d
V_act = sqrt(((k * pow(d, 2))/(m_b + m_s)) - (2 * g * y_delta))
v_i = V_act
//Constants
m_b = m_{b}=0.0059375 //mass of ball
m_s = 0.01 //mass of launcher follower thing
g = 32,174 //gravitational constant
k = 50 * 12 //spring constant (UPDATE FOR SPRING CLASS)
d = (1/12) //compression of spring (UPDATE FOR SPRING CLASS)
L_tube = 0.5 //Length of Launch tube (ft)
h_launch = 0 //Height at launch position


//translated functions, maybe iterate with a 0.01 step for x?
y = acos((x_f)/(v_i * x))
y = asin(((4.9 * pow(x, 2)) - y_i)/(v_i * x))

*/
