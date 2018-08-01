# Test Application for Vue.js and Flask SPA

### Installation instructions

Install the necessary dependencies

* [Python2.7](https://www.python.org/downloads/)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [Node.js](https://nodejs.org/en/download/)
* [PostgreSQL](https://www.postgresql.org/download/)

Clone repo, checkout test branch and make a new branch for exploring

```sh
    git clone https://bitbucket.org/amcquistan/test-app.git
	cd test-app/
    git checkout -b yourname-test-app
```

Install frontend (Vue.js) dependencies

```sh
    cd frontend
    cd test-spa
	npm install
```

Create virtualenv and activate it

```sh
	cd ../../backend
    virtualenv -p=python27 venv
	source venv/bin/activate
```

Install python packages

```sh
    (venv) pip install -r requirements.txt
```

Create the testdb postgres database

```
 psql
 username=# create database testdb;
 username=# \q
```

Run database migrations, seed database with test data, and then start the flask dev server from within backend/

```sh
    (venv) cd web
    (venv) python manage.py db upgrade
    (venv) python manage.py seed_database
	(venv) python app.py
```

In another new terminal start the webpack dev server in the frontend/test-spa/ directory (webpack dev server installs automatically with npm install)

```sh
   npm run dev
```

You should now be able to go to http://localhost:8080 and see the home page


### Directions to finish

update the Flask REST API endpoint /api/variations to query the database for all variations
and return in JSON form inside the code snippet below from app.py

```python
# app.py

@app.route('/api/variations', methods=('GET',))
def get_variations():
    # TODO: query the database using the Flask-SQLAlchemy model defined in models.py
    # and return them in a serialized list using the to_dict() method of the Variation model
    return jsonify("VARIATIONS TO HERE")

```

Update frontend/test-spa/src/api/index.js to fetch the variations from the Flask REST app
inside the code snippet shown below using axios within the function fetchVariations

```
// frontend/test-spa/src/api/index.js
export function fetchVariations () {
    // write code to do ajax call with axios to get variations from /api/variations
}
```

Update the action method in the vuex store to call the fetchVariations AJAX function
and call commit a mutation using the next function to be defined called setVariations
to set the state's variations array

```
// frontend/test-spa/src/store/index.js

const actions = {
  loadVariations ({ commit }) {
    // make async call to fetch variations
    // and use commit to commit the REST API response
    // to set the value in the state using the mutation
    // setVariations
  }
}
```


Define the setVariations vuex mutation that is called by loadVariations to store the 
results of the AJAX function fetchVariations

```
// frontend/test-spa/src/store.js

const mutations = {
  // define setVariations mutation to set the list of variations returned
  // by loadVariations action
}

```

Fetch the variations from the src/components/Variations.vue in the beforeMount 
lifecycle hook

```
<script>
export default {
  computed: {
    variations () {
      return this.$store.state.variations
    }
  },
  beforeMount () {
    // once you have finished coding the loadVariations vuex / store action you will
    // be able to call it from this Vue components lifecycle hook to make sure
    // the store contains the variations data that will be displayed in the table on
    // this component's template
  }
}
</script>
```

Build an html table in the components template as described in the comments below.

```
<template>
<section class="section">
  <div class="container is-fluid">
    <div class="columns">
      <div class="column is-offset-2">
        <table class="table is-hoverable">
          <!-- populate this table with the variations retreived from the vuex store -->
          <!-- there should be 4 columns: Keyword (keyword object field), Variation Length (length of label field), Color (background color based off Variation Length) -->
          <!-- for the color column use the css classes blue and red. assign blue if label's length is > 5 otherwise blue -->
        </table>
      </div>
    </div>
  </div>
</section>
</template>
```

Make all code changes in the branch you created above "yourname-test-app" and issue a pull request to this repo





