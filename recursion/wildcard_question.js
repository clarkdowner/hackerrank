
function get(doc, path, travelled, pathObj) {

  if (path === '' && travelled === undefined) {
    return {};
  }

  pathObj = pathObj || {};
  travelled = travelled || ''

  if (path.length === 0) {
    pathObj[travelled] = doc;
  }

  if (path.charAt(0) === '.') {
    path = path.slice(1);
  }

  if (path.charAt(0) !== '*') {
    if (doc[path.charAt(0)] !== undefined) {
      travelled += path.charAt(0)
      get(doc[path.charAt(0)], path.slice(1), travelled, pathObj);
    }
  }

  if (path.charAt(0) === '*') {
    for (var key in doc) {
      var wildPath = travelled + key;
      get(doc[key], path.slice(1), wildPath, pathObj);
    }
  }

  return pathObj;
}

doc = {
  'a': {
    'b': {
      'c': 'hello'
    },
    'd': {
      'c': 'sup',
      'e': {
        'f': 'blah blah blah'
      }
    }
  }
}

console.log(get(doc, 'a.d.e.f'))
// {'a.d.e.f': 'blah blah blah'}

console.log(get(doc, 'a.*.c'))
// // {'a.b.c': 'hello', 'a.d.c': 'sup'}

console.log(get(doc, 'a.*.e'))
// // {'a.d.e': {'f': 'blah blah blah'}}}

console.log(get(doc, 'a.b.c.e.*'))
// // {}

console.log(get(doc, '*'))
// // {'a':{'b':{'c':'hello'},'d':{'c':'sup','e':{'f':'blah blah blah'}}}}

console.log(get(doc, ''))
// // {}
