# Images compression based on a DCT based algorithm

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org).

```
$ git clone https://github.com/mferri17/dct-image-compression
$ cd dct-image-compression
$ pip install -r requirements.txt
$ python manage.py runserver 9999
```


If you prefer, you can also run the application using Heroku. First of all, you have to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
After `pip install`, you can run the application locally with this command for Linux users:
```
$ heroku local
```

Or this one for Windows users:
```
> heroku local web -f Procfile.windows
```

Your app should now be running on [localhost:9999](http://localhost:9999/).


## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
