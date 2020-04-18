articles
This a simple blog with class based Generic views

All auth
login, signup, logout system with all auth

userprofiles
An app to make a profile for the user

Requirements
Crispy forms
all auth
Pillow 7.0.0

if you wnt to add specific styles to a specific template you can do it like This
Notice that the directory mentioned down here is in the app static folder (appname/static/appname/css/style.css)

{% extends "base.html" %}
{% load static %}

{% block css %}
<link href="{% static 'css/user_list.css' %}" rel="stylesheet">
{% endblock css %}

{% block content %}

<div class="page-header">
  <h1>Contacts</h1>
</div>
....
{% endblock content %}

in the base we type 
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
		integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
	<link rel="stylesheet" href="{% static 'css/landing.css' %}">
	{% block css %}

	{% endblock css %}
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
	<script src="https://cdn.jsdelivr.net/npm/sweetalert2@9"></script>
	<title>My Blog</title>
</head>