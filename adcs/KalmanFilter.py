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

# Initializing parameters
initial_position_guess = 5
initial_variance_guess = 10000
q = 0.10
r = 2

#prediction of next state
prediction_position_next_timestamp = initial_position_guess
prediction_variance_next_timestamp = initial_variance_guess + q

save_estimates = []
save_predictions = [prediction_position_next_timestamp]


for i in position:
    #estimation of current state
    kalman_gain = prediction_variance_next_timestamp/(prediction_variance_next_timestamp + r)
    prediction_position_current_position = prediction_position_next_timestamp + kalman_gain * (i - prediction_position_next_timestamp)
    prediction_variance_current_timestamp = (1 - kalman_gain) * prediction_variance_next_timestamp
    save_estimates.append(prediction_position_current_position+4)

    # prediction of next state
    prediction_position_next_timestamp = prediction_position_current_position
    prediction_variance_next_timestamp = prediction_variance_current_timestamp + q
    save_predictions.append(prediction_position_next_timestamp)

save_predictions.pop()

Y = find_truevalue_line(1)

# Plot the position over time
plt.figure(figsize=(10, 6))
plt.plot(time,Y,color='g',label='True Value')
plt.plot(time, position,color='b' ,label='Position of the dog')
plt.plot(time,save_estimates,color='r',label='Estimation')
#plt.plot(time,save_predictions,color='c',label='Predictions')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude (m)')
plt.title('Position of the dog over time')
plt.legend()
plt.grid(True)
plt.show()





