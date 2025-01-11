# Aggregate Pipeline

The aggregation pipeline in MongoDB is a framework that processes data through a series of stages, where each stage applies a specific operation (e.g., filtering, grouping, sorting) to transform and analyze the documents in a collection. It allows for complex data manipulation and computation, with the results passed from one stage to the next.

- **Syntax**:

```jsx
db.collection.aggregation([
  { stage1: { operator: { field: value } } },
  { stage2: { operator: { field: value } } },
  ...
]);
```

- **Example**:

```jsx
db.collection.aggregate([
  { $match: { status: "active" } }, // Stage 1: Filter documents where status is "active"
  { $group: { _id: "$category", total: { $sum: "$amount" } } }, // Stage 2: Group by category and calculate the total amount
  { $sort: { total: -1 } }, // Stage 3: Sort by total amount in descending order
]);
```

## Operators

### $abs

Returns the absolute value of a number.

**syntax**

```jsx
{ $abs: <number> }
```

**example**

```jsx
db.files.aggregate([
  {
    $project: {
      Total_Page: {
        $abs: {
          $subtract: ["$File_Page", 1],
        },
      },
    },
  },
]);
```

### $accumulator

### $acos

### $accosh

### $add

### $addToSet

### $allElementsTrue

### $and

Evaluates one or more expressions and return `true` if all of the expressions are `true` or if run with no argument expressions. Otherwise, `$and` returns `false`.

**syntax**

```jsx
{ $and: [ <expression1>, <expression2>, ... ] }
```

**example**

```jsx
db.files.find({
  $and: [
    {
      IsHistorical: False,
    },
    {
      File_Format: "837",
    },
  ],
});

db.files.aggregate([
  {
    $match: {
      $and: [
        {
          IsHistorical: false,
        },
        {
          File_Format: "837",
        },
      ],
    },
  },
]);
```

### $anyElementTrue

### $arrayElemAt

### $arrayToObject

### $asin

### $asinh

### $atan2

### $avg

### $binarySize

### $bitAnd

### $bitNot

### $bitOr

### $bitXor

### $bottom

### $bottomN

### $bottomSize

### $ceil

### $cmp

### $concat

Concatenates strings and returns the concatenated string.

**syntax**

```jsx
{ $concat: [ <expression1>, <expression2>, ... ] }
```

**example**

```jsx
db.files.aggregate([
  {
    $project: {
      fileDetail: {
        $concat: ["$File_Status", "-", "$File_Name"],
      },
    },
  },
]);
```

### $concatArrays

### $cond

### $convert

### $cos

### $cosh

### $count-accumulator

### $dateAdd

### $dateDiff

### $dateFromString

### $dateSubtract

### $dateToParts

### $dateToString

### $dateTrunc

### $dayOfMonth

### $dayOfWeek

### $dayOfYear

### $degreesToRadians

### $denseRank

### $derivative

### $divide

### $documentNumber

### $eq

Compares two values and returns:

- `true` when the values are equivalent.
- `false` when the values are not equivalent.

**syntax**

```jsx
{ $eq: [ <expression1>, <expression2> ] }
```

**example**

```jsx
db.claims_837.find({
  DxCount: {
    $eq: 3,
  },
});

db.claims_837.aggregate([
  {
    $match: {
      DxCount: {
        $eq: 3,
      },
    },
  },
]);
```

### $exp

Raises Euler's number(i.e. e) to the specified exponent and returns the result.

**syntax**

```jsx
{ $exp: <exponent> }
```

**example**

```jsx
db.files.aggregate([
  {
    $project: {
      Total_Page: {
        $subtract: [
          {
            $exp: "$File_Page",
          },
          1,
        ],
      },
    },
  },
]);
```

### $expMovingAvg

### $filter

### $first

### $firstN

### $floor

### $function

### $getField

### $gt

Compares two values and returns:

- `true` when the first value is greater than the second value.
- `false` when the first value is less than or equal to the second value.

**syntax**

```jsx
{ $gt: [ <expression1>, <expression2> ] }
```

**example**

```jsx
db.claims_837.find({
  DxCount: {
    $gt: 3,
  },
});

db.claims_837.aggregate([
  {
    $match: {
      DxCount: {
        $gt: 3,
      },
    },
  },
]);
```

### $gte

Compares two values and returns:

- `true` when the first value is greater than or equal to the second value.
- `false` when the first value is less than or equal to the second value.

**syntax**

```jsx
{ $gt: [ <expression1>, <expression2> ] }
```

**example**

```jsx
db.claims_837.find({
  DxCount: {
    $gte: 3,
  },
});

db.claims_837.aggregate([
  {
    $match: {
      DxCount: {
        $gte: 3,
      },
    },
  },
]);
```

### $hour

### $ifNull

### $indexOfArray

### $indexOfBytes

### $indexOfCP

### $integral

### $isArray

### $isNumber

### $isoDayOfWeek

### $isoWeek

### $isoWeekYear

### $last

### $lastN

### $let

### $linearFill

### $literal

### $in

Returns a boolean indicating whether a specified value is in an array.

**syntax**

```jsx
{ $in: [ <expression>, <array expression> ] }
```

**example**

```jsx
db.files.find({
  File_Status: {
    $in: ["Queued", "Processing"],
  },
});

db.files.aggregate([
  {
    $match: {
      File_Status: {
        $in: ["Queued", "Processing"],
      },
    },
  },
]);
```

### $locf

### $log

### $log10

### $lt

Compare two values and returns:

- `true` when the first value is less than the second value.
- `false` when the first value is greater than or equivalent to the second value.

**syntax**

```jsx
{ $lt: [ <expression1>, <expression2> ] }
```

**example**

```jsx
db.claims_837.find({
  DxCount: {
    $lt: 3,
  },
});

db.claims_837.aggregate([
  {
    $match: {
      DxCount: {
        $lt: 3,
      },
    },
  },
]);
```

### $lte

Compare two values and returns:

- `true` when the first value is less than or equivalent to the second value.
- `false` when the first value is greater than or equivalent to the second value.

**syntax**

```jsx
{ $lt: [ <expression1>, <expression2> ] }
```

**example**

```jsx
db.claims_837.find({
  DxCount: {
    $lt: 3,
  },
});

db.claims_837.aggregate([
  {
    $match: {
      DxCount: {
        $lt: 3,
      },
    },
  },
]);
```

### $ltrim

### $map

### $max

### $maxN

### $maxN-array-element

### $median

### $mergeObjects

### $meta

### $min

### $minN

### $minN-array-element

### $millisecond

### $mod

### $month

### $multiple

### $ne

Compares two values and returns:

- `true` when the values are not equivalent.
- `false` when the values are equivale

**syntax**

```jsx
{ $ne: [ <expression1>, <expression2> ] }
```

**example**

```jsx
db.claims_837.find({
  DxCount: {
    $ne: 3,
  },
});

db.claims_837.aggregate([
  {
    $match: {
      DxCount: {
        $ne: 3,
      },
    },
  },
]);

db.claims_837.aggregate([
  {
    $project: {
      File_Type: 1,
      Status: 1,
      DxCount: {
        $ne: ["$DxCount", 3],
      },
      _id: 0,
    },
  },
]);
```

### $not

Evaluates a boolean and returns the opposite boolean value; i.e. when passed on expression that evaluates to `true`, `$not` returns `false`; when passed an expression that evaluates to `false`, `$not` return `true`.

**syntax**

```jsx
{ $not: [ <expression> ] }
```

**example**

```jsx
db.files.find({
  File_Status: {
    $not: {
      $eq: "Processed",
    },
  },
});

db.files.aggregate([
  {
    $match: {
      File_Status: {
        $not: {
          $eq: "Processed",
        },
      },
    },
  },
]);
```

### $objectToArray

### $or

Evaluates one or more expressions and returns `true` if any of the expressions are `true`. Otherwise, `$or` return `false`.

**syntax**

```js
{ $or: [ <expression1>, <expression2>, ... ] }
```

**example**

```js
db.files.find({
  $or: [
    {
      File_Status: "Queued",
    },
    {
      IsActive: true,
    },
  ],
});

db.files.aggregate([
  {
    $match: {
      $or: [
        {
          File_Status: "Queued",
        },
        {
          IsActive: true,
        },
      ],
    },
  },
]);
```

### $percentile

### $pow

### $pow

### $push

### $radiansToDegrees

### $rand

### $range

### $rank

### $reduce

### $regexFind

### $regexFindAll

### $regexMatch

### $replaceOne

### $replaceAll

### $reverseArray

### $round

### $rtrim

### $sampleRate

### $second

### $setDifference

### $setEquals

### $setField

### $setIntersection

### $setIsSubset

### $setUnion

### $shift

### $size

Counts and returns the total number of items in an array.

**syntax**

```jsx
{ $size: <expression> }
```

**example**

```jsx
db.claims_837.find({
  ServiceLine: {
    $size: 2,
  },
});

db.claims_837.aggregate([
  {
    $project: {
      NoServiceLine: {
        $size: "$ServiceLine",
      },
    },
  },
]);
```

### $sin

### $sinh

### $slice

### $sortArray

### $split

### $sqrt

### $stdDevPop

### $stdDevSamp

### $strcasecmp

### $strLenBytes

### $strLenCP

### $substr

### $substrBytes

### $substrCP

### $subtract

### $sum

### $switch

### $tan

### $tanh

### $stdDevSamp

### $toBool

### $toDate

### $toDecimal

### $toDouble

### $toHashedIndexKey

### $toInt

### $toLong

### $toObjectId

### $top

### $topN

### $toString

### $toLower

### $toUpper

### $toUUID

### $tsIncrement

### $tsSecond

### $trim

### $trunc

### $type

### $unsetField

### $week

### $year

### $zip
