import cgitb
cgitb.enable()

print("Content-type:text/html\n\n")

#Added HTML Structure with title and styling
print("""
<!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Intructors of the Yoga Club</title>
      <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
            color: #333;
            margin: 0;
            padding: 20px;
        }
      h1 {
        text-align: center;
        color:#008080;
      }
      table {
        width: 50%;
        margin: 0 auto;
        border-collapse: collapse;
        border: 2px solid #008080;
      
      }
      th, td{
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
      th{
        background-color: #008080;
        color: white;
      }
    </style>
</head>
<body>
      <h1> Instructors of the Yoga Club</h1>
      <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
        </tr>
""")

#!/usr/bin/python3

#debug mode on
import cgitb


#print html headers
print("Content-Type:text/html\n\n")

#connect to the DB
import pymysql
con = pymysql.connect(
	db='yoga', user='root', passwd='NewPassword', host='localhost')

#fetch and print contents
try:
	with con.cursor() as cur:
			cur.execute("Select * from instructors")

			rows=cur.fetchall()
			for row in rows:
				print(f"""
		  		<tr>
		  			<td>{row[0]}</td>
					<td>{row[1]}</td>
				</tr>
				""")
finally:
		con.close()

