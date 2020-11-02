# Sphinx Template

## Install template

1. `$ git clone https://github.com/DukeOfEtiquette/sphinx_template.git`
2. Update info in `source/conf.py`, for example:

```
# -- Project information -----------------------------------------------------

project = 'Sphinx Template'
copyright = '2020, Adam DuQuette <duquetteadam@gmail.com>'
author = 'Adam DuQuette <duquetteadam@gmail.com>'
```

3. If your documentation will be part of a larger project under vcs, then remove the hidden `.git` folder for this template
   - `$ rm -rf .git`
   - **DANGER** Don't delete the `.git` of the parent project!

## Install dependencies

1. `$ python3 -m venv venv/` # create a python virtualenv
2. `$ source venv/bin/activate` # activate the python virtualenv
3. `$ pip install -r requirements.txt` # install project dependencies
4. `$ npm install` # install dev tools

**NOTE**: Before running any script, start your Python virtual environment.

- `$ source venv/vin/activate`

Last, update `source/_templates/searchbox.html` to display your desired text in the search box.

## Running the project

### Build

Start a `make` build:

- `$ make clean html`

or with npm

- `$ npm run build`

The build output is located at `build/html/`.

### Start

Serve the project from `build/html/` with your preferred tool, or with npm:

- `$ npm start`

## Contribute

### Build in DEV mode

*DEV mode* will include content under [.. only::](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#including-content-based-on-tags) directives. See *devhtml* in the *Makefile* for more information.

- `$ make clean devhtml`

or with npm

- `$ npm run build:dev`

The build output is located at `build_dev/html/`.

### Start in DEV mode

Serve the project from `build_dev/html/` with your preferred tool, or with npm

- `$ npm run start:dev`

Using this npm script will serve the project at http://localhost:8080 and will automatically **reload** the browser if it detects any changes to `build_dev/html/`.

### Watch in DEV mode

Run this script in a seperate window from the dev server. It will automatically **build** the project anytime a change is made to any `rst` or `py` files in `source/`.

- `$ npm run watch`

Running this script **and** `npm
### sphinx-veldus-theme

This template uses the [sphinx-veldus-theme]() for the Sphinx Theme.f note

### netlify.toml

This is only needed if you plan to deploy the site using Netlify.

### source/dm_zone

Any content in this folder will be **ignored** during build. You can place content her that you do not want published, but want to track as part of the project (say, for draft content).

### sphinx-veldus-ext

This template comes with [sphinx-veldus-ext]() pre-installed.

### sphinx-veldus-theme

This template uses the [sphinx-veldus-theme]() for the Sphinx Theme.