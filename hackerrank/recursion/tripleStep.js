// Naive
var tSteps = function(numSteps) {
  var poss = 0;
  var possSteps = [1,2,3];

  var helper = function(steps) {
    if (steps === 0) {
      poss++;
      return;
    } else if (steps < 0) {
      return;
    } else {
      for (var i = 0; i < possSteps.length; i++) {
        helper(steps - possSteps[i]);
      }
    }
  };
  helper(numSteps);
  return poss;
};

// Dynamic
var tSteps = function(n) {
  if (n < 0) {
    return 0;
  } else if (n === 0) {
    return 1;
  } else {
    return tSteps(n - 1) + tSteps(n - 2) + tSteps(n - 3);
  }
};

console.log(tSteps(1)); // 1
console.log(tSteps(2)); // 2
console.log(tSteps(3)); // 4
console.log(tSteps(4)); // 7
console.log(tSteps(5)); // 13