function processData(input) {
  //Enter your code here
  var input = input.split('\n')
  for (var i = 0; i < input.length; i++) {
      input[i] = input[i].split(' ');       
  }
  var buildArray = [];
  for (var i = 0; i < input[0][0]; i++) {
      buildArray.push(0);
  }
  for (var i = 1; i < input.length; i++) {
      for (var j = input[i][0] - 1; j < input[i][1]; j++) {
          buildArray[j] += +input[i][2];
      }
  }
  console.log(Math.max(...buildArray));
}