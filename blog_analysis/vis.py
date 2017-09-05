from bkcharts.attributes import CatAttr
from bokeh.charts import Bar, output_file, show
from bokeh.models import NumeralTickFormatter


def plot_bar_chart(table, file_name):
    bar = Bar(table, values='views', label=CatAttr(columns=['languages'],
                                                   sort=False),
              title='Programming Languages popularity', legend=False)

    bar.yaxis.formatter = NumeralTickFormatter(format="0.0a")
    output_file(file_name)

    show(bar)
