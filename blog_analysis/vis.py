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


def split(collection, chunk_size):
    k, mod = divmod(len(collection), chunk_size)
    iterations = k + 1 if mod else 0
    length = len(collection)
    return [collection[i * chunk_size:min((i + 1) * chunk_size, length)]
            for i in range(iterations)]
    # k, mod = divmod(len(collection), n)
    # return (collection[i * k + min(i, mod):(i + 1) * k + min(i + 1, mod)]
    #         for i in range(n))

print(split(list(range(10)), 2))
print(split(list(range(10)), 3))
print(split(list(range(10)), 4))
print(split(list(range(11)), 2))


def plot_scatter_charts(data, file_name):
    output_file("layout.html")

    scatters = []
    for lang, values in data.items():
        s = figure(width=300, plot_height=300, title=lang)
        s.circle(values[0], values[1], size=10, color="navy", alpha=0.5)
        scatters.append(s)

    split_scatters = split(scatters, 3)
    # put all the plots in a grid layout
    p = gridplot(split_scatters)

    output_file(file_name)

    # TODO: remove!
    # show the results
    show(p)


def plot_scatter_charts_2(data, file_name):
    # p = Scatter(df, x='mpg', y='hp', title="HP vs MPG",
    #             xlabel="Miles Per Gallon", ylabel="Horsepower")
    #
    # output_file("scatter.html")
    #
    # # TODO: remove!
    # show(p)
    from bokeh.io import gridplot, output_file, show
    from bokeh.plotting import figure

    output_file("layout.html")

    x = list(range(11))
    y0 = x
    y1 = [10 - i for i in x]
    y2 = [abs(i - 5) for i in x]

    # create a new plot
    s1 = figure(width=250, plot_height=250, title=None)
    s1.circle(x, y0, size=10, color="navy", alpha=0.5)

    # create another one
    s2 = figure(width=250, height=250, title=None)
    s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

    # create and another
    s3 = figure(width=250, height=250, title=None)
    s3.square(x, y2, size=10, color="olive", alpha=0.5)

    # put all the plots in a grid layout
    p = gridplot([[s1, s2], [None, s3]])

    # show the results
    show(p)
