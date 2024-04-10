#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  for (let i = 0; i < Math.floor(len / 2); i++) {
    [list[i], list[len - 1 - i]] = [list[len - 1 - i], list[i]];
  }
  return list;
};
