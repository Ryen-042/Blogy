# Flask Blog.

A simple blog web app made using Flask, HTML, CSS, and Bootstrap.


## Getting Started
This project should be compatible with Python 3.7 and above. It is highly recommended to use a virtual environment to run this project.

To get started with this template:
1. Download source files or clone the repository:

```bash
git clone https://github.com/Ryen-042/Blogy.git
```

2. Install the dependencies with `pip install -r requirements.txt` or `make install-reqs`:

3. Run the app with `python src/run.py` or `make run`:

4. Navigate to `http://localhost:5000` in your browser to view the app.

## Project Structure

```bash
E:.
|   blog.py
|   configs.py
|   db_init.py
|   run.py
|   __init__.py
|
+---errors
|   |   handlers.py
|   |   __init__.py
|
+---instance
|   |   site.db
|
+---main
|   |   site_routes.py
|   |   __init__.py
|
+---posts
|   |   forms.py
|   |   models.py
|   |   routes.py
|   |   __init__.py
|
+---static
|   |   main.css
|   |
|   +---icons
|   |
|   \---profile_photos
|
+---templates
|   |   home.html
|   |
|   +---errors
|   |       403.html
|   |       404.html
|   |       500.html
|   |
|   \---layouts
|           base.html
|
\---users
    |   forms.py
    |   models.py
    |   routes.py
    |   utils.py
    |   __init__.py
```

The `src` directory contains the project source code. It includes the main entry point file (`run.py`) and subdirectories for different components (blueprints). Each blueprint is a self-contained directory containing the files necessary for that blueprint. The available blueprints are: `main`, `errors`, `users`, and `posts`.

The `src/templates` directory contains Jinja2 templates for each blueprint. Flask will look for templates in this directory when rendering views. The `base.html` file contains the base template that is extended by all other templates.

The `src/static` directory contains all static files, such as stylesheets and images.

---

## Makefile Commands

The Makefile contains several useful commands for initializing the database and runing and linting the project. These commands are: `install-reqs`, `run`, `db-init`, `db-clean`, `activate`, `ruff`, `flake8`, and `lint`.