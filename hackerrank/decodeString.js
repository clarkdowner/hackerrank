// Let 1 represent ‘A’, 2 represents ‘B’, 26 represents ‘Z’ etc. 
// Given a digit sequence, count the number of possible decodings of the given digit sequence.

// ex: 121 --> 3 (ABA, LA, AU)

// the input is a string


function decodeString(string) {
	if (string.length === 0) {
		return 0;
	}

	var poss = 1;

	for (var i = 0; i < string.length; i++) {

		var char = string.charAt(i);

		if (char === '0') {
			if (i === 0) {
				return false;
			}
			var prev = string.charAt(i - 1);
			if (!(prev === '1' || prev === '2')) {
				return false;
			}
			poss -= 2;
		}

		if (char === '1' && i !== string.length - 1) {
			poss += 1;
		}

		if (char === '2' && i !== string.length - 1) {
			var next = 0 + string.charAt(i + 1);
			if (next < 7) {
				poss += 1;
			}
		}
	}

	return poss;
}

function assert(a, b) {
	if (a === b) { console.log('success'); }
	else { console.log('expected ' + a + ' to equal ' + b); }
}

assert(decodeString('1210'), 2);
assert(decodeString('120'), 1);
assert(decodeString('121'), 3);
assert(decodeString('12'), 2);
assert(decodeString('0121'), false);
assert(decodeString('12001'), false);
assert(decodeString('128'), 2);
assert(decodeString('1535'), 2);
assert(decodeString('1226'), 4);
assert(decodeString('30'), false);