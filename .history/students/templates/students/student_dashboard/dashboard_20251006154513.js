#include <iostream>
using namespace std;

int n, a[100];

void in(int k) {
    for (int i = 1; i <= k; i++)
        cout << a[i] << " ";
    cout << endl;
}

void Try(int i, int sum, int max_val) {
    for (int j = 1; j <= max_val; j++) {
        if (sum + j < n) {
            a[i] = j;
            Try(i + 1, sum + j, j); // Giới hạn số tiếp theo ≤ j
        }
        else if (sum + j == n) {
            a[i] = j;
            in(i); // In đúng số lượng phần tử
        }
    }
}

int main() {
    cout << "Nhap n: ";
    cin >> n;
    cout << "Cac cach phan chia n la:\n";
    Try(1, 0, n);
    return 0;
}
z