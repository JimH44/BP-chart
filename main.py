import matplotlib.pyplot as plt
import datetime

# Sample blood pressure data
dates = [datetime.date(2023, 10, 1), datetime.date(2023, 10, 2), datetime.date(2023, 10, 3), datetime.date(2023, 10, 4), datetime.date(2023, 10, 5)]
systolic = [120, 125, 118, 130, 122]
diastolic = [80, 82, 78, 85, 80]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(dates, systolic, label='Systolic', marker='o', color='red')
plt.plot(dates, diastolic, label='Diastolic', marker='o', color='blue')

# Customize the plot
plt.title('Blood Pressure Over Time')
plt.xlabel('Date')
plt.ylabel('Blood Pressure (mmHg)')
plt.grid(True)
plt.legend()

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()