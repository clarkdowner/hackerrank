function main(expression) {
  var t = parseInt(readLine());
  for(var a0 = 0; a0 < t; a0++){
    var expression = readLine();
    var good = true;
    var arrayStore = [];
    for (var i = 0; i < expression.length; i ++) {
      if (expression[i] === '[' || expression[i] === '{' || expression[i] === '(') {
        arrayStore.push(expression[i]);
      } else if (expression[i] === ']') {
        arrayStore[arrayStore.length - 1] === '[' ? arrayStore.pop() : good = false;
      } else if (expression[i] === '}') {
        arrayStore[arrayStore.length - 1] === '{' ? arrayStore.pop() : good = false;
      } else if (expression[i] === ')') {
        arrayStore[arrayStore.length - 1] === '(' ? arrayStore.pop() : good = false;
      } else {
        console.log('Unexpected character at position ', i);
      }
    }
    if (good === true && arrayStore.length === 0) {
      console.log('YES');
    } else {
      console.log('NO');
    }
  }
}
