#!/usr/bin/node
function findSecondBiggest (args) {
  if (args.length < 3) {
    return 0; // Return 0 if less than 2 arguments are provided
  }
  const numbers = args.map(Number); // Convert arguments to numbers
  let [biggest, secondBiggest] = numbers[0] > numbers[1] ? [numbers[0], numbers[1]] : [numbers[1], numbers[0]];

  for (let i = 2; i < numbers.length; i++) {
    if (numbers[i] > biggest) {
      secondBiggest = biggest;
      biggest = numbers[i];
    } else if (numbers[i] > secondBiggest) {
      secondBiggest = numbers[i];
    }
  }

  return secondBiggest;
}

const args = process.argv.slice(2);
console.log(findSecondBiggest(args));
