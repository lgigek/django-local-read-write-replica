# django-local-read-write-replica
This repo was created to simulate a Django project using a write/read replica database (PSQL).

## How to run
As you can see on the project root, this project uses docker-compose, so simply run `docker-compose up app` and that's 
it! 

## Some evidences
The scenario that will be explained uses the route `POST /api/v1/message` ([this](https://github.com/lgigek/django-local-read-write-replica/blob/master/django_local_read_write_replica/apps/my_app/drf/views.py#L14) is the view). 

I also used PyCharm for debug purposes, with an remote interpreter of `app` (from [docker-compose.yml](https://github.com/lgigek/django-local-read-write-replica/blob/master/docker-compose.yml#L32))

### Without DB Router
This scenario is before applying the DB Router (to be more specifically, the test was made on [this commit](https://github.com/lgigek/django-local-read-write-replica/commit/d33e522398396c2b00db27e35ec3ef9a980160a4)).

As we can see, using a single database replica for read/write, even before the transaction being commited, the data is available to be retrieved:

The object was created on line 19 and, just after that, it's possible to perform a `.get` and retrieve it.

![without db router](docs/evidences/without%20db%20router.png)

### After using DB Router
As we can see, using a database replica specific for read and another one for write, the data will only be created after the transaction commit is finished.

The first image simulates the same scenario that was performed before: inside the same transaction, right after performing the `.create`, on line 19. 
But, since tthe transaction wasn't commited yet, thus the new data isn't on read replica, it raise a `Message.DoesNotExist`, which is exactly the scenario that we're looking for! 

![with db router - inside transaction](docs/evidences/with%20db%20router%20-%20inside%20tranasction.png)

And, right after the transaction is commited, the data was found on read replica.
![with db router - after transaction](docs/evidences/with%20db%20router%20-%20after%20transaction.png)

## Considerations
There are some TODOs, such as:
- Create an integration test, to make it easier to debug;
- Some docstrings to help understand the code;

But the initial purpose of the project was achieved, so other people can benefit from it. 

## References
- [docker-postgres-replication](https://github.com/DanielDent/docker-postgres-replication)