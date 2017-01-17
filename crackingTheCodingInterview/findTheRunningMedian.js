function main() {
  var n = parseInt(readLine());
  var a = [];
  var s = [];
  var even = true;

  var findIndex = function(element) {
    if (s.length === 0 || element <= s[0]) {
      return 0;
    }
    if (s[s.length - 1] <= element) {
      return s.length;
    }

    var lowerBound = 0; 
    var upperBound = s.length; 
    var index = Math.floor((upperBound - lowerBound) / 2) + lowerBound; 

    while(!(s[index - 1] <= element && s[index] >= element)) {
      if (s[index - 1] > element) {
        upperBound = index;
      } else {
        lowerBound = index;
      }
      index = Math.floor((upperBound - lowerBound) / 2) + lowerBound;
    }
    return index;
  }

  for (var i = 0; i < n; i++) {
    a[i] = parseInt(readLine());
    // find index where a[i] belongs in sorted array
    var sortedIndex = findIndex(a[i], a);
    // insert into sorted array
    s.splice(sortedIndex, 0, a[i]);
    even = !even;
    
    // find median
    var median;
    if (even) {
      median = (s[(s.length / 2) - 1] + s[s.length / 2]) / 2;
    } else {
      median = s[Math.floor(s.length / 2)];
    }
    // console median
    median % 1 === 0 ? console.log(median + '.0') : console.log(median);
  }
}