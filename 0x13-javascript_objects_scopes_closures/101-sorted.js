#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = {};
for (const uID in dict) {
  const occurrences = dict[uID];
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(uID);
}
console.log(newDict);
