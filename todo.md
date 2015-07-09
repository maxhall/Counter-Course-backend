## To Do ("The Horror. The Horror")
First Stage:
- Write a specific outline of the data the Frontend will need
- Use this to expand notes_fields, subjects_fields, units_fields to include the needed codes and links
- Investigate and setup a system for fileuploads
    - This will be a POST endpoint on the Notes resource which takes a name, author and file
    - parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')
- Include logic to only render an object if it is marked as published

Second stage:
- Add tests (also place bet that this is never happens ~sigh~)
- Limit the number of subjects that are returned in one go and add pagination
- Check and standardise the length of strings allowed in the Models
- Test the migration script
- Admin stuff
    - Bulk import
    - Publish and unpublish
    - Allow actual subject names etc to be viewed in the admin panel
    - Add login security
    - change the name of the login url
