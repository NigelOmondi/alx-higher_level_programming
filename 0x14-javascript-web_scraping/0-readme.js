#!/usr/bin/node

const fs = require('fs');

// Get filename from command line arguments
const fileName = process.argv[2];

// Check if filename was provided as an argument
if (!fileName) {
  console.error('Usage: .0-readme.js <fileName>');
  process.exit(1);
}

// Read the content of the file in utf-8 encoding
fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    // If error occurs during reading
    console.error(err);
  } else {
    // Print the contents of the file
    console.log(data);
  }
});
