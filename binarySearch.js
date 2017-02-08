var search = function(array, target) {
   min = 0; 
   max = array.length - 1; 
   
   while (min <= max) {
      var searchAt = Math.floor((max - min) / 2) + min;
      if (array[searchAt] === target) {
         return searchAt;
      } else if (array[searchAt] < target) {
         min = searchAt + 1;
      } else {
         max = searchAt - 1;
      }
   }

   return -1;
}


console.log(search([2, 4, 5, 9, 12, 17], 2)); // 0
console.log(search([2, 4, 5, 9, 12, 17], 17)); // 5
console.log(search([2, 4, 5, 9, 12, 17], 13));// -1
console.log(search([2, 4, 5, 9, 12, 17], 1));// -1
console.log(search([2, 4, 5, 9, 12, 17], 12));// 4
console.log(search([2, 4, 5, 9, 12, 17], 9));// 3