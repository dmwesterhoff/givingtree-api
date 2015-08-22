from models import Event

class EventRequests(object):

    def event_with_id(self, event_id):
        return Event.get(Event.id == event_id)

    def events(self):
        events = []
        for event in Event.select():
            events.append(event.dict())
        return events
