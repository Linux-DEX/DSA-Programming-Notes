// assign()
// The Object.assign() static method copies all enumerable own properties from one or more source objects to a target object. It returns the modified target object.

const target = { a: 1, b: 2 };
const source = { b: 4, c: 5 };

const returnedTarget = Object.assign(target, source);

console.log(target); // output: { a: 1, b: 4, c: 5 }
console.log(returnedTarget === target); // output: true


// create()
// The Object.create() static method creates a new object, using an existing object as the prototype of the newly created object.

const person = {
  isHuman: false,
  printIntroduction: function () {
    console.log(`My name is ${this.name}. Am I human? ${this.isHuman}`);
  },
};

const me = Object.create(person);

me.name = "Matthew"; // "name" is a property set on "me", but not on "person"
me.isHuman = true; // Inherited properties can be overwritten

me.printIntroduction(); // output: "My name is Matthew. Am I human? true"


// defineProperties()
// The Object.defineProperties() static method defines new or modifies existing properties directly on an object, returning the object.

const object1 = {};

Object.defineProperties(object1, {
  property1: {
    value: 42,
    writable: true,
  },
  property2: {},
});

console.log(object1.property1); // output: 42


// defineProperty()
// The Object.defineProperty() static method defines a new property directly on an object, or modifies an existing property on an object, and returns the object.

const object2 = {};

Object.defineProperty(object2, "property1", {
  value: 42,
  writable: false,
});

// object2.property1 = 77; // Throws an error in strict mode

console.log(object2.property1); // output: 42


// entries()
// The Object.entries() static method returns an array of a given object's own enumerable string-keyed property key-value pairs.

const object3 = {
  a: "somestring",
  b: 42,
};

for (const [key, value] of Object.entries(object3)) {
  console.log(`${key}: ${value}`);
}
/*
  output:
  a: somestring 
  b: 42
*/


// freeze()
// The Object.freeze() static method freezes an object. Freezing an object prevents extensions and makes existing properties non-writable and non-configurable. A frozen object can no longer be changed: new properties cannot be added, existing properties cannot be removed, their enumerability, configurability, writability, or value cannot be changed, and the object's prototype cannot be re-assigned. freeze() returns the same object that was passed in.

const obj = {
  prop: 42,
};
Object.freeze(obj);

// Throws an error in strict mode
// obj.prop = 33;

console.log(obj.prop); // output: 42


// fromEntries()
// The Object.fromEntries() static method transforms a list of key-value pairs into an object.

const entries = new Map([
  ["foo", "bar"],
  ["baz", 42],
]);

const obj1 = Object.fromEntries(entries);

console.log(obj1); // output: Object { foo: "bar", baz: 42 }


// getOwnPropertyDescriptor()
// The Object.getOwnPropertyDescriptor() static method returns an object describing the configuration of a specific property on a given object (that is, one directly present on an object and not in the object's prototype chain). The object returned is mutable but mutating it has no effect on the original property's configuration.

const object4 = {
  property1: 42,
};

const descriptor1 = Object.getOwnPropertyDescriptor(object4, "property1");

console.log(descriptor1.configurable); // output: true
console.log(descriptor1.value); // output: 42


// getOwnPropertyDescriptors() 
// The Object.getOwnPropertyDescriptors() static method returns all own property descriptors of a given object.

const object5 = {
  property1: 42,
};

const descriptors2 = Object.getOwnPropertyDescriptors(object5);

console.log(descriptors2.property1.writable); // output: true
console.log(descriptors2.property1.value); // output: 42


// getOwnPropertyNames()
// The Object.getOwnPropertyNames() static method returns an array of all properties (including non-enumerable properties except for those which use Symbol) found directly in a given object.

const object6 = {
  a: 1,
  b: 2,
  c: 3,
};

console.log(Object.getOwnPropertyNames(object6)); // output: Array ["a", "b", "c"]


// getOwnPropertySymbols()
// The Object.getOwnPropertySymbols() static method returns an array of all symbol properties found directly upon a given object.

const object7 = {};
const a = Symbol("a");
const b = Symbol.for("b");

object7[a] = "localSymbol";
object7[b] = "globalSymbol";

const objectSymbols = Object.getOwnPropertySymbols(object7);

console.log(objectSymbols.length); // output: 2


// getPrototypeOf()
// The Object.getPrototypeOf() static method returns the prototype (i.e. the value of the internal [[Prototype]] property) of the specified objec

const prototype1 = {};
const object8 = Object.create(prototype1);

console.log(Object.getPrototypeOf(object8) === prototype1); // output: true


// groupBy()
// The Object.groupBy() static method groups the elements of a given iterable according to the string values returned by a provided callback function. The returned object has separate properties for each group, containing arrays with the elements in the group.

const inventory = [
  { name: "asparagus", type: "vegetables", quantity: 9 },
  { name: "bananas", type: "fruit", quantity: 5 },
  { name: "goat", type: "meat", quantity: 23 },
  { name: "cherries", type: "fruit", quantity: 12 },
  { name: "fish", type: "meat", quantity: 22 },
];

const restock = { restock: true };
const sufficient = { restock: false };
const result = Object.groupBy(inventory, ({ quantity }) =>
  quantity < 6 ? "restock" : "sufficient",
);
console.log(result.restock); // output: [{ name: "bananas", type: "fruit", quantity: 5 }]


// hasOwn()
// The Object.hasOwn() static method returns true if the specified object has the indicated property as its own property. If the property is inherited, or does not exist, the method returns false.

const object9 = {
  prop: "exists",
};

console.log(Object.hasOwn(object9, "prop")); // output: true
console.log(Object.hasOwn(object9, "toString")); // output: false
console.log(Object.hasOwn(object9, "undeclaredPropertyValue")); // output: false


// is()
// The Object.is() static method determines whether two values are the same value.

console.log(Object.is("1", 1)); // output: false
console.log(Object.is(NaN, NaN)); // output: true
console.log(Object.is(-0, 0)); // output: false

const obj3 = {};
console.log(Object.is(obj3, {})); // output: false


// isExtensible()
// The Object.isExtensible() static method determines if an object is extensible (whether it can have new properties added to it).

const object10 = {};

console.log(Object.isExtensible(object10)); // output: true
Object.preventExtensions(object10);
console.log(Object.isExtensible(object10)); // output: false


// isFrozen()
// The Object.isFrozen() static method determines if an object is frozen.

const object11 = {
  property1: 42,
};

console.log(Object.isFrozen(object11)); // output: false

Object.freeze(object11);
console.log(Object.isFrozen(object11)); // output: true


// isSealed()
// The Object.isSealed() static method determines if an object is sealed.

const object12 = {
  property1: 42,
};
console.log(Object.isSealed(object12)); // output: false

Object.seal(object12);
console.log(Object.isSealed(object12)); // output: true


// keys()
// The Object.keys() static method returns an array of a given object's own enumerable string-keyed property names.

const object13 = {
  a: "somestring",
  b: 42,
  c: false,
};

console.log(Object.keys(object13)); // output: Array ["a", "b", "c"]


// preventExtensions()
// The Object.preventExtensions() static method prevents new properties from ever being added to an object (i.e. prevents future extensions to the object). It also prevents the object's prototype from being re-assigned.

const object14 = {};

Object.preventExtensions(object14);

try {
    Object.defineProperty(object14, "property1", {
    value: 42,
  });
} catch (e) {
  console.log(e); // Expected output: TypeError: Cannot define property property1, object is not extensible
}


// seal()
// The Object.seal() static method seals an object. Sealing an object prevents extensions and makes existing properties non-configurable. A sealed object has a fixed set of properties: new properties cannot be added, existing properties cannot be removed, their enumerability and configurability cannot be changed, and its prototype cannot be re-assigned. Values of existing properties can still be changed as long as they are writable. seal() returns the same object that was passed in.

const object15 = {
  property1: 42,
};

Object.seal(object15);
object15.property1 = 33;
console.log(object15.property1); // output: 33

// delete object15.property1; // Cannot delete when sealed
console.log(object15.property1); // output: 33


// setPrototypeOf()
// The Object.setPrototypeOf() static method sets the prototype (i.e., the internal [[Prototype]] property) of a specified object to another object or null.

const obj4 = {};
const parent = { foo: "bar" };

console.log(obj4.foo); // output: undefined

Object.setPrototypeOf(obj4, parent);
console.log(obj4.foo); // output: "bar"


// values()
// The Object.values() static method returns an array of a given object's own enumerable string-keyed property values.

const object16 = {
  a: "somestring",
  b: 42,
  c: false,
};

console.log(Object.values(object16)); // output: Array ["somestring", 42, false]


