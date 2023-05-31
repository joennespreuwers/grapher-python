import io
import base64
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from sympy import symbols, sympify, lambdify


def plot(f: str = "x"):
    print(f)
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x = np.linspace(-10, 10, 100)
    y = np.vectorize(lambdify(symbols("x"), sympify(f)))(x)
    axis.plot(x, y, label=f"y={f}")

    axis.spines["left"].set_position("center")
    axis.spines["bottom"].set_position("zero")
    axis.spines["right"].set_color("none")
    axis.spines["top"].set_color("none")
    axis.xaxis.set_ticks_position("bottom")
    axis.yaxis.set_ticks_position("left")

    axis.set_xlim(-10, 10)
    axis.set_ylim(-10, 10)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    image_data = base64.b64encode(output.getvalue()).decode("utf-8")
    return image_data
