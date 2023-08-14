#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let size = 0;
    let mySquare = '';

    while (size < x) {
      mySquare = mySquare + 'X';
      size++;
    }
    console.log(mySquare);
  }
}
