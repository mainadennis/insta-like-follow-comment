import random
from config import *
from instapy import smart_run

users = ["user1","user2","user3","user4"]
# let's go! :>
with smart_run(session):
    # general settings
    session.set_simulation(enabled=True)
    session.set_do_story(enabled=True, percentage=100)

    # activities
    #session.grab_following(username="cakeyKenya", amount=252)
    """ set story by users expects a list of all the usernames you wish to view their story
    	The above commented line grabs all the usernames of the users that you're following and stores them in a json file in the InstaPy folder
    	under InstaPy/logs/relationship_data/<username>/following/
    	You can then copy the usernames and paste them above on the users variable.
    	If there is no stories to watch on that user, he/she will be skipped.
    """
    session.story_by_users(users)

