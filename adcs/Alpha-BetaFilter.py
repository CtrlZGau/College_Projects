import numpy as np
import matplotlib.pyplot as plt

def find_truevalue_line(m):
    l = []
    for i in range(time_period):
        l.append(initial_position+m*i)
    return l

# Set the parameters
initial_position = 0
velocity = 1  # m/s
mean = 0
variance = 2  # m^2/s^2
time_period = 60  # seconds

# Create a time array from 0 to time_period with a step of 1 second
time = np.arange(time_period)

# Generate the process noise
noise = np.random.normal(mean, np.sqrt(variance), time_period)

# Calculate the position of the dog at each point in time
position = initial_position + velocity * time + noise

# Initial Guesses
initial_position_guess = 0
initial_velocity_guess = 2
time_interval = 1
n = 1
alpha = 1
beta = 0.2

# Initializations
prediction_position_with_previous_timestamp = initial_position_guess + time_interval * initial_velocity_guess
prediction_velocity_with_previous_timestamp = initial_velocity_guess

# saving the estimates and predictions
save_estimates = []
save_predictions = [prediction_position_with_previous_timestamp]


for i in position:
    # calculate current state estimates
    prediction_position_with_current_timestamp = prediction_position_with_previous_timestamp + alpha * (i - prediction_position_with_previous_timestamp)
    prediction_velocity_with_current_timestamp = prediction_velocity_with_previous_timestamp + beta * (i - prediction_position_with_previous_timestamp)/time_interval
    save_estimates.append(prediction_position_with_current_timestamp)

    # predict the next state estimates with current state estimates essentially the next timestamp's previous 
    prediction_position_with_previous_timestamp = prediction_position_with_current_timestamp + time_interval * prediction_velocity_with_current_timestamp
    prediction_velocity_with_previous_timestamp = prediction_velocity_with_current_timestamp
    n += 1
    save_predictions.append(prediction_position_with_previous_timestamp)

save_predictions.pop()

Y = find_truevalue_line(1)

# Plot the position over time
plt.figure(figsize=(10, 6))
plt.plot(time,Y,color='g',label='True Value')
plt.plot(time, position,color='b' ,label='Position of the dog')
plt.plot(time,save_estimates,color='r',label='Estimation')
plt.plot(time,save_predictions,color='c',label='Predictions')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude (m)')
plt.title('Position of the dog over time')
plt.legend()
plt.grid(True)
plt.show()
