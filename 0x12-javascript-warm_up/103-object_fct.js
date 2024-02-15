#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};

console.log(myObject);
// Increment the value
myObject.incr();
console.log(myObject); // Should show value: 13
myObject.incr();
console.log(myObject); // Should show value: 14
myObject.incr();
console.log(myObject); // Should show value: 15
