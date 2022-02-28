from instapy import InstaPy

# login credentials
insta_username = '<YourUsername>'
insta_password = '<YourPassword>'

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  disable_image_load=False,
                  bypass_security_challenge_using="mobile",
                  multi_logs=True)
