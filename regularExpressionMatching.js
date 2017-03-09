/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(string, regEx, inProcess = false) {
  // console.log('string: ', string)
  // console.log('regEx: ', regEx)
  // console.log('inProcess: ', inProcess)
  if (string === false || string === undefined || string.length === 0) {
    // return regEx.length === 0 ? true : false;
  }
  if (regEx === undefined || regEx.length === 0) {
    return false;
  }

  // console.log('preSlice: ', string)
  if (string.length > 1) {
    var rString = string.slice(1);
  }
  if (regEx.length > 1) {
    var rRegEx = regEx.slice(1);
  }
  // console.log('string: ', string)
  if (regEx.charAt(0) === '.' || regEx.charAt(0) === string.charAt(0)) {
    return string.length === 1 ? true : isMatch(rString, rRegEx, true);
  
  } else if (regEx.charAt(0) === '*') {
    // if (regEx === '*a') { console.log('hit')}
    if (regEx.length === 1) { return true; }

    var nextRegExChar = regEx.charAt(1);
    var possibleStrings = [];

    for (var i = 1; i < string.length; i++) {
      if (string[i] === nextRegExChar) {
        var possString = string.slice(i);
        possibleStrings.push(possString);
      }
    }

    if (possibleStrings.length === 0) { return false; }
    // if (regEx === '*a') { 
    //   console.log('possibleStrings: ', possibleStrings); 
    //   console.log('rRegEx: ', rRegEx)
    // }

    // // var reductionHelper = (pre, cur) => isMatch(pre, curr, true);
    // possibleStrings.reduce((partial, reduction) => {
    //   // console.log('partial: ', partial)
    //   // console.log('reduction: ', reduction)
    //   // console.log('rRegEx: ', rRegEx)
    //   return isMatch(partial, rRegEx, true) || reduction;
    // }, false);
    possibleStrings.some(partial => isMatch(partial, rRegEx, true));

  } else {
    return inProcess ? false : isMatch(rString, regEx);
  }
  // console.log('string: ', string)
  // console.log('regEx: ', regEx)
  // console.log('ending')
  return true;
};

var assert = function(a, b) {
  if (a === b) { console.log('success'); }
  else { console.log('Expected ' + a + ' to equal ' + b); }
}

assert(isMatch("aa","a"), false);
assert(isMatch("aa","aa"), true);
assert(isMatch("aaa","aa"), false);
assert(isMatch("aa", "a*"), true);
assert(isMatch("aa", ".*"), true);
assert(isMatch("ab", ".*"), true);
assert(isMatch("aab", "c*a*b"), true);
assert(isMatch('a', 'a', false), true);
assert(isMatch('aa', '*a'), true);
assert(isMatch('aaa', 'a*a'), true);
assert(isMatch('abcd', 'd*'), false);

