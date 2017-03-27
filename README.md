# Django graphql sample


This is only for study only, at least, till now ...

I'm very interested in the graphql development, specially for some projects i already have.
So i decided to try a bit with Django and Graphene to see what happens.


To install, i recommend you to create a new virtualenv.
After that run `pip install -r requirements.txt`

There are some apps in the requirements that are not really a requirements, but some apps that gives me some shortcuts and facilities.

To run, you need first to create your db, with the migrate command.
After that, you can load some sample categories and products.

All products are in portuguese , so if you don't know what they are, do not be worried :P

To import them, with the database created, just run `python manage.py loaddata products.json`

With the server running, just open the browser: http://localhost:8000/graphql

We have to queries available.
all_categories and category.

The main goal here is that, you can query all categories, or fetch one category by its id.

So, in the query:

    query {
      allCategories{
        id
        name
        description
        products{
          id
          name
          description
          picture
          category
        }

Here, we are querying all categories, and the fields we are retrieving are:
***id, name, description and its products***
In the products, we want to retrieve the fields:
 ***id, name, description, picture and category***

Feel free to play with this query =D

To get a single category, you can start with this exemple:

    query {
      category(id: "1"){
        name
        description
        products{
          name
          picture
          description
        }
      }

Still didn't make the query to get the products, but i will put it ;)

Cheers! ^^

