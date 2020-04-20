

## Run it locally

In order to run the projects locally, you need to have Node, npm and Python installed on your machine.

### Running the Django project

Make sure you have python3 installed in your machine.

First, create the python virtual environment :

```bash
python3 -m venv myvenv
```

Then, activate it:

```bash
cd myvenv/Scripts/activate.bat
```

Just then you can clone the project from GitHub. So, `cd` into the venv and run:

```bash
git clone https://github.com/sundaramseth/algofocus.git
```

Now, add the needed Djano dependencies:

```bash
pip install django djangorestframework django-cors-headers
```

Great, just need to run the project now. For this, `cd` into the 'algofocus' folder and run:

```bash
python manage.py runserver
```

That's it. Access the address http://localhost:8000/api/students/ and check for the API up and running.

### Running the React project

First, `cd` the students-fe directory and run:

```bash
npm install
```

Then, you just need to run the app via:

```bash
npm start
```
