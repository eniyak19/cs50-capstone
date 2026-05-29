# Recipe Manager

## Description
Recipe Manager is a Django web application that allows users to create, store, search, and view recipes. The goal of the project is to provide a simple platform where recipes can be organized and accessed easily.

The application allows users to add recipes through a form, upload recipe images, search recipes by title, and view detailed recipe pages containing descriptions, ingredients, and instructions. Bootstrap was used to improve the appearance and responsiveness of the website.

This project was built using Django because it provides powerful tools for handling databases, forms, and URL routing. One challenge during development was displaying recipe ingredients and instructions in a clear format. This was solved by processing recipe data in Django views and displaying it using Bootstrap components.

## Features
* Create recipes
* View all recipes
* View detailed recipe pages
* Responsive Bootstrap interface

## Technologies Used
* Python
* Django
* HTML
* CSS
* Bootstrap
* SQLite

## How to Run
1. Install project dependencies.
2. Run migrations:
python manage.py migrate
3. Start the server:
python manage.py runserver
4. Open http://127.0.0.1:8000/ in a browser.
