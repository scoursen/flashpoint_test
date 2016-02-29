from django.core.management.base import BaseCommand, CommandError
import time
import random
from django.utils import timezone
from stats.models import Messages

GEOGRAPHY = {
    'New York': ['New York', 'Albany', 'Buffalo'],
    'New Jersey': ['Trenton', 'Newark', 'Matawan'],
    'Pennsylvania': ['Philadelphia', 'Pittsburgh'],
    'Montana': ['Bozeman', 'Missoula', 'Ronan'],
}

USERS = ['User1', 'User2', 'User3', 'Admin1', 'Admin2', 'Support1', 'Support2']

class Command(BaseCommand):
    help = 'Continuously generate random stat messages'

    def handle(self, *args, **options):
        while True:
            state = random.choice(GEOGRAPHY.keys())
            city = random.choice(GEOGRAPHY[state])
            username = random.choice(USERS)
            message = 'Random message @ {0}'.format(timezone.now().isoformat())
            Messages.objects.create(state=state, city=city, username=username, message=message)
            self.stdout.write(self.style.SUCCESS('Generated random message for {0} in {1}, {2}'.format(username, city, state)))
            time.sleep(random.random())
