from models import Event

class EventRequests(object):
  
  def event_with_id(self, event_id):
    return Event.get(Event.id == event_id)
