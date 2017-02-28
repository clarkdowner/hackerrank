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
		// if (i < string.length - 1 && (string.charAt(i) === '1' || string.charAt(i) === '2')) {
		// 	poss++;
		// }
	}

	return poss;
}


console.log(decodeString('121') === 3);
console.log(decodeString('12') === 2);
console.log(decodeString('1210') === 2);
console.log(decodeString('0121') === false);
console.log(decodeString('12001') === false);
console.log(decodeString('120') === 1);
console.log(decodeString('128') === 2);
console.log(decodeString('1535') === 2);
console.log(decodeString('1226') === 4);
console.log(decodeString('30') === false);