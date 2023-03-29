*********
This step is only needed the first time you run the application in order
to create the SQLite3 database file (this will be stored in the app folder).
*********
  Still from the project directory, perform the following:
  - Start python interpreter by typing:     flask shell
  - At the python prompt type (>>>), run following Python statement in
    sequence:
          from app import db
          db.create_all()
          quit()    # this takes you back to the terminal prompt

 The create_all function creates the database schema defined in app/models.py.


**** To delete the data and recreate the table *****
Follow the Python statements above and type db.drop_all() before
db.create_all()
****

Now run the Flask application from the project top-level directory:

  flask run
