
from flask_script import Manager  
from flask_migrate import Migrate, MigrateCommand

from app import app

from models import Variation, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed_database():
    variation1 = Variation(label="dog", keyword="animal")
    db.session.add(variation1)
    variation2 = Variation(label="big horse", keyword="animal")
    db.session.add(variation2)
    variation3 = Variation(label="fluffy lion", keyword="animal")
    db.session.add(variation3)
    variation4 = Variation(label="cat", keyword="animal")
    db.session.add(variation4)
    db.session.commit()


@manager.shell
def shell_context():
    return dict(app=app,
                db=db,
                Variation=Variation)


if __name__ == '__main__':
    manager.run()

