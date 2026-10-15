class PDController:
    def __init__(self):
        self.kp = 0.15 # proportional gain
        self.kd = 0.6 # derivative gain
        self.previous_error = 0

    def control(self, reference, observation):
        # Calculate error term for the time step
        error = reference - observation
        
        # Calculate the control action using PD controller
        action = self.kp * error + self.kd * (error - self.previous_error)

        # Updates previous error for next time step
        self.previous_error = error
        return action




    