#!/usr/bin/node
const myFirstArgument = parseInt(process.argv[2]);
console.log(myFirstArgument ? `My number: ${myFirstArgument}` : 'Not a number');
