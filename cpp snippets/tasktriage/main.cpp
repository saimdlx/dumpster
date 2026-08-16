#include <iostream>
#include <fstream>

using namespace std;

void displayMenu();
void showTasks();
void addTask(string);
void deleteTask(int);

int main() {

    fstream obj;
    obj.open("list.md");
    return 0;
}

void displayMenu() {

    cout << "===== TASK TRIAGE =====" << endl;
    cout << "Select one of the following options: " << endl;
    cout << "1. Add a new task." << endl;
    cout << "2. Delete a task." << endl;
    cout << "3. View all tasks." << endl; 
}