#include <iostream>
#include <string>
using namespace std;

class Spring{
	public:
		Spring();					  // default constructor
		Spring(string n, double st, double c); // constructor
		
		void set_spring_constant(double st);
		void set_compression(double c);
		void set_name(string n);
		
		double get_spring_contant();
		double get_compression();
		string get_name();
		
	private:
		double spring_constant, compression;
		string name;

};

Spring::Spring(){
	spring_constant = 0;
	compression = 0;
}

Spring::Spring(string n, double st,double c){
	spring_constant = st;
	compression = c;
	name = n;
}

void Spring::set_spring_constant(double st){
	spring_constant = st;
}

void Spring::set_compression(double c){
	compression = c;
}

double Spring::get_spring_contant(){
	return spring_constant;
}

double Spring::get_compression(){
	return spring_constant;
}

string Spring::get_name(){
	return name;
}


