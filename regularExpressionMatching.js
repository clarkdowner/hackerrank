// /**
//  * @param {string} s
//  * @param {string} p
//  * @return {boolean}
//  */
// var isMatch = function(string, regEx, inProcess = false) {
//   // console.log('string: ', string)
//   // console.log('regEx: ', regEx)
//   // console.log('inProcess: ', inProcess)

//   if (string === false || string === undefined || string.length === 0) {
//     return true;
//   }
//   if (regEx === undefined || regEx.length === 0) {
//     return false;
//   }



//   if (regEx.charAt(0) === '.' || regEx.charAt(0) === string.charAt(0)) {
//     if (string.length === 1) { 
//       return regEx.length === 1 ? true : false; 
//     }

//     var rString = string.slice(1);
//     var rRegEx = regEx.slice(1);

//     return isMatch(rString, rRegEx, true);
  
//   } else if (regEx.charAt(0) === '*') {
//     if (regEx.length === 1) { return true; }

//     var nextRegExChar = regEx.charAt(1);
//     var possibleStrings = [];

//     for (var i = 1; i < string.length; i++) {
//       if (string[i] === nextRegExChar) {
//         var possString = string.slice(i);
//         possibleStrings.push(possString);
//       }
//     }
//     console.log(possibleStrings)
//     if (possibleStrings.length === 0) { return false; }
    
//     var rRegEx = regEx.slice(1);
//     return possibleStrings.some(partial => isMatch(partial, rRegEx, inProcess));

//   } else {
//     // console.log('string: ', string)
//     // console.log('regEx: ', regEx)
//     // console.log('inProcess: ', inProcess)
//     var possibleRegExes = [regEx];
//     for (var i = 1; i < regEx.length; i++) {
//       if (regEx[i] === '*') {
//         var possRegEx = regEx.slice(i);
//         possibleRegExes.push(possRegEx);
//       }
//     }

//     var rString = string.slice(1);
//     return inProcess ? false : isMatch(rString, regEx);
//   }
//   // console.log('string: ', string)
//   // console.log('regEx: ', regEx)
//   // console.log('ending')
//   return true;
// };

var isMatch = function(string, regEx, sInd = 0, rInd = 0, inProcess = false) {
  var rLen = regEx.length;
  var sLen = string.length;

  if (sInd > sLen) {
    return false;
  }

  // Match multiple
  if (regEx[rInd] === '*') {
    if (rInd === rLen - 1) {
      console.log('80')
      return true;
    }

    var nextRegExChar = regEx[rInd + 1];
    var possibleStrings = [];
    for (var i = sInd; i < sLen; i++) {
      if (string[i] === nextRegExChar) {
        possibleStrings.push(i);
      }
    }

    if (possibleStrings.length === 0) {
      return false;
    } else {
      return possibleStrings.reduce((acc, index) => {
        return isMatch(string, regEx, index, rInd + 1, inProcess) || acc;
      }, false);
    }
  }

  // Match single
  else if (regEx[rInd] === '.' || regEx[rInd] === string[sInd]) {
    console.log('string: ', string)
    console.log('regEx: ', regEx)
    console.log('sInd: ', sInd)
    console.log('rInd: ', rInd)
    //if end of string
    if (sInd === sLen - 1) {
      console.log('105')
      return rInd === rLen - 1 ? true : false;
    }
    return isMatch(string, regEx, sInd + 1, rInd + 1, true);
  }

  // No match
  else {
    var noMatchHelper = function() {      
      var possibleRegExes = [];
      for ( var i = rInd; i < rLen; i++) {
        if (regEx[i] === '*') {
          possibleRegExes.push(i);
        }
      }

      if (possibleRegExes.length === 0) {
        return false;
      } else {
        return possibleRegExes.reduce((acc, index) => {
          return isMatch(string, regEx, 0, index, false) || acc;
        }, false);
      }
    }

    return isMatch(string, regEx, sInd + 1, rInd) || noMatchHelper();
  }

};

var assert = function(a, b) {
  if (a === b) { console.log('success'); }
  else { console.log('Expected ' + a + ' to equal ' + b); }
}

// assert(isMatch("aa","a"), false);
// assert(isMatch("aa","aa"), true);
// assert(isMatch("aaa","aa"), false);
// assert(isMatch("aa", "a*"), true);
// assert(isMatch("aa", ".*"), true);
// assert(isMatch("ab", ".*"), true);
// assert(isMatch('a', 'a'), true);
// assert(isMatch("aab", "a*b"), true);
// assert(isMatch("aab", "c*a*b"), true);
// assert(isMatch('aa', '*a'), true);
// assert(isMatch('aaa', 'a*a'), true);
// assert(isMatch('aaa', '*a'), true);
// assert(isMatch('aaa', 'ab*ac*a'), true);
assert(isMatch('cd', 'd*'), false);
// assert(isMatch('abcd', 'd*'), false);
