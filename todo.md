## To Do ("The Horror. The Horror")
- Complete models and ensure that the relationships between tables are functioning correctly
- Split into modules to make understanding the files easier
- Include a run.py script up front to launch the dev server
- Alter the fields{} objects to correspond
- Check and standardise the length of strings allowed in the Models
- Investigate and setup a consistent system of database migrations
- Admin interface
    - Bulk import
    - Publish and unpublish
- expand views
- Investigate and setup a system for fileuploads
- Add tests (also place bet that this is never happens ~sigh~)
- Limit the number of subjects that are returned in one go and add pagination

- Note: if the backref to Units on the subject model returns a list (i.e. it gives a `['engl1234', 'abcd4567', 'asdf6789']` sort of thing, then we might have to attempt to use the fields.list('units') method to render them. Who knows. Maybe.
