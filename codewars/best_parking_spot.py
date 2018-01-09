"""
Todd is looking for the best place to park in the grocery store parking lot. Todd knows that there's a sequence of
events that happens whenever he buys groceries:

When he first arrives, he walks straight into the store (where the carts are kept).
After completing shopping, he will return to his car with his cart to put the groceries away.
He will walk with the now empty cart to the nearest cart corral, and deposit it.
He will walk back to his car.
This particular parking lot is fairly simple. The store is located on the far left, there is a single row of parking,
with some number of cart corrals interspersed within them. For example:

["STORE", "TAKEN", "TAKEN", "CORRAL", "TAKEN", "OPEN", "OPEN", "TAKEN", "CORRAL"]
Each index is one "space" of walking.

In this case, the best spot for Todd would be at index 5. He would take 5 steps to get to the store, then 5 steps to get
back to his car, then 2 steps to get to a cart corral, then 2 steps to get back, for a total of 14 steps.

Return the index of the parking spot Todd should choose. Since Todd is driving in from the side without the store on it,
if there's a tie in distance, pick the one that's the furthest from the store. (Less driving. Todd is incredibly lazy.)
"""


def best_parking_spot(arr):
    OPEN = 'OPEN'
    CORRAL = 'CORRAL'

    parking = {}
    corrals = []

    for i, x in enumerate(arr):
        if x == OPEN:
            parking[i] = i*2
        if x == CORRAL:
            corrals.append(i)

    def get_closest_corral(spot):
        dist = len(arr) + 1
        for x in corrals:
            d = abs(spot - x)
            dist = min(dist, d)
        return dist

    for spot in parking:
        dist = get_closest_corral(spot)
        parking[spot] += dist*2

    spots = list(parking.keys())
    spots.sort()
    spots = spots[::-1]
    best = spots[0]

    for x in spots:
        if parking[x] < parking[best]:
            best = x

    return best

best_parking_spot(["STORE", "TAKEN", "TAKEN", "CORRAL", "TAKEN", "OPEN", "OPEN", "TAKEN", "CORRAL"])
