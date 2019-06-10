# Images compression with a DCT2 based algorithm

Project 2 for the *Methods of Scientific Computation* course for the MSc in Computer Science at University of Milano-Bicocca.

## Brief
As described in `docs/MCS_project-description.pdf`, this project is divided into two parts:
- The first one aims to **implement the Discrete Cosine Transform Type-II, and compare its time complexity against a library's implementation** (which supposingly uses a Fast Fourier Transform behind the scenes). The comparison will be held against `scipy`'s implementation. This part of the project and its README can be found into `_PART1` folder of this repository.
- The second one is a **Web App that implements a simple JPEG-derived algorithm to demonstrate how DCT2 is used in image compressions**. The application has been deployed and it is available here: https://dct-image-compression.herokuapp.com/

#
## Running locally (project part 2)

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org).

```console
$ git clone https://github.com/mferri17/dct-image-compression
$ cd dct-image-compression
$ pip install -r requirements.txt
$ python manage.py runserver 9999
```


If you prefer, you can also run the application using Heroku. First of all, you have to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
After `pip install`, you can run the application locally with this command for Linux users:
```console
$ heroku local
```

Or this one for Windows users:
```console
> heroku local web -f Procfile.windows
```

Your app should now be running on [localhost:9999](http://localhost:9999/). Using the Web App, you a `media` folder should appear in the project root, that is where uploaded images are saved.


### Deploying to Heroku

```console
$ heroku create
$ git push heroku master
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

For more information about using Python on Heroku, see [these articles](https://devcenter.heroku.com/categories/python).


## Folder Tree Structure

In `docs` folder you can find **project description**, some **slides** and **proposed images** to test the application.

This is a **Django Web App**. Most relevant code that directly use DCT2 algorithm is placed into `webui/views.py` (the component that handle browser requests) and `webui/utils.py` (containing the algorithm described in the project description).

Other files are needed for running a Django projects (see, for example, `webui/templates` for the Views and `webui/urls.py` for routing) and deploying it on Heroku (such as `app.json` and `Procfile`).



#
## Authors

- **Nassim Habbash** (808292) - [dodicin](https://github.com/dodicin)
- **Marco Ferri** (807130) - [mferri17](https://github.com/mferri17)