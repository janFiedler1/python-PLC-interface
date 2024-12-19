## main.py
## This file imports the ui model, creates a controller, connects buttons on the ui to controller functions
## and displays the model

import controller
## Constants
TIMER_INTERVAL = 1000  # time in ms

if __name__ == "__main__":
    controller = controller.Controller()
