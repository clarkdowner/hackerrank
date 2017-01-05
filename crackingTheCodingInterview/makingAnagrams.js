function main() {
  var a = readLine();
  var b = readLine();
  
  var hash = {};
  
  for (var i = 0; i < a.length; i++) {
    if (hash[a[i]] === undefined) {
      hash[a[i]] = 1;
    } else {
      hash[a[i]]++;
    }
  }
  
  for (var i = 0; i < b.length; i++) {
    if (hash[b[i]] === undefined) {
      hash[b[i]] = -1;
    } else {
      hash[b[i]]--;
    }
  }
  
  var total = 0;
  for (var key in hash) {
    total += Math.abs(hash[key]);
  }
  console.log(total);
}
