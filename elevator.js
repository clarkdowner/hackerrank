
function solution(A, B, M, X, Y) {
  var personWeight = A;
  var targetFloor = B;
  // M = number of floors
  var maxPersons = X;
  var maxWeight = Y;

  var totalPeople = personWeight.length;
  var personIndex = 0;
  var numStops = 0;

  var elevator = {};
  elevator.weight = 0;
  elevator.numPeople = 0;
  elevator.floors = [];

  function canAdd(index) {
    if (index >= totalPeople) { 
      return false; 
    }

    if (elevator.weight + personWeight[index] <= maxWeight && elevator.numPeople + 1 <= maxPersons) {
      return true;
    }
    return false;
  }

  function addPerson(index) {
    elevator.weight = elevator.weight + personWeight[index];
    elevator.numPeople += 1;

    findAndAddFloor(targetFloor[index]);

    personIndex++;
  }

  function findAndAddFloor(floorNum, temp) {

    function findFloor(target, min = 0, max = elevator.floors.length, index = Math.floor((max - min) / 2) + min) {

      var floors = elevator.floors;
      var elem = floors[index]

      if (target === elem) { // base case
        return false;
      }

      if (target < elem) {
        if (index === 0 || target > floors[index - 1]) {
          return index;
        }

        return findFloor(target, min, index - 1);
      } else {
        if (index === floors.length - 1 || target < floors[index + 1]) {
          return index + 1;
        }

        return findFloor(target, index + 1, max)
      }
    }

    function addFloor(floorNumber, index) {
      elevator.floors.splice(index, 0, floorNumber);
    }

    var floorInd = elevator.floors.length === 0 ? 0 : findFloor(floorNum);

    if (floorInd !== false) {
      addFloor(floorNum, floorInd);
    }
  }

  function runElevator(floors) {
    while (floors.length) {
      floors.pop();
      numStops++;
    }
  }

  function emptyElevator(elevatorObj) {
    numStops++; // stop at first floor to drop off
    elevatorObj.weight = 0;
    elevatorObj.numPeople = 0;
    elevatorObj.floors = [];
  }

  while (personIndex < totalPeople) {

    while (canAdd(personIndex)) {
      addPerson(personIndex);
    }

    runElevator(elevator.floors);
    emptyElevator(elevator);
  }


  return numStops;
}

var assert = function(a, b) {
	if (a === b) {
		console.log('success')
	} else {
		console.log('Expected ' + a + ' to equal ' + b);
	}
}

assert(solution([60, 80, 40], [2, 3, 5], 5, 2, 200), 5);
assert(solution([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 3, 5, 200), 6);