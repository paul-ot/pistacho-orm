# Pistacho ORM

## Attention, Pistacho ORM is currently under construction, be patient and you will be rewarded `:)` 

# Pistacho ORM basics

## 1 What is Pistacho ORM?
This project is a Python-based Object-Relational Mapping (ORM) library designed to abstract database interactions, inspired by the ActiveRecord pattern from Ruby on Rails. It aims to simplify database operations by allowing developers to interact with the database using Python objects and methods instead of raw SQL queries.
### 1.1 The Pistacho ORM Pattern
In Pistacho ORM, objects carry both persistent data and behavior which operates on that data. Pistacho ORM takes the opinion that ensuring data access logic as part of the object will educate users of that object on how to write to and read from the database.
### 1.2 Object Relational Mapping
Object Relational Mapping, commonly referred to as its abbreviation ORM, is a technique that connects the rich objects of an application to tables in a relational database management system. Using ORM, the properties and relationships of the objects in an application can be easily stored and retrieved from a database without writing SQL statements directly and with less overall database access code.
### 1.3 Pistacho as an ORM framework
Pistacho ORM gives us several mechanisms, the most important being the ability to:

* Represent models and their data.
* Represent associations between these models.
* Represent inheritance hierarchies through related models.
* Validate models before they get persisted to the database.
* Perform database operations in an object-oriented fashion.

## 2 Convention over Configuration in Pistacho ORM
When writing applications using other programming languages or frameworks, it may be necessary to write a lot of configuration code. This is particularly true for ORM frameworks in general. However, if you follow the conventions adopted by Rails, you'll need to write very little configuration (in some cases no configuration at all) when creating Pistacho models. The idea is that if you configure your applications in the very same way most of the time then this should be the default way. Thus, explicit configuration would be needed only in those cases where you can't follow the standard convention.

### 2.1 Naming Conventions
By default, Pistacho ORM uses some naming conventions to find out how the mapping between models and database tables should be created. Rails will pluralize your class names to find the respective database table. So, for a class Book, you should have a database table called books. The Rails pluralization mechanisms are very powerful, being capable of pluralizing (and singularizing) both regular and irregular words. When using class names composed of two or more words, the model class name should follow the Ruby conventions, using the CamelCase form, while the table name must use the snake_case form. Examples:

* Model Class - Singular with the first letter of each word capitalized (e.g., `BookClub`).
* Database Table - Plural with underscores separating words (e.g., `book_clubs`).


| Model / Class |	Table / Schema
| ------------- |:----------------:|
| Article       | articles
| LineItem	    | line_items
| Deer	        | deers
| Mouse	        | mice
| Person        | people

### 2.2 Schema Conventions
Pistacho ORM uses naming conventions for the columns in database tables, depending on the purpose of these columns.

* **Foreign keys** - These fields should be named following the pattern `singularized_table_name_id` (e.g., `item_id`, `order_id`). These are the fields that Pistacho ORM will look for when you create associations between your models.
* **Primary keys** - By default, Pistacho ORM will use an integer column named `id` as the table's primary key (`bigint` for PostgreSQL and MySQL, `integer` for SQLite).

## 3 Creating Pistacho ORM Models
When using Pistacho you have a `pistacho.Model` class, this will be the base class for all models in an app, and it's what turns a regular python class into a Pistacho model.

To create Pistacho ORM models, subclass the `pistacho.Model` class and you're good to go:
```python
class Product(Model):
    pass
```
This will create a `Product` model, mapped to a `products` table at the database. By doing this you'll also have the ability to map the columns of each row in that table with the attributes of the instances of your model. Suppose that the `products` table was created using an SQL (or one of its extensions) statement like:

```sql
CREATE TABLE products (
  id int(11) NOT NULL auto_increment,
  name varchar(255),
  PRIMARY KEY  (id)
);
```

The schema above declares a table with two columns: `id` and `name`. Each row of this table represents a certain product with these two parameters. Thus, you would be able to write code like the following:

```python
p = Product()
p.name = "Some Book"
print(p.name) # "Some Book"
```

## 4 Overriding the Naming Conventions
What if you need to follow a different naming convention or need to use your  application with a legacy database? No problem, you can easily override the default conventions.

Since you models inherits from `pistacho.Model`, your application's models will have a number of helpful methods available to them. For example, you can use the `table_name=` method to customize the table name that should be used:
```python
# Under development...
```

It's also possible to override the column that should be used as the table's primary key using the `primary_key=` method:

```python
# Under construction as well...
```

## 5 CRUD: Reading and Writing Data
CRUD is an acronym for the four verbs we use to operate on data: **C**reate, **R**ead, **U**pdate and **D**elete. Pistacho ORM automatically creates methods to allow an application to read and manipulate data stored within its tables.

### 5.1 Create
Pistacho objects can be created from a hash, a block, or have their attributes manually set after creation. The `new` method will return a new object while `create` will return the object and save it to the database.

For example, given a model `User` with attributes of `name` and `occupation`, the `create` method call will create and save a new record into the database:

```python
user = User.create(name="David", occupation="Code Artist")
```

Using the `new` method, an object can be instantiated without being saved:

```python
user = User()
user.name = "David"
user.occupation = "Code Artist"
```

A call to `user.save()` will commit the record to the database.

```python
user = User()
user.name = "David"
user.occupation = "Code Artist"
user.save()
```

### 5.2 Read
Pistacho ORM provides a rich API for accessing data within a database. Below are a few examples of different data access methods provided by Pistacho ORM.

```python
# return a collection with all users
users = User.all()
```


```python
# return the first user
user = User.first()
```

```python
# return the first user named David
david = User.find_by(name='David')

```

```python
# find all users named David who are Code Artists and sort by created_at in reverse chronological order
users = User.where(name='David', occupation='Code Artist').order(created_at='desc')
```
You can learn more about querying an Pistacho ORM model in the Pistacho ORM Query Interface guide. (soon)

### 5.3 Update
Once a Pistacho ORM object has been retrieved, its attributes can be modified and it can be saved to the database.

```python
user = User.find_by(name='David')
user.name = 'Dave'
user.save
```

A shorthand for this is to use a hash mapping attribute names to the desired value, like so:

```python
user = User.find_by(name='David')
user.update(name='Dave')
```

This is most useful when updating several attributes at once.

If you'd like to update several records in bulk you can update the database directly using `update_all`:

```python
User.update_all(max_login_attempts=3, must_change_password=true)
```

## 5.4 Delete
Likewise, once retrieved, an Pistacho ORM object can be destroyed, which removes it from the database.

```python
user = User.find_by(name='David')
user.delete()
```

If you'd like to delete several records in bulk, you may use `destroy_by` or `destroy_all` method:


```python
# find and delete all users named David
User.destroy_by(name='David')

# delete all users
User.destroy_all
```

## 6 Validations
Validations are not in this scope.

## 7 Callbacks
No callbacks at this time.

## 8 Migrations
There are no migrations.

### 9 Associations
I'm still thinking about how to implement them...

