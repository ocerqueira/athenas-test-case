import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Espera pelo banco de dados estar disponível'

    def handle(self, *args, **kwargs):
        self.stdout.write('Esperando o banco de dados...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Banco de dados não disponível, aguardando...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Banco de dados disponível!'))
