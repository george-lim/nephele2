import shlex

from lib.core.interface import Interface
from lib.events.scheduler import Scheduler

def handler(event, _):
  interface = Interface(event['interface'])

  try:
    args = shlex.split(event['command'])[1:]
  except:
    interface.reply_message('Failed to parse input.')
    raise

  if len(args) < 1:
    interface.reply_message('Please provide a scheduled event name to enable.')
    raise Exception('missing scheduled event name')

  try:
    event_name = args[0]

    scheduler = Scheduler(event['userId'])
    scheduler.enable_event(event_name)

    interface.reply_message('Successfully enabled scheduled event!')
  except:
    interface.reply_message('Failed to enable scheduled event: invalid event name.')
    raise
