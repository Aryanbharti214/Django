aryanbharti@Aryans-MacBook-Air L07_DB_Admin %  source /Users/aryanbharti/Desktop/Django/venv/bin/activate
(Venv) aryanbharti@Aryans-MacBook-Air L07_DB_Admin % python manage.py shell
13 objects imported automatically (use -v 2 for details).

Cmd click to launch VS Code Native REPL
Python 3.13.9 (v3.13.9:8183fa5e3f7, Oct 14 2025, 10:27:13) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> >>> from do.contrib.auth.models inport user
  File "<console>", line 1
    from django.contrib.auth.models inport user
                                    ^^^^^^
SyntaxError: invalid syntax
>>> from django.contrib.auth.models import user
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ImportError: cannot import name 'user' from 'django.contrib.auth.models' (/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/contrib/auth/models.py)
>>> from django.contrib.auth.models import User
>>> from stdBlog.models import Post
>>> user=User.objects.get(username='admin')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/query.py", line 639, in get
    raise self.model.DoesNotExist(
        "%s matching query does not exist." % self.model._meta.object_name
    )
django.contrib.auth.models.User.DoesNotExist: User matching query does not exist.
>>> user=User.objects.get(username='Aryan')
>>> post=Post(title='Aryanxyz',slug='anPOST',body='Post Body',author=user)
>>> post.save()
>>> Post.objects.create(title='One more post',slug='oneMorePost',body='Post body',author=user)
<Post: One more post>
>>> user, created=User.objects.get_or_create(username='user2')
>>> user
<User: user2>
>>> created
True
>>> post.title='New Title'
>>> post.save()
>>> post.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/manager.py", line 186, in __get__
    raise AttributeError(
        "Manager isn't accessible via %s instances" % cls.__name__
    )
AttributeError: Manager isn't accessible via Post instances
>>> Post.objects.all()
<QuerySet [<Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(title='Macbook')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(id__exact=1)
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(id__exact=5)
<QuerySet []>
>>> Post.objects.filter(id__exact='post4')
Traceback (most recent call last):
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/fields/__init__.py", line 2128, in get_prep_value
    return int(value)
ValueError: invalid literal for int() with base 10: 'post4'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/query.py", line 1542, in filter
    return self._filter_or_exclude(False, args, kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/query.py", line 1560, in _filter_or_exclude
    clone._filter_or_exclude_inplace(negate, args, kwargs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/query.py", line 1570, in _filter_or_exclude_inplace
    self._query.add_q(Q(*args, **kwargs))
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1676, in add_q
    clause, _ = self._add_q(q_object, can_reuse)
                ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1708, in _add_q
    child_clause, needed_inner = self.build_filter(
                                 ~~~~~~~~~~~~~~~~~^
        child,
        ^^^^^^
    ...<7 lines>...
        update_join_types=update_join_types,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1618, in build_filter
    condition = self.build_lookup(lookups, col, value)
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1445, in build_lookup
    lookup = lookup_class(lhs, rhs)
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/lookups.py", line 35, in __init__
    self.rhs = self.get_prep_lookup()
               ~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/lookups.py", line 391, in get_prep_lookup
    return super().get_prep_lookup()
           ~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/lookups.py", line 93, in get_prep_lookup
    return self.lhs.output_field.get_prep_value(self.rhs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/fields/__init__.py", line 2130, in get_prep_value
    raise e.__class__(
        "Field '%s' expected a number but got %r." % (self.name, value),
    ) from e
ValueError: Field 'id' expected a number but got 'post4'.
>>> Post.objects.filter(title__exact='post4')
<QuerySet []>
>>> Post.objects.filter(title__exact='Post4')
<QuerySet []>
>>> Post.objects.filter(title__exact='Macbook')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(title__exact='macbook')
<QuerySet []>
>>> Post.objects.filter(title__iexact='macbook')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(title__contains='macbook')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(id__in=[1,3)
  File "<console>", line 1
    Post.objects.filter(id__in=[1,3)
                                   ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> Post.objects.filter(id__in=[1,3])
<QuerySet [<Post: New Title>, <Post: Macbook>]>
>>> Post.objects.filter(id__gt=3)
<QuerySet [<Post: One more post>]>
>>> Post.objects.filter(id__lt=3)
<QuerySet [<Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(id__lte=3)
<QuerySet [<Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(title__startswith='macbook')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(title__istartswith='macbook')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(title__endswith='macbook')
<QuerySet [<Post: Macbook>]>
>>> Post.objects.filter(title__iendswith='macbook')
<QuerySet [<Post: Macbook>]>
>>> from datetime import date
>>> Post.objects.filter(publish__date=date(2026,2,23))
<QuerySet []>
>>> Post.objects.filter(publish__date=date(2026,2,27))
<QuerySet [<Post: One more post>, <Post: New Title>]>
>>> Post.objects.filter(publish__year=date(2026,2,27))
Traceback (most recent call last):
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/fields/__init__.py", line 2128, in get_prep_value
    return int(value)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'datetime.date'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/query.py", line 1542, in filter
    return self._filter_or_exclude(False, args, kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/query.py", line 1560, in _filter_or_exclude
    clone._filter_or_exclude_inplace(negate, args, kwargs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/query.py", line 1570, in _filter_or_exclude_inplace
    self._query.add_q(Q(*args, **kwargs))
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1676, in add_q
    clause, _ = self._add_q(q_object, can_reuse)
                ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1708, in _add_q
    child_clause, needed_inner = self.build_filter(
                                 ~~~~~~~~~~~~~~~~~^
        child,
        ^^^^^^
    ...<7 lines>...
        update_join_types=update_join_types,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1618, in build_filter
    condition = self.build_lookup(lookups, col, value)
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/sql/query.py", line 1445, in build_lookup
    lookup = lookup_class(lhs, rhs)
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/lookups.py", line 35, in __init__
    self.rhs = self.get_prep_lookup()
               ~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/lookups.py", line 391, in get_prep_lookup
    return super().get_prep_lookup()
           ~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/lookups.py", line 93, in get_prep_lookup
    return self.lhs.output_field.get_prep_value(self.rhs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/Users/aryanbharti/Desktop/Django/Venv/lib/python3.13/site-packages/django/db/models/fields/__init__.py", line 2130, in get_prep_value
    raise e.__class__(
        "Field '%s' expected a number but got %r." % (self.name, value),
    ) from e
TypeError: Field 'None' expected a number but got datetime.date(2026, 2, 27).
>>> Post.objects.filter(publish__year=date(2026))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: function missing required argument 'month' (pos 2)
>>> Post.objects.filter(publish__year=2026)
<QuerySet [<Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(publish__month=04)
  File "<console>", line 1
    Post.objects.filter(publish__month=04)
                                       ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> Post.objects.filter(publish__month=4)
<QuerySet []>
>>> Post.objects.filter(publish__month=2)
<QuerySet [<Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(publish__month=27)
<QuerySet []>
>>> Post.objects.filter(publish__day=27)
<QuerySet [<Post: One more post>, <Post: New Title>]>
>>> Post.objects.filter(publish__date__lt=date(2026,2,27))
<QuerySet [<Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(publish__date__lte=date(2026,2,27))
<QuerySet [<Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> Post.objects.filter(author__username='Aryan',title__startswith="Macbook")
<QuerySet [<Post: Macbook>]>
>>> from django.db.models import Q
>>> a=Q(author__username="Aryan")
>>> b=Q(id__gt=3)
>>> Post.objects.filter(a|b)
<QuerySet [<Post: One more post>, <Post: New Title>, <Post: Macbook>, <Post: Aryan>]>
>>> 