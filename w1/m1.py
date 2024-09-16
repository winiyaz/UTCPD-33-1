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

def test_url():
    """ Testin the url here  """
    url = "http://api.open-notify.org/iss-now.json"

    # Capture the response here
    repo = rq.get(url)
    repo.raise_for_status()

    # Extract the data here
    resdata = repo.json()['iss_position']['longitude']
    pprint(resdata, expand_all=True)

# Using the 
test_url()
