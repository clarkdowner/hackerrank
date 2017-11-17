
var add = function(arg) {
	var sum = 0;

	var curryAdd = function(num) {
		if (num === undefined) {
			return sum;
		} else {
			sum += num;
			return curryAdd;
		}
	}

	return curryAdd(arg);
}



var assert = function(a, b) {
	a === b ? console.log('Success!') : console.log('Failed :(, expected ' + a + ' to equal ' + b);
}

assert(add(), 0);
assert(add(-1)(), -1);
assert(add(1)(2)(3)(), 6);
assert(add(0)(0)(), 0);
assert(add(-1)(1)(), 0);
assert(add(10)(10)(10)(10)(10)(10)(10)(), 70);