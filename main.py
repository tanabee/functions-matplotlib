from flask import make_response
import matplotlib.pyplot
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO
import random

def graph(request):

    fig, ax = matplotlib.pyplot.subplots()
    ax.set_title(u'GRAPH')
    x_ax = range(1, 200)
    y_ax = [x * random.randint(100, 200) for x in x_ax]
    ax.plot(x_ax, y_ax)

    canvas = FigureCanvasAgg(fig)
    buf = BytesIO()
    canvas.print_png(buf)
    data = buf.getvalue()

    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)
    return response
