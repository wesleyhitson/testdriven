from flask_script import Manager
from project import app

# New manager instance handles all manager commands from the command line
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
