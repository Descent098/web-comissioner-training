# Web commissioner Training

The purpose of this repo is to collect together the resources for web comissioner training. 

## Table of contents

- [Day 1 Basics of HTML, CSS, JS](#day-1-basics-of-html-css-js)
- [Day 2 Basics of static site generators](#day-2-basics-of-static-site-generators)
- [Day 3 Basics of CI/CD, git deployments, and a tour around our system](#day-3-basics-of-cicd-git-deployments-and-a-tour-around-our-system)
- [Day 4 Networking & infastructure fundamentals](#day-4-networking--infastructure-fundamentals)

**Assumptions/Prerequisites:**

- You know git & about github (see here if you dont: [Intro to Git (Schulich Ignite X NASA Space Apps)](https://www.youtube.com/watch?v=NwASRGFz5Wg) )

- You know some sort of programming language

- If you already know web development you can skip lecture 1, if you know web developnment with static site generators you can skip 1 and 2

- Setup on first download
  
  - On initial clone run `git submodule update --init --recursive`
  
  - Update submodules using `git submodule update --recursive --remote`

## Schedule

| Topic                                                            | Slides                                                                                                 | Date                      |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------- |
| Fundamentals of version control and git                          | [Intro to Git (Schulich Ignite X NASA Space Apps) ](https://www.youtube.com/watch?v=NwASRGFz5Wg)       | N/A                       |
| Basics of HTML/CSS/JS and basic web development workflows        | [Basic Web Technologies](https://kieranwood.ca/basic-web-technologies/)                                | June 24th (Fri): 10-11:30 |
| Basics of static site generators & usage of Hugo                 | [Static site generators](https://kieranwood.ca/static-site-generators)                                 | June 25th (Sat): 10-11:30 |
| Basics of CI/CD, git deployments, and a tour around our system   | [Static Site Hosting done easily Slide 38 onward](https://kieranwood.ca/static-site-hosting/#slide=38) | July 1st (Fri) 10-11:30   |
| Basic networking and infrastructure (how people access our site) |                                                                                                        | July 2nd (sat) 10-11:30   |

## Day 1 Basics of HTML, CSS, JS

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
  - `<span class="long-dates">February 14, 2022 — April 11, 2022</span>` <-- modify this element to have todays date

## Day 2 Basics of static site generators

- Slides - [Static site generators](https://kieranwood.ca/static-site-generators)

- Transforming data or Code generation

- templating languages
  
  - Cover Hugo specifics (called go html or go text templates, specific to hugo and go apps)

- Example SSG's
  
  - Using hugo
    
    - [Hugo install](https://gohugo.io/getting-started/quick-start/)
    
    - [Hugo Source](https://github.com/gohugoio/hugo) 
    
    - [Hugo Docs](https://gohugo.io/documentation/)
    
    - [Ignite Site Source](https://github.com/Schulich-Ignite/website)
  
  - Using ezcv
    
    - [ezcv Source](https://github.com/Descent098/ezcv) 
    
    - [ezcv Docs](https://ezcv.readthedocs.io/en/latest/)
  
  - Using ezprez
    
    - [ezprez Source](https://github.com/Descent098/ezprez) 
    
    - [ezprez Docs](https://ezprez.readthedocs.io/en/latest/)
    
    - [Presentation Source](https://github.com/Descent098/static-site-generators)

## Day 3 Basics of CI/CD, git deployments, and a tour around our system

- [Static Site Hosting done easily Slide 38 onward](https://kieranwood.ca/static-site-hosting/#slide=38)

- CI/CD
  
  - Virtual computer that you input commands to
  
  - In our case we build the site, then GH Pages takes over and just serves the files
  
  - cron scheduling
  
  - use cases
    
    - Running test cases
    - build site on schedule
  
  - Concept of github actions
    
    - When we make pushes to master `.github/workflows/hugo.yml` runs and deploys our site changes to `gh-pages` which then runs the github pages pipeline which publishes those files live

- How to make changes to our site
  
  - Documentation
    
    - [GitHub - Schulich-Ignite/website: The 2020 revamp of the schulich ignite website](https://github.com/Schulich-Ignite/website#table-of-contents)
    
    - Dev guide [GitHub - Schulich-Ignite/website: The 2020 revamp of the schulich ignite website](https://github.com/Schulich-Ignite/website#development-guide)
  
  - How to schedule content updates
    
    - [GitHub - Schulich-Ignite/website: The 2020 revamp of the schulich ignite website](https://github.com/Schulich-Ignite/website#building-on-a-schedule)
    
    - Cron [website/hugo.yml at master · Schulich-Ignite/website · GitHub](https://github.com/Schulich-Ignite/website/blob/master/.github/workflows/hugo.yml#L9)
    
    - Any content that has it's date before the current time will not be published. Also won't be published if not `ready`
  
  - How to change themes
    
    - [GitHub - Schulich-Ignite/website: The 2020 revamp of the schulich ignite website](https://github.com/Schulich-Ignite/website#site-variables) (status)

## Day 4 Networking & infastructure fundamentals

- Everything you need to know about networking to keep the site up and running along with a bit of extra theory to understand what each piece is doing
  
  - Review [GitHub - Schulich-Ignite/website: The 2020 revamp of the schulich ignite website](https://github.com/Schulich-Ignite/website#infastructure)
    
    - Look at how each piece interacts with each other and what it's responsible for
    - HTTP 4xx vs 5xx errors and which parts are responsible for each

- Socket (TCP/UDP) --> HTTP request --> DNR --> DNS provider --> Host at port --> HTTP Response
