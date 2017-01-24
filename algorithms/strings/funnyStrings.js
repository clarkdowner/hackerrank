function processData(input) {
  var strings = input.split('\n');
  for (var i = 1; i < strings.length; i++) {
  	var funny = true;
  	for (var j = 0; j < strings[i].length / 2; j++) {
  		var front = Math.abs(strings[i].charCodeAt(j) - strings[i].charCodeAt(j + 1));
  		var back = Math.abs(strings[i].charCodeAt(strings[i].length - 1 - j) - strings[i].charCodeAt(strings[i].length - 2 - j));
  		if (front !== back) {
  			funny = false;
  		}
  	}
  	funny ? console.log('Funny') : console.log('Not Funny');
  }
} 