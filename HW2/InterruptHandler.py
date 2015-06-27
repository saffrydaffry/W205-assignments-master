__author__ = 'Safyre'

def interrupt(signum, frame):
   print "Interrupted, closing ..."
   # magic goes here
   exit(1)

signal.signal(signal.SIGINT, interrupt)