from bkcharts import Bar
from bkcharts.attributes import CatAttr
from bokeh.io import gridplot, output_file, show
from bokeh.models import NumeralTickFormatter
from bokeh.plotting import figure


def plot_bar_chart(data, file_name):
    bar = Bar(data, values='views', label=CatAttr(columns=['languages'],
                                                  sort=False),
              title='Programming Languages popularity', legend=False)

    bar.yaxis.formatter = NumeralTickFormatter(format="0.0a")
    output_file(file_name)
    show(bar)


def split(collection, chunk_size):
    k, mod = divmod(len(collection), chunk_size)
    iterations = k + (1 if mod else 0)
    length = len(collection)
    return [collection[i * chunk_size:min((i + 1) * chunk_size, length)]
            for i in range(iterations)]


def plot_scatter_charts(data, file_name):
    scatters = []
    for lang, values in data.items():
        s = figure(width=300, plot_height=300, title=lang)
        s.circle(values[0], values[1], size=10, color="navy", alpha=0.5)
        s.yaxis.formatter = NumeralTickFormatter(format="0.0a")
        scatters.append(s)
    split_scatters = split(scatters, 3)
    p = gridplot(split_scatters)
    output_file(file_name)
    show(p)
