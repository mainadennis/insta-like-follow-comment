import random
from instapy import smart_run
from config import *

dont_likes = ['sex', 'nude', 'naked','pussy']
comments = ['I love your baking! :smiling_face_with_heart_eyes: @{}',
        'Your feed is an inspiration :smiling_face_with_smiling_eyes:',
        'Just incredible :open_mouth:',
        'Sweetness is in the air :shortcake: @{}',
        'Yummy! :face_savoring_food: @{}',
        'Looks amazing :beating_heart: @{}',
        'Getting inspired by you :sparkles: @{}',
        ':raised_hands: :cake: Yes!',
        'I can feel your passion :smiling_face_with_hearts: @{}',
        ':smiling_face_with_smiling_eyes:']
# will prevent commenting on and unfollowing your good friends (the images will still be liked)
friends = ['friend1',"friend2"]

like_tag_list = ['bakery', 'bakeries', 'bakingtime', 'bakingfun',
                 'bakerylife', 'bakerslife', 'weddingcakes',
                 'weddingcakesideas', 'birthdaycakes', 'birthdaycakesforgirls', 'birthdaycakesforboys',
                 'bakerylove']

# prevent posts that contain some plantbased meat from being skipped
ignore_list = ['vegan', 'veggie', 'plantbased']

accounts = ['similarAccount1', 'similarAccount2', 'similarAccount3']

with smart_run(session):
    # settings
    """I used to have potency_ratio=-0.85 and max_followers=1200 for set_relationship_bounds()
        Having a stricter relationship bound to target only low profiles 
        users was not very useful,
        as interactions/sever calls ratio was very low. I would reach the 
        server call threshold for
        the day before even crossing half of the presumed safe limits for 
        likes, follow and comments (yes,
        looks like quiet a lot of big(bot) managed accounts out there!!).
        So I relaxed it a bit to -0.50 and 2000 respectively.
    """
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-0.50,
                                    delimit_by_numbers=True,
                                    max_following=3500,
                                    min_followers=25,
                                    min_following=25,
                                    max_followers=2000)
    # my account is small at the moment, so I keep smaller upper threshold
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                 sleepyhead=True,
                                 stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_daily=700,
                                 peak_comments_daily=150,
                                 peak_follows_daily=125,
                                 peak_unfollows_daily=200,
                                 peak_server_calls_daily=3000)
                                 
    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    # don't like if a post already has more than 150 likes
    session.set_delimit_liking(enabled=True, max_likes=150, min_likes=0)
    # don't comment if a post already has more than 4 comments
    session.set_delimit_commenting(enabled=True, max_comments=4, min_comments=0)
    session.set_ignore_if_contains(ignore_list)
    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=60)
    session.set_do_like(enabled=True, percentage=80)
    session.set_do_comment(enabled=True, percentage=30)
    session.set_comments(comments, media='Photo')

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 100), interact=True)
    # unfollow users followed through this bot that hasn't followed back within one week
    session.unfollow_users(amount=random.randint(75, 150),
                           instapy_followed_enabled=True,
                           nonFollowers=True,
                           style="FIFO",
                           unfollow_after=168 * 60 * 60, sleep_delay=501)
                           
    session.join_pods(topic='food') #'general', 'fashion', 'food', 'travel', 'sports', 'entertainment'

    
session.end()
