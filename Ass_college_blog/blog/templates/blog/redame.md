{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Blog List</title>
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">

</head>
<body>

<div class="container">

<h1>Title List</h1>


    {% for s in title %}
    <h3><u>{{s.title}}</u></h3>
    <p>{{s.content}}</p>
    {% endfor %}


</div>

</body>
</html>









{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Blog List</title>
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">

</head>
<body>

<div class="container">

<h1>Blog List</h1>

{% if blog %}

    {% for s in blog %}
        <div class="blog-card">

            <div class="blog-title">
                {{ s.title }}
            </div>

            <div class="blog-meta">
                <strong>Slug:</strong> {{ s.slug }} <br>
                <strong>Published:</strong> {{ s.publish }} <br>
                <strong>Created:</strong> {{ s.created }} <br>
                <strong>Updated:</strong> {{ s.updated }}
            </div>

            <div class="blog-body">
                {{ s.body }}
            </div>

        </div>
    {% endfor %}

{% else %}
    <p>No blog posts available.</p>
{% endif %}

</div>

</body>
</html>