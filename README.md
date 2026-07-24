# Personal-Library-API

## Models
```
Author
-------
id
name
country

Book
-------
id
title
pages
published_year
author_id (FK)
```
**Entities**: Author, Book

## Relationship
```
One Author
    |
    |------ Many Books
```
## Operations
```
Author
--------
Create
Read all
Read one
Delete
```
```
Book
-------
Create
Read all
Read one
Update
Delete
```
