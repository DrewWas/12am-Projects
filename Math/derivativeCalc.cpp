#include <iostream>
using namespace std;

int main(){
	string func;
	system("clear");
	cout << "Input the function you would like to differentiate\n"; 
	cout << "Use () to seperate multiplication and ^ for exponents\n\n";
	cout << "-  ";
	cin >> func;
	cout << "\n\nThe differentiated function is - " + func + "\n\n";
	return 0;

}

// Parse the function
//
// See which rule is needed where 
//
// call rules accordingly
//
// This is super high level... Ill probably realize how hard this is once I actually get started
