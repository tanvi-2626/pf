import warnings
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error

warnings.filterwarnings("ignore")

demand = [120, 125, 132, 128, 140, 145,
          150, 148, 155, 162, 168, 175]

train = demand[:10]
test = demand[10:]

model = ExponentialSmoothing(train, trend="add").fit()

forecast = model.forecast(2)

mae = mean_absolute_error(test, forecast)
rmse = np.sqrt(mean_squared_error(test, forecast))

print("TIME SERIES ANALYSIS")
print("--------------------")
print("Input Demand:", demand)
print("Actual Demand:", test)
print("Forecast Demand:", [round(float(x), 2) for x in forecast])
print("MAE:", round(float(mae), 2))
print("RMSE:", round(float(rmse), 2))

future = model.forecast(3)

print("\nFUTURE DEMAND FORECAST")
print("----------------------")
print([round(float(x), 2) for x in future])
