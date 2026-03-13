  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1363, in solve_lookup_type
    _, field, _, lookup_parts = self.names_to_path(lookup_splitted, self.get_meta())
                                ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1842, in names_to_path
    raise FieldError(
    ...<2 lines>...
    )
django.core.exceptions.FieldError: Cannot resolve keyword 'ttle' into field. Choices are: author, author_id, body, created, id, publish, slug, status, title, updated
>>> Post.objects.filter(title='macbook')
<QuerySet []>
>>> Post.objects.filter(title='Macbook')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(title='One more post')
<QuerySet [<Post: One more post>]>
>>> 
>>> Post.objects.filter(title='One more ')
<QuerySet []>
>>> Post.objects.filter(title__iexact='One more post')
<QuerySet [<Post: One more post>]>
>>> Post.objects.filter(title__iexact='macbook')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(title__contains='One more ')
<QuerySet [<Post: One more post>]>
>>> Post.objects.filter(title__contains='oo')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(title__contains='po')
<QuerySet [<Post: POSTAN>, <Post: One more post>]>
>>> Post.objects.filter(id__in=[1,3])
<QuerySet [<Post: New Title>, <Post: Macbook>]>
>>> Post.objects.filter(id__lte=3)
<QuerySet [<Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(id__gte=3)
<QuerySet [<Post: POSTAN>, <Post: new title1>, <Post: fdfdf>, <Post: One more post>, <Post: New Title>]>
>>> Post.objects.filter(title__iendswith='an')
<QuerySet [<Post: POSTAN>, <Post: Aryan>]>
>>> Post.objects.filter(publish__month=1)
<QuerySet []>
>>> Post.objects.filter(publish__year=2026)
<QuerySet [<Post: POSTAN>, <Post: new title1>, <Post: fdfdf>, <Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> pt=Post.objects.filter(publish__year=2026)
>>> pt
<QuerySet [<Post: POSTAN>, <Post: new title1>, <Post: fdfdf>, <Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> pt=Post.objects.filter(publish__day=1)
>>> pt
<QuerySet []>
>>> Post.objects.filter(publish__month=03)
  File "<console>", line 1
    Post.objects.filter(publish__month=03)
                                       ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> Post.objects.filter(publish__month=3)
<QuerySet [<Post: POSTAN>, <Post: new title1>]>
>>> Post.objects.filter(publish__month=2)
<QuerySet [<Post: fdfdf>, <Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(publish__date__gt=date(2024,1,1))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'date' is not defined
>>> import date
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ModuleNotFoundError: No module named 'date'
>>> from date import date
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ModuleNotFoundError: No module named 'date'
>>> from datetime import date
>>> Post.objects.filter(publish__date__gt=date(2024,1,1))
<QuerySet [<Post: POSTAN>, <Post: new title1>, <Post: fdfdf>, <Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> user, created=User.objects.get_or_create(username='user10')
>>> Post.objects.filter(author__username__startswith='Ar')
<QuerySet [<Post: POSTAN>, <Post: new title1>, <Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(publish__year=2024).filter(author__username='Aryan')
<QuerySet []>
>>> Post.objects.filter(publish__year=2026).filter(author__username='Aryan')
<QuerySet [<Post: POSTAN>, <Post: new title1>, <Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.order_by('author','title')
<QuerySet [<Post: Aryan>, <Post: Macbook>, <Post: New Title>, <Post: One more post>, <Post: POSTAN>, <Post: new title1>, <Post: fdfdf>]>
>>> Post.objects.order_by('author','?title')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/query.py", line 1772, in order_by
    obj.query.add_ordering(*field_names)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 2343, in add_ordering
    self.names_to_path(item.split(LOOKUP_SEP), self.model._meta)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1842, in names_to_path
    raise FieldError(
    ...<2 lines>...
    )
django.core.exceptions.FieldError: Cannot resolve keyword '?title' into field. Choices are: author, author_id, body, created, id, publish, slug, status, title, updated
>>> Post.objects.order_by('author','title')
<QuerySet [<Post: Aryan>, <Post: Macbook>, <Post: New Title>, <Post: One more post>, <Post: POSTAN>, <Post: new title1>, <Post: fdfdf>]>
>>> Post.objects.all()[:5]
<QuerySet [<Post: POSTAN>, <Post: new title1>, <Post: fdfdf>, <Post: One more post>, <Post: New Title>]>
>>> Post.objects.filter(id__gt=3)
<QuerySet [<Post: POSTAN>, <Post: new title1>, <Post: fdfdf>, <Post: One more post>]>
>>> Post.objects.filter(id__gt=3).exists()
True
>>> post=Post.objects.filter(id=5)
>>> post.delete()
(1, {'stdBlog.Post': 1})
>>> 
 *  History restored 

aryanbharti@Aryans-MacBook-Air L07_DB_Admin % 