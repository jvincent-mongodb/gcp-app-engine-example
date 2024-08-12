index_view = """
<!DOCTYPE html>
<html>
   <head>
      <title>GCP App Engine + MongoDB Atlas Demo App</title>
   </head>
   <body style="background-color:white;">
        <h1 style="color: #000000; margin: 15px;">GCP App Engine + MongoDB Atlas Example App</h1>
        <div style="background-color: #589636; margin: 15px; border-radius: 5px; padding: 15px; width: 400px">
        <form action="/get-doc" method="get">
            <h2> Get a document from the Movie Reviews collection in your Atlas cluster</h2>
            <p><input type=submit value="Get document">   
        </form>
        </div>
    </body>
</html>
"""