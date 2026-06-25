#include <iostream>
using namespace std;

//i saw some shit like this in a jetbrains video and felt like implementing it myself. turn your brain off and code kinda question.

int main(){

    //exhaust user inputs until zero is pressed, return primary numerical counts
    int pos = 0;
    int neg = 0;
    int input = 0;

    cin >> input;
    while (input){
        if (input > 0){
            pos++;
        }
        if (input < 0){
            neg++;
        }
        cin >> input;
    }
    if (pos > neg){
        cout << "More positives" << endl;
    }
    else if (neg > pos){
        cout << "More negatives" << endl;
    }
    else {
        cout << "They're equal" << endl;
    }
    
    return 0;

}