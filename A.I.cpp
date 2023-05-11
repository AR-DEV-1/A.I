#include <iostream>
#include <string>

using namespace std;

int main() {
    string input;
    cout << "Hello, I am an artificial intelligence. How can I help you today?" << endl;
    getline(cin, input);
    if (input == "What is your name?") {
        cout << "My name is AI." << endl;
    }
    else if (input == "What is the weather like today?") {
        cout << "I'm sorry, I am not currently able to check the weather." << endl;
    }
    else {
        cout << "I'm sorry, I don't understand what you're asking. Please try again." << endl;
    }
    return 0;
}
