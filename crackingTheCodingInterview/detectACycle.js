//  Cannot be solved with JavaScript on the website at this time


/*  How I would approach it:
 *  
 *  As a race, one pointer would advance a single node (node.next)
 *  at a time, while a second would advance two nodes (node.next.next)
 *  at a time.
 *  
 *  If pointerTwo reaches a node where node.next.next is undefined or recieves
 *  a reference error, then we've reached the end of the list and we do
 *  not have a cycle. Print 0 and return.
 *  
 *  Else if pointerTwo is equal to pointerOne (they are referencing the same object)
 *  at any step, then we do have a cycle. Print 1 and return.
 */  
  