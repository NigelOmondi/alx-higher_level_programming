#!/usr/bin/node
const numArguments = process.argv.length;
console.log(numArguments === 2 ? 'No argument' : numArguments === 3 ? 'Argument found' : 'Arguments found');
