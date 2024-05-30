# Week 1

Use the provided Django project template to implement a website for a restaurant.

The website should feature the following pages:

* a home page
* an about page
* a menu page
* a reservation page
* an order page (optional)

The home page and the about page are already provided.
The other pages are your task to build.

Create new Django apps for the menu, reservations and orders.

**Requirements:**

* Level 0 (minimum): All pages are available
* Level 1 (basic): The menu app is implemented
* Level 2 (intermediate): The reservations app is implemented
* Level 3 (advanced): The orders app is implemented


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


## Orders app

This add defines two models:

* `Order` for orders
* `OrderItem` for items of an order

Orders have a **name**, **date and time**, **address** and **delivery status**.

Order items have a **note** for special requests.
Each order item belongs to one order and references one menu item.

Orders are composed through the menu page and created on a checkout page.
They are displayed on a password protected page ordered by date and time and grouped by delivery status.
Orders can also be created, edited and deleted through the admin interface.


# Week 2

Use [Django REST Framework](https://www.django-rest-framework.org/) to create the following API endpoints:

    GET /api/menu 
    POST /api/reservations
    GET /api/reservations
    POST /api/orders
    GET /api/orders

**Requirements:**

* Level 0 (minimum): `GET /api/menu` is implemented
* Level 1 (basic): `GET /api/reservations` is implemented
* Level 2 (intermediate): `POST /api/reservations` is implemented
* Level 3 (advanced): `GET /api/orders` and `POST /api/orders` are implemented

Optional: Refactor the forms in such way that they access the API via JavaScript.

...