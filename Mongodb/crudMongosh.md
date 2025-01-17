# CRUD Operations

## Insert

### insertOne()

to insert single document, use the `insertOne()` method.

```jsx
db.post.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: Date(),
});
```

### insertMany()

to insert multiple document at once, use the `insertMany()` method.

```jsx
db.posts.insertMany([
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: Date(),
  },
  {
    title: "Post Title 3",
    body: "Body of post.",
    category: "Technology",
    likes: 3,
    tags: ["news", "events"],
    date: Date(),
  },
  {
    title: "Post Title 4",
    body: "Body of post.",
    category: "Event",
    likes: 4,
    tags: ["news", "events"],
    date: Date(),
  },
]);
```

## Find Data

### find()

- to select data from a collection mongodb, we can use the `find()` method.
- this method accept query object. If left empty, all document will be returned.

- **definition**

```jsx
db.collection.find( <query>, <projection>, <options> )
```

| parameter  | type     | description                                                                                                                                                                                                                                                                                    |
| ---------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| query      | document | Optional. Specifies selection filter using [query operators](https://www.mongodb.com/docs/manual/reference/operator/query/#std-label-query-projection-operators-top). To return all documents in a collection, omit this parameter or pass an empty document (`{}`).                           |
| projection | document | Optional. Specifies the fields to return in the documents that match the query filter. To return all fields in the matching documents, omit this parameter. For details, see [Projection.](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#std-label-find-projection) |
| options    | document | Optional. Specifies additional options for the query. These options modify query behavior and how results are returned. For details, see [Options.](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#std-label-find-options)                                           |

- get all the document from collections post

```jsx
db.post.find();
```

- To query, or filter, data we can include a query in our `find()` or `findOne()` methods.

```jsx
db.posts.find({ category: "News" });
```

- This parameter is an `object` that describes which fields to include in the results
- We use a `1` to include a field and `0` to exclude a field.

```jsx
db.posts.find({}, { title: 1, date: 1 });

db.posts.find({}, { _id: 0, title: 1, date: 1 });
```

- we can use different query methods like $gt, $lt etc..

```jsx
db.collection.find({ qty: { $gt: 4 } });
```

### findOne()

- To select only one document, we can use the `findOne()` method.
- This method accepts a query object. If left empty, it will return the first document it finds

```jsx
db.posts.findOne();
```

> [!NOTE]
>
> - we can use findOne() same as find() function.
> - there are many different query we can use which will be under different file.

### countDocuments()

Returns the count of documents that match the query.

```jsx
db.collection.countDocuments({ age: { $gt: 25 } });
```

## Update

### updateOne()

The `updateOne()` method will update the first document that is found matching the provided query.

```jsx
db.posts.updateOne({ title: "Post Title 1" }, { $set: { likes: 2 } });
```

### updateMany()

The `updateMany()` method will update all documents that match the provided query.

```jsx
db.posts.updateMany({}, { $inc: { likes: 1 } });
```

### replaceOne()

Replaces a document with a new document.

```jsx
db.collection.replaceOne({ name: "Alice" }, { name: "Alice", age: 26 });
```

## Delete

### deleteOne()

The `deleteOne()` method will delete the first document that matches the query provided.

```jsx
db.posts.deleteOne({ title: "Post Title 5" });
```

### deleteMany()

The `deleteMany()` method will delete all documents that match the query provided.

```jsx
db.posts.deleteMany({ category: "Technology" });
```

## Addition Userfull function

### findOneAndUpdate():

Finds a document and updates it in one operation.

```jsx
db.collection.findOneAndUpdate(
  { name: "John" },
  { $set: { age: 40 } },
  { returnDocument: "after" }, // Optional: to return the updated document
);
```

### findOneAndDelete():

Finds a document and deletes it in one operation.

```jsx
db.collection.findOneAndDelete({ name: "Bob" });
```

### findAndModify():

Atomically modifies and return a document.

```jsx
db.collection.findAndModify({
  query: { name: "Alice" },
  update: { $set: { age: 30 } },
  new: true,
});
```

### drop():

Deletes a collection from the database.

```jsx
db.collection.drop();
```

### count():

Counts the number of documents that match a query.

```jsx
db.collection.countDocuments({ age: 26 });
```

### createIndex():

Creates an index on a collection to imporove query performance.

```jsx
db.collection.createIndex({ age: 1 });
```

### dropIndex():

Removes an index from a collection.

```jsx
db.collection.dropIndex({ age: 1 });
```

### renameCollection():

Rename a collection.

```jsx
db.collection.renameCollection("newCollection");
```

### distinct():

Returns distinct values for a specified field.

```jsx
db.collection.distinct("age");
```

### upsert():

Performs an update that inserts the document if no matching document is found.

```js
db.collection.updateOne(
  { name: "Bob" },
  { $set: { age: 28 } },
  { upsert: true },
);
```

### bulkWrite():

Performs multiple write operations ( insert, update, delete ) in a single request.

```jsx
db.collection.bulkWrite([
  { insertOne: { document: { name: "john", age: 22 } } },
  { updateOne: { filter: { name: "Alice" }, update: { $set: { age: 27 } } } },
  { deleteOne: { filter: { name: "Bob" } } },
]);
```

### mapReduce():

Applies a map-reduce operation to a collection for complex aggreation.

```js
db.collection.mapReduce(
  function () {
    emit(this.age, 1);
  },
  function (key, values) {
    return Array.sum(values);
  },
  { out: "age_count" },
);
```

### listCollections():

Retrieves a list of all collections in a database.

```jsx
db.getCollectionNames();
```

### isMaster()

Checks the status of a MongoDB instance ( master/slave, etc. )

```jsx
db.isMaster();
```

### ping():

Checks if the server is reachable.

```jsx
db.adminCommand({ ping: 1 });
```

### limit():

- Used to limit the fields of documents that you want to show.
- it used with find()

```jsx
db.collection.find().limit(10);
```
