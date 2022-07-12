import  statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
import csv
import pandas as pd

df = pd.read_csv("data.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)

def R30_samples():
    samples=[]
    for i in range(0,30):
        Rsamples=random.randInt(0,len(data)-1)
        values=data[Rsamples]
        samples.append(values)
    mean=statistics.mean(samples)
    return mean

def setup():
    test_data=[]
    for i in range(0,100):
        mean_set=R30_samples()
        test_data.append(mean_set)
    plot_graph(test_data)

def plot_graph(test_data):
    mean2=test_data
    graph=ff.create_distplot([data],["Math_score"])
    graph.show()

std_deviation = statistics.stdev(data)
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig=ff.create_distplot([std_deviation],["Math_score"])
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
