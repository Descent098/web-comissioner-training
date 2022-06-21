Day 1 Basics of HTML, CSS, JS

- Slides - [Basic Web Technologies](https://kieranwood.ca/basic-web-technologies/)
- JS course: [JavaScript Crash Course For Beginners - YouTube](https://www.youtube.com/watch?v=hdI2bqOjy3c)
- CSS Course: [CSS Crash Course For Absolute Beginners - YouTube](https://www.youtube.com/watch?v=yfoY53QXEnI)
- Build a quick and dirty demo with bootstrap
  - using the grid system: [Grid system · Bootstrap (getbootstrap.com)](https://getbootstrap.com/docs/4.0/layout/grid/)
  - Additional components: [Alerts · Bootstrap (getbootstrap.com)](https://getbootstrap.com/docs/4.0/components/alerts/)
  - Starter HTML:
    - Add in a navbar: [Navbar · Bootstrap (getbootstrap.com)](https://getbootstrap.com/docs/4.0/components/navbar/)
    - Add in a trio of cards that are full width on mobile, half on ipad and a third on full-width: [Cards · Bootstrap (getbootstrap.com)](https://getbootstrap.com/docs/4.0/components/card/#titles-text-and-links)
    - Add modals to cards: [Modal · Bootstrap (getbootstrap.com)](https://getbootstrap.com/docs/4.0/components/modal/)
    - Add buttons to the trio to link to other sites: [Buttons · Bootstrap (getbootstrap.com)](https://getbootstrap.com/docs/4.0/components/buttons/#button-tags)

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```

- Work with modifying a saved copy of the ignite site
  - Use javascript to get a certain element node and modify it in-line with a button