from order_service import create_order
from database import SessionLocal, Base, engine
from user_repository import JsonPlaceholderUserRepository

Base.metadata.create_all(bind=engine)

class DummyLogger:
    def log(self, msg):
        # logger que no hace nada
        pass

class NullNotifier:
    def send(self, to, message):
        # notifier que no hace nada
        pass

def test_create_order_integration_real_api():
    db = SessionLocal()
    order = create_order(1, 50, NullNotifier(), DummyLogger(), db, JsonPlaceholderUserRepository())
    # estado esperado
    assert order.status == 'CREATED'
    db.close()
