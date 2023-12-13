<html>
<body>
<h2>Update Student and Course</h2>
<hr/>
<form action="/update" method="post">
  <input type="hidden" name="id" value="{{str(item['StudentID'])}}"/>
  <p>Student Name: <input name="student_name" value="{{item['StudentName']}}" required/></p>
  <p>Course Name: <input name="course_name" value="{{item['CourseName']}}" required/></p>
  <p>Department: <input name="department" value="{{item['Department']}}" required/></p>
  <p>Credits: <input name="credits" type="number" value="{{item['Credits']}}" required/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
<a href="/">Back to List</a>
<hr/>
</body>
</html>
