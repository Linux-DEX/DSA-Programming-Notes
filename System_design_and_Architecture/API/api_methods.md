# API Methods

## HTTPS RESTfull API Methods

- **GET**
The GET method is used to 'retrieve' a record or a collection of records from the server. The below code shows the implementation of the GET method in JavaScript.

```js
// returns the list of students
app.get('/students', function (req, res) {

    res.json(students);
});
```

- **POST**
The POST method sends data to create a 'new record' on the server. The below code shows the implementation of the POST method in JavaScript.

```js
// add student
app.post("/students", function (req, res) {
  var student = req.body;
  
  students.push(student);
  
  res.json({ message: "Record Added" });
});
```

- **PUT**
The PUT method sends data to update an 'existing record' on the server. The below code shows the implementation of the PUT method in JavaScript.

```js
app.put("/students/:id", function (req, res) {
  var id = req.params.id;
  
  var student = req.body;
  
  // updating user with the specific id
  for (var i = 0; i < students.length; i++) {
    if (students[i].id == id) {
      students[i] = student;
      break;
    }
  }
  
  res.json({ message: "Record Updated" });
});
```

- **PATCH**
Like the PUT method, PATCH is also used to send data to update an 'existing record' on the server. But the important difference between PUT and PATCH is that PATCH only applies partial modifications to the record instead of replacing the whole record. The below code shows the implementation of the PATCH method in JavaScript.

```js
app.patch("/students/:id", function (req, res) {
  var id = req.params.id;
  var student = req.body;
  
  for (var i = 0; i < students.length; i++) {
    if (students[i].id == id) {
    
    // replacing only specific properties 
      for (var key in student) {
        students[i][key] = student[key];
      }
      break;
      
    }
  }
  res.json({ message: "Record Updated using patch" });
});
```

- **DELETE**
The DELETE method is used to delete record(s) from the server. The below code shows the implementation of the DELETE method in JavaScript.

```js
app.delete("/students/:id", function (req, res) {
  var id = req.params.id;
  
  for (var i = 0; i < students.length; i++) {
    if (students[i].id == id) {
      students.splice(i, 1);
      break;
    }
  }
  
  res.json({ message: "Record Deleted" });
});
```
