#include <queue>
#include <unordered_set>
#include <vector>
using namespace std;

class RideSharingSystem {
private:
    queue<int> riders;
    queue<int> drivers;
    unordered_set<int> activeRiders;

public:
    RideSharingSystem() {}

    void addRider(int riderId) {
        riders.push(riderId);
        activeRiders.insert(riderId);
    }

    void addDriver(int driverId) {
        drivers.push(driverId);
    }

    vector<int> matchDriverWithRider() {
        // Remove cancelled riders from front
        while (!riders.empty() && activeRiders.count(riders.front()) == 0) {
            riders.pop();
        }

        if (riders.empty() || drivers.empty()) {
            return {-1, -1};
        }

        int riderId = riders.front();
        int driverId = drivers.front();

        riders.pop();
        drivers.pop();
        activeRiders.erase(riderId);

        return {driverId, riderId};
    }

    void cancelRider(int riderId) {
        activeRiders.erase(riderId); // lazy removal
    }
};
