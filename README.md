## Flask Application Design

### HTML Files
- The application will require two main HTML files:
  - `index.html`: This will serve as the landing page and display the collection of helpful mental health resources. It should have a visually appealing design, clear navigation options, and accessibility features.
  - `contact.html`: This will provide a form for users to contact the organization or subscribe to a newsletter or updates on mental health resources.

### Routes
- The application will define three routes:
  - `@app.route("/")`: This route will handle the main landing page and display the `index.html` file.
  - `@app.route("/contact")`: This route will display the `contact.html` file, allowing users to get in touch or subscribe to updates.
  - `@app.route("/resources")`: This route will serve a JSON response containing a list of the available mental health resources. It will be used by the front-end to dynamically populate the landing page with resource information.