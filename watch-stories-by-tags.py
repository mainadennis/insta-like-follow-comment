import random
from config import *
from instapy import smart_run

tags = ["tag1","tag2"]

# let's go! :>
with smart_run(session):
    # general settings
    session.set_simulation(enabled=True)
    session.set_do_story(enabled=True, percentage=100)

    # activities
    session.story_by_tags(tags)

