<html>
<body>
<h2>Add New Student and Course</h2>
<hr/>
<form action="/add" method="post">
  <p>Student Name: <input name="student_name" required/></p>
  <p>Course Name: <input name="course_name" required/></p>
  <p>Department: <input name="department" required/></p>
  <p>Credits: <input name="credits" type="number" required/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
<a href="/">Back to List</a>
<hr/>
</body>
</html>
