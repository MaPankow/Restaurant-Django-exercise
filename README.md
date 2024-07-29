# Restaurant Django Exercise

The task was to implement a website for a restaurant.

The website should feature the following pages:

* a home page
* an about page
* a menu page
* a reservation page

## Menu app

This app defines two models:

* `MenuCategory` for menu categories
* `MenuItem` for menu items

Menu categories have a **name**,
menu items have a **name**, **description** and **price**.
Each menu item belongs to one category.

Menu categories and items are displayed on the `menu` page.
They can only be created, edited and deleted through the admin interface.


## Reservations app

This app defines one model: `Reservation` for reservations.

Reservations have a **name**, **date and time** and **number of guests**.

Reservations are created through a form on a public page.
They are displayed on a password protected page ordered and grouped by day.
The restaurant has a capacity of 30 guests per evening.
Reservations can only be created as long as the capacity is greater than the sum of all reservation's guests.
Reservations can also be created, edited and deleted through the admin interface.

## API endpoints

This website has the following API endpoints:

    GET /api/menu 
    POST /api/reservations
    GET /api/reservations

The adminpage is accessable via [http://127.0.0.1:8000/admin/].




