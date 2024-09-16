#!/usr/bin/env python3

## Prettification code 
# PRettifer 
# Prettifyer code

# ------------------------------------------------------
from rich import print as rprint # For rprinting
from rich.pretty import pprint # For pretty printing
from rich import inspect # For inspect
from rich.console import Console # For console.print
from rich.markdown import Markdown # For markdown
from rich.panel import Panel # For Panel()
from rich import box # For Panel Boxes
from rich.prompt import Prompt # For Prompting 
from rich.style import Style # For styles colors
from rich.text import Text # For text Styles
console = Console() # Standard code to access console
from rich.traceback import install
install(show_locals=True)
# -------------------------------------------------------
##

import requests as rq

url = "http://api.open-notify.org/iss-now.json"
repo = rq.get(url).json()

# Using the 
pprint(repo, expand_all=True)
