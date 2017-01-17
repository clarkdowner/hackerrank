function main() {
  var t = parseInt(readLine());
  for(var a0 = 0; a0 < t; a0++){
  	// money
    var m = parseInt(readLine());
    // number of ice creams
    var n = parseInt(readLine());
    a = readLine().split(' ');
    // array of costs
    a = a.map(Number);


    var hashStore = {};
    var found = false;
        
    while (!found) {
      for (var i = 0; i < a.length; i++) {
        hashStore[a[i]] = [true, i + 1];
        if (!found && a[i] !== m - a[i] && hashStore[m - a[i]] !== undefined) {
        	console.log(Math.min(hashStore[a[i]][1], hashStore[m - a[i]][1]) + ' ' + Math.max(hashStore[a[i]][1], hashStore[m - a[i]][1]));
        	found = true;
        }
      }   
    }
  }
}
