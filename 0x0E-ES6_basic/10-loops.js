#!/usr/bin/node
export default function appendToEachArrayValue(array, appendString) {
  const array2 = [];
  for (let idx of array) {
    idx = appendString + idx;
    array2.push(idx);
  }

  return array2;
}
