function main() {
  var s = parseInt(readLine());
  var memo = {};
  for(var a0 = 0; a0 < s; a0++){
    var n = parseInt(readLine());

    var stepCombos = 0;

    var staircase = function(stairsRemaining) {
      var poss = [3,2,1];

      if (memo[stairsRemaining] !== undefined) {
        stepCombos += memo[stairsRemaining];
        return;
      }

      if (stairsRemaining === 0) {
        stepCombos++;
        return;
      }

      for (var i = 0; i < poss.length; i++) {
        if (stairsRemaining - poss[i] >= 0) {
          staircase(stairsRemaining - poss[i]);
        }
      }

    }

    staircase(n);
    console.log(stepCombos);
    memo[n] = stepCombos;
  }
}