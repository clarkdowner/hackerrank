var merge = function(leftHalf, rightHalf) {
	var mergedArrays = [];
	var leftPoint = 0;
	var rightPoint = 0;

	while (leftPoint < leftHalf.length && rightPoint < rightHalf.length) {
		if (leftHalf[leftPoint] < rightHalf[rightPoint]) {
			mergedArrays.push(leftHalf[leftPoint]);
			leftPoint++;
		} else {
			mergedArrays.push(rightHalf[rightPoint]);
			rightPoint++;
		}
	}

	while (leftPoint < leftHalf.length) {
		mergedArrays.push(leftHalf[leftPoint]);
		leftPoint++;
	}

	while (rightPoint < rightHalf.length) {
		mergedArrays.push(rightHalf[rightPoint]);
		rightPoint++;
	}

	return mergedArrays;
}

var mergeSort = function(array) {
	if (array === undefined || array.length === 0) {
		return [];
	}
	if (array.length < 2) {
		return array;
	}

	// split halves logic
	var midpoint = Math.max(array.length / 2);
	var leftHalf = array.slice(0, midpoint);
	var rightHalf = array.slice(midpoint);

	var left = mergeSort(leftHalf);
	var right = mergeSort(rightHalf);
	return merge(left, right);
}



var assert = function(a, b) {
	var same = true;
	if (a.length !== b.length) {
		same = false;
	} 
	for (var i = 0; same && i < a.length; i++) {
		if (a[i] !== b[i]) {
			same = false;
		}
	}
	if (same) {console.log('success');}
	else {console.log('Expected ' + a + ' to equal ' + b);}
}

// test cases: 
var test1 = [1,2,3,4,5];
var test2 = [5,4,3,2,1];
var test3 = [];
var test4 = [1,1,1,1,1];
var test5 = [1,2,3,4,5,6,7,8];
var test6 = [1,2,6,5,4,3,7,8];
var test7 = [4,2,7,1,8,5,6,3];
assert(mergeSort(test1), [1,2,3,4,5]);
assert(mergeSort(test2), [1,2,3,4,5]);
assert(mergeSort(test3), []);
assert(mergeSort(test4), [1,1,1,1,1]);
assert(mergeSort(test5), [1,2,3,4,5,6,7,8]);
assert(mergeSort(test6), [1,2,3,4,5,6,7,8]);
assert(mergeSort(test7), [1,2,3,4,5,6,7,8]);