#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let nums = process.argv.slice(2).map(Number);
  nums = nums.sort(function (a, b) { return b - a; });
  const result = nums[1];
  console.log(result);
}
