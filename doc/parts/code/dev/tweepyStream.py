stream = tweepy.Stream(auth, listener)
with open(out_log, 'w') as log:
    while (True):
        log.write("Reconnecting ...")
        try:
            stream.filter(track=['twitter'], languages=['ru'])
        except Exception as e:
            log.write("Exception: %s"%(str(e)))
