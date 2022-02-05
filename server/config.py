import twint

def TwintConfig(**kwargs):
    c = twint.Config()
    twint.output.clean_lists()
    old = twint.output.tweets_list
    if (old):
        old.clear()
    if (kwargs['username']):
        c.Username = kwargs['username']
    if (kwargs['search_term']):
        c.Search = kwargs['search_term']
    c.Store_object = True                #creates store data object; required.
    c.Hide_output = True                 #prevents spamming the terminal; required.
    c.Limit = 102                        #recommended to stay at this number for aesthetics, or below 1000 for speed; required.
    #c.Profile_full = True               #includes shadowbanned accounts & tweets. warning: slow; optional.
    return c
