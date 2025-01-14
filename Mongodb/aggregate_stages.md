# Aggregation Stages

In the `db.collection.aggregate()` method and `db.aggregate()` method, pipeline stages appear in an array. In the Atlas UI, you can arrange pipeline stages using the **aggregation pipeline builder**.

**Syntax**

```js
db.collection.aggregate( [ { <stage> }, ... ] )
```

| Stage                        | Description                                                                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| $addFields                   | Adds new fields to documents. Similar to $project, reshapes each document by adding new fields while keeping existing fields from input docs. |
| $set                         | Alias for $addFields. Adds new fields to documents, reshaping them by adding new fields.                                                      |
| $bucket                      | Categorizes incoming documents into groups, called buckets, based on a specified expression and bucket boundaries.                            |
| $bucketAuto                  | Categorizes incoming documents into a specific number of groups, with automatic bucket boundary determination.                                |
| $changeStream                | Returns a Change Stream cursor for the collection, must be the first stage, can only occur once in the pipeline.                              |
| $changeStreamSplitLargeEvent | Splits large change stream events exceeding 16 MB into smaller fragments in a change stream pipeline.                                         |
| $collStats                   | Returns statistics regarding a collection or view.                                                                                            |
| $count                       | Returns a count of the number of documents at this stage of the aggregation pipeline.                                                         |
| $densify                     | Creates new documents in a sequence where certain values in a field are missing.                                                              |
| $documents                   | Returns literal documents from input expressions.                                                                                             |
| $facet                       | Processes multiple aggregation pipelines on the same set of input documents, enabling multi-faceted aggregations.                             |
| $fill                        | Populates null and missing field values within documents.                                                                                     |
| $geoNear                     | Returns documents ordered by proximity to a geospatial point, including distance and location identifier.                                     |
| $graphLookup                 | Performs a recursive search on a collection and adds an array field with the traversal results for each document.                             |
| $group                       | Groups input documents by an identifier expression and applies accumulator expressions, outputting one document per distinct group.           |
| $indexStats                  | Returns statistics about the use of each index in the collection.                                                                             |
| $limit                       | Passes the first n documents to the pipeline, outputting either one document or none based on the limit.                                      |
| $listSampledQueries          | Lists sampled queries for all or a specific collection.                                                                                       |
| $listSearchIndexes           | Returns information about existing Atlas Search indexes on a collection.                                                                      |
| $listSessions                | Lists sessions that have been active long enough to propagate to the system.sessions collection.                                              |
| $lookup                      | Performs a left outer join to another collection to filter in documents for processing.                                                       |
| $match                       | Filters documents in the pipeline based on a specified query, outputting matching or zero documents.                                          |
| $merge                       | Writes the aggregation results to a collection, with customizable operations like insert, merge, or replace.                                  |
| $out                         | Writes the aggregation results to a collection, must be the last stage in the pipeline.                                                       |
| $planCacheStats              | Returns plan cache information for a collection.                                                                                              |
| $project                     | Reshapes each document, by adding/removing fields or modifying them.                                                                          |
| $querySettings               | Returns query settings added with setQuerySettings.                                                                                           |
| $queryStats                  | Returns runtime statistics for recorded queries (unsupported, may change in future).                                                          |
| $redact                      | Reshapes documents by restricting content based on the document's information, used for field-level redaction.                                |
| $replaceRoot                 | Replaces a document with the specified embedded document, promoting it to the top level.                                                      |
| $replaceWith                 | Alias for $replaceRoot, replaces a document with the specified embedded document.                                                             |
| $sample                      | Randomly selects a specified number of documents from input.                                                                                  |
| $search                      | Performs a full-text search in an Atlas collection (only available on MongoDB Atlas).                                                         |
| $searchMeta                  | Returns metadata results for an Atlas Search query. (Only available on MongoDB Atlas)                                                         |
| $setWindowFields             | Groups documents into windows and applies operators to each window. (New in version 5.0)                                                      |
| $skip                        | Skips the first n documents, passing the remaining ones unmodified.                                                                           |
| $sort                        | Reorders the document stream by a specified sort key.                                                                                         |
| $sortByCount                 | Groups documents by the value of a specified expression and computes the count of documents in each group.                                    |
| $unionWith                   | Combines results from two collections into a single result set.                                                                               |
| $unset                       | Removes/excludes fields from documents. (Alias for $project)                                                                                  |
| $unwind                      | Deconstructs an array field, outputting one document per array element.                                                                       |
| $vectorSearch                | Performs an ANN or ENN search on a vector in a specified field of an Atlas collection. (Available for MongoDB Atlas v6.0.11 or higher)        |

**For the updates, the pipeline can consist of the following stages:**

- $addFields and its alias $set
- $project and its alias $unset
- $replaceRoot and its alias $replaceWith.

## Stages & Operations

### $project

Passes along the documents with the requested fields to the next stage in the pipeline. The specified fields can be existing fields from the input documents or newly computed fields.

**Syntax**

```js
{ $project: { <specification> } }
```

**Example**

```js
db.files.aggregate([
  {
    $project: {
      File_Name: 1,
      File_Format: 1,
      IsActive: 1,
      _id: 0,
    },
  },
]);

// nested
db.claims_837.aggregate([
  {
    $project: {
      Submission: {
        File_ID: 1,
        File_Name: 1,
      },
      _id: 0,
    },
  },
]);
```

## $addFields

- Adds new fields to documents. $addFields outputs documents that contain all existing fields from the input documents and newly added fields.
- The $addFields stage is equivalent to a $project stage that explicitly specifies all existing fields in the input documents and adds the new fields.

> [!NOTE]
> You can also use the `$set` stage, which is an alias for `$addFields.`

**Syntax**

```js
{ $addFields: { <newField>: <expression>, ... } }
```

**Example**

```js
db.scores.aggregate([
  {
    $addFields: {
      totalHomework: { $sum: "$homework" },
      totalQuiz: { $sum: "$quiz" },
    },
  },
  {
    $addFields: {
      totalScore: { $add: ["$totalHomework", "$totalQuiz", "$extraCredit"] },
    },
  },
]);

db.files.aggregate([
  {
    $addFields: {
      Client: {
        $concat: ["$Client_Key", "Bus_Type_Key", "Bus_SubType_Key"],
      },
    },
  },
]);
```

## $group

- The $group stage separates documents into groups according to a "group key". The output is one document for each unique group key.
- A group key is often a field, or group of fields. The group key can also be the result of an expression. Use the \_id field in the $group pipeline stage to set the group key.
- In the $group stage output, the \_id field is set to the group key for that document.

> [!NOTE]
>
> `$group` does not order output document.

**Syntax**

```js
{
 $group:
   {
     _id: <expression>, // Group key
     <field1>: { <accumulator1> : <expression1> },
     ...
   }
 }
```

**Example**

```js
db.files.aggregate([
  {
    $group: {
      _id: "$File_Name",
    },
  },
]);

db.files.aggregate([
  {
    $group: {
      _id: "$File_Name",
      total_Page: {
        $sum: "$File_Page",
      },
    },
  },
]);
```

## $limit

Limits the number of documents passed to the next stage in the pipeline.

**Syntax**

```js
{ $limit: <positive 64-bit integer> }
```

**Example**

```js
db.files.aggregate([{
    $limit: 3,
}, ]);

db.files.aggregate([
    {
        $group: {
            _id: "$File_Name",
            total_Page: {
                $sum: "$File_Page",
            },
        },
    },
    {
        $limit: 3,
    },
]
```

## $skip

- Skips over the specified number of documents that pass into the stage and passes the remaining documents to the next stage in the pipeline.
- The $skip stage has the following prototype form.

**Syntax**

```js
{ $skip: <positive 64-bit integer> }
```

**Example**

```js
db.files.aggregate([
  {
    $skip: 3,
  },
]);
```

## $sort

Sorts all input documents and returns them to the pipeline in sorted order.

**Syntax**

```js
{ $sort: { <field1>: <sort order>, <field2>: <sort order> ... } }
```

**Example**

```js
db.files.aggregate([
  {
    $sort: {
      File_Name: 1,
    },
  },
]);

db.files.aggregate([
  {
    $project: {
      File_Name: 1,
      File_Format: 1,
      IsActive: 1,
      _id: 0,
    },
  },
  {
    $sort: {
      File_Name: 1,
    },
  },
]);
```

## $unset

Removes/excludes fields from documents.

**Syntax**

```js
{ $unset: "<field>" }

{ $unset: [ "<field1>", "<field2>", ... ] }
```

**Example**

```js
db.files.aggregate([
  {
    $addFields: {
      Client: {
        $concat: ["$Client_Key", "$Bus_Type_Key", "$Bus_SubType_Key"],
      },
    },
  },
  {
    $unset: ["Client_Key", "Bus_Type_Key", "Bus_SubType_Key"],
  },
]);
```

## $unwind

Deconstructs an array field from the input documents to output a document for each element. Each output document is the input document with the value of the array field replaced by the element.

**Syntax**

```js
{ $unwind: <field path> }
```

**Example**

```js
db.claims_837.aggregate([
  {
    $unwind: "$ServiceLine",
  },
]);

db.claims_837.aggregate([
  {
    $unwind: {
      path: "$ServiceLine",
      preserveNullAndEmptyArrays: true,
    },
  },
]);
```

## $count

Passes a document to the next stage that contains a count of the number of documents input to the stage.

**Syntax**

```js
{ $count: <string> }
```

**Example**

```js
db.claims_837.aggregate([
  {
    $count: "totalCount",
  },
]);
```

## $match

Filters documents based on a specified query predicate. Matched documents are passed to the next pipeline stage.

**Syntax**

```js
{ $match: { <query predicate> } }
```

**Example**

```js
db.claims_837.aggregate([
  {
    $match: {
      $or: [
        {
          Status: "Submission",
        },
        {
          File_Type: "PROF",
        },
      ],
    },
  },
]);
```

## $out

- Takes the documents returned by the aggregation pipeline and writes them to a specified collection. You can specify the output database.
- The $out stage must be the last stage in the pipeline. The $out operator lets the aggregation framework return result sets of any size.

**Syntax**

```js
{
  $out: "<output-collection>";
} // Output collection is in the same database
```

**Example**

```js
db.edps_files.aggregate([
  {
    $out: "files",
  },
]);
```

## $lookup

- Performs a left outer join to a collection in the same database to filter in documents from the "joined" collection for processing. The $lookup stage adds a new array field to each input document. The new array field contains the matching documents from the "joined" collection. The $lookup stage passes these reshaped documents to the next stage.
- Starting in MongoDB 5.1, you can use $lookup with sharded collections.
- To combine elements from two different collections, use the $unionWith pipeline stage.

**Syntax**

```js
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       as: <output array field>
     }
}
```

**Example**

```js
db.orders.aggregate([
  {
    $lookup: {
      from: "inventory",
      localField: "item",
      foreignField: "sku",
      as: "inventory_docs",
    },
  },
]);
```

## $documents

Returns literal documents from input values.

**Syntax**

```js
{ $documents: <expression> }
```

**Example**

```js
db.aggregate([
  {
    $documents: [
      {
        x: 10,
      },
      {
        x: 2,
      },
      {
        x: 5,
      },
    ],
  },
  {
    $bucketAuto: {
      groupBy: "$x",
      buckets: 4,
    },
  },
]);
```
