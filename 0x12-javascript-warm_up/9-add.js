#!/usr/bin/node
function add (a, b) {
  const S = a + b;
  console.log(S);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
