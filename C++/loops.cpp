#include <iostream>
using namespace std;

int main() {
    int n;
    double factorial = 1.0;

    cout << "Enter n for n factorial: ";
    cin >> n;

    // this is so similar to java, heck, I could confuse it with java
    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }
    cout << n << "! is " << factorial; // << instead of +

    return 0;
}