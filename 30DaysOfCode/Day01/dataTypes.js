let tester = () => {
  let i = 4;
  let d = 4.0;
  let s = 'HackerRank';
  let args = [...arguments];
  // Declare second integer, double, and String variables.
  // Read and save an integer, double, and String to your variables.
  let i2 = args[0];
  let d2 = args[1];
  let s2 = args[2];
  // Print the sum of both integer variables on a new line.
  console.log(i + i2);
  // Print the sum of the double variables on a new line.
  console.log(d + d2);
  // Concatenate and print the String variables on a new line
  // The 's' variable above should be printed first.
  console.log(s + s2);
}

