function print(head) {
  if (head !== null) {
    console.log(head.data);
    print(head.next);
  }
}