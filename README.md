# Team Awesome Webstack_Portfolio_Project - ConnectMedia-API

<img src="https://i.imgur.com/MvgPiT3.jpeg" alt="Logo" width="25%" style="display: block; margin: auto;">

## Introduction

Welcome to the ConnectMedia-API, part of the Team Awesome Webstack_Portfolio_Project. This API serves as the backend for managing media-related functionalities such as comments, followers, likes, posts, and user profiles.

## Getting Started

To use this repository, follow the steps below:

Clone the repository:

```bash
git clone https://github.com/BEChukwunwike/connectmedia-api.git
```

Setup a virtual environment by using: `python -m venv your_virtual_env_name`

Install the requirements programs by:

```bash
pip install -r requirements.txt
```

Create a Cloudinary and Postgres accounts for storing media and database as to use the variables specified in the `settings.py` file.

Create a `.env` or `env.py` file in the project root directory to store the specified variables

Create Django superuser:

```bash
python manage.py createsuperuser
```

and follow the screen instructions

To run the program, `cd` to `connectmedia` directory and run

`python manage.py migrate` to migrate the database after then

```bash
python manage.py runserver
```

## Available Routes
* `/admin` : Django admin panel.
* `/comments` : Endpoint for managing comments.
* `/followers` : Endpoint for managing followers.
* `/likes` : Endpoint for managing likes.
* `/posts` : Endpoint for managing posts.
* `/profiles` : Endpoint for managing user profiles.

All with the ability to perform CRUD functionalties through the backend and also the frontend when created.
Feel free to explore and interact with these routes as needed for your application.
Thank you for using ConnectMedia-API! If you have any questions or issues, please don't hesitate to reach out.
