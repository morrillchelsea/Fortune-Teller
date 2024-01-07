from loghandler import user_logger
from databasehelper import auth_user

# user_module.py
user_session = None

def login(username, password):
    # perform authentication logic
    global user_session
    
    if auth_user(username, password):
        user_session = {"username": username, "authenticated": True}

def logout():
    '''Signs user out and resets global variables'''
    global user_session
    
    user_session = None

    # verify session is closed
    if user_session == None:
        user_logger.info('User %{username}s signed out successfully')
        return True
    else:
        user_logger.error('User %{username}s Could Not Be Signed Out!')
        return False

def is_authenticated():
    global user_session
    return user_session is not None and user_session.get("authenticated", False)
