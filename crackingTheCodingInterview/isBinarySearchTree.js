// not available yet in JavaScript

// the way I would approach this:

// if node.left
  // if node.left.value >= node.value
  	// return false
  // recursive call on node.left

// if node.right
  // if node.right.value <= node.value
    // return false
  // reucursive call on node.right

// return true
