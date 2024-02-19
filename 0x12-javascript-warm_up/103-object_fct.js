#!/usr/bin/node
const incrFunction = function () {
  this.value++;
};

const myObject = {
  type: 'object',
  value: 12,
  incr: incrFunction
};

console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
