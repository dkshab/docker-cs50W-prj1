# services/books/manage.py


import sys
import unittest

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Book

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(Book(title='The Awakening',
                        author='Kelley Armstrong', isbn='61662763'))
    db.session.add(Book(title='The Van Alen Legacy',
                        author='Melissa de la Cruz', isbn='1423102266'))
    db.session.add(Book(title='Noughts & Crosses',
                        author='Malorie Blackman', isbn='552555703'))
    db.session.add(Book(title='Lincoln in the Bardo',
                        author='George Saunders', isbn='812995341'))
    db.session.commit()


@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()
