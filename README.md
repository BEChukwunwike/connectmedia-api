# Team Awesome Webstack_Portfolio_Project

Using the repository:

```bash
git clone https://github.com/BEChukwunwike/connectmedia-api.git
```

Install the requirements programs by:

```bash
pip install -r requirements.txt
```

Create a Clourdinary and Postgres accounts for storing media and database as to use the variables specified in the `settings.py` file.

Create a `.env` or `env.py` file in the project root directory to store the specified variables

To run the program, `cd` to `connectmedia` directory and run

```bash
python manage.py runserver
```

Available routes include: `/comments`, `/followers`, `/likes`, `/posts`, `/profiles`
