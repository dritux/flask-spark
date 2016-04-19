from flask.ext.script import Manager
from spark import app

manager = Manager(app)

@manager.command
def generate_api_key(name):
    print "Environment settings variable: SPARK"
    print app.signer.sign(name)

@manager.command
def submit(filename):
    print filename

if __name__ == '__main__':
    manager.run()
