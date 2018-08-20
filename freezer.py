from flask_frozen import Freezer
from app import app, Library

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def library():
    for library in Library.query.all():
        yield { 'dbn': library.dbn }

if __name__ == '__main__':
    freezer.freeze()