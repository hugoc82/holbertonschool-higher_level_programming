#!/usr/bin/node
const fs = require('fs'); // Import the File System module

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Use fs.writeFile to write the string to the specified file
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err); // If an error occurs, print it
  }
});
