from ezprez.core import Slide, Presentation
from ezprez.components import *

# Creating a slide
Slide('Source Files', 'The source file(s) are written in python using .py files', background='black')

# Presentation settings
title = 'Static site generators'
description = 'An overview of markup transformation & Static Site Generator (SSG) demo'
url = 'https://kieranwood.ca/static-site-generators'

prez = Presentation(title, description, url)
prez.export('.', force=True, folder_name='Presentation') # Export to ./Presentation