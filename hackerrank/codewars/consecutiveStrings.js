// You are given an array strarr of strings and an integer k. 
// Your task is to return the first longest string consisting of k consecutive strings taken in the array.

// Example:

// longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

// n being the length of the string array, if n = 0 or k > n or k <= 0 return ""

function longestConsec(strarr, k) {
  var n = strarr.length;
  if (n === undefined || n === 0 || k > n || k <= 0) {
    return '';
  }

  var index = 0;
  var currConsec = [];
  var currConCount = 0;

  for (var i = 0; i < k; i++) {
    currConsec.push(strarr[i].length);
    currConCount += strarr[i].length;
  }

  var longestConCount = currConCount;


  for (var i = 0; i < n - k; i++) {
    var drop = currConsec.shift();
    currConCount -= drop;
    var add = strarr[i + k].length;
    currConsec.push(add);
    currConCount += add;

    if (currConCount > longestConCount) {
      var longestConCount = currConCount;
      var index = i + 1;
    }
  }

  var returnString = '';

  for (var i = index; i < index + k; i++) {
    returnString += strarr[i];
  }

  return returnString;
}
