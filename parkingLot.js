// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(E, L) {

  var convertToMinutes = function(time) {
  	var time = time.split(':');
  	var hours = 1 * time[0];
  	var min = 1 * time[1];

  	var totalMin = (hours * 60) + min
  	return totalMin
  }

  var enter = convertToMinutes(E);
  var leave = convertToMinutes(L);

  var parkedTime = leave - enter;

  var hoursParked = Math.ceil(parkedTime / 60);

  var cost = 2; // enter fee
  cost += 3; // first hour, some portion will always be used

  return hoursParked <= 1 ? cost : cost + (4 * (hoursParked - 1)); // remaining hours
}

var assert = function(a, b) {
	if (a === b) {
		console.log('success')
	} else {
		console.log('Expected ' + a + ' to equal ' + b);
	}
}


assert(solution('10:00', '13:21'), 17);
assert(solution('09:42', '11:42'), 9);