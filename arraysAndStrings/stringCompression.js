var stringComp = function(string) {
  if (!string) {
    return '';
  }

	var redString = ''
  var letter = string.charAt(0);
  var count = 0;

  for (var i = 0; i < string.length; i++) {
    if (string.charAt(i) === letter) {
      count++;
    } else {
      redString += '' + letter + count;
      letter = string.charAt(i);
      count = 1;
    }
  }
  redString += '' + letter + count;

  return redString.length < string.length ? redString : string;
}


console.log(stringComp('aabcccccaaa')); // a2b1c5a3
console.log(stringComp('aaaaaaaaa')); // a9
console.log(stringComp('aaaAAAaaa')); // a3A3a3
console.log(stringComp('abcdef')); // abcdef
console.log(stringComp('aabbcc')); // aabbcc
console.log(stringComp('')); ''