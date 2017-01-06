function main() {
  var m_temp = readLine().split(' ');
  var m = parseInt(m_temp[0]);
  var n = parseInt(m_temp[1]);
  magazine = readLine().split(' ');
  ransom = readLine().split(' ');
    
  var magazineHashStore = {}  
  for (var i = 0; i < magazine.length; i++) {
    if (magazineHashStore[magazine[i]] === undefined) {
      magazineHashStore[magazine[i]] = 1;
    } else {
      magazineHashStore[magazine[i]]++;
    }
  }
  var good = true;
  for (var j = 0; j < ransom.length; j++) {
    if (magazineHashStore[ransom[j]] === 0 || magazineHashStore[ransom[j]] === undefined) {
      good = false;      
    } else {
      magazineHashStore[ransom[j]]--;
    }
  }
  good ? console.log('Yes') : console.log('No');
}