Inefficient database querying is one of the most common performance pitfalls with Django. N+1 queries in particular can have a negative impact on your application's performance early on. They occur when you select records from an associated table using an individual query for each record rather than grabbing all records in a single query. Such inefficiencies are unfortunately quite easy to introduce with the Django ORM. That being said, they are something you can quickly uncover and prevent via automated testing.

This article looks at how to:

1. Test the number of queries executed by a request along with the duration of the queries
2. Prevent N+1 queries using the nplusone package

[Check out the article.](https://testdriven.io/blog/django-performance-testing/)
