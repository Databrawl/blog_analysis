from bokeh.charts import Bar, output_file, show


def plot_table(table, file_name):
    data = {
        'sample': ['1st', '2nd', '1st', '2nd', '1st', '2nd'],
        'interpreter': ['python', 'python', 'pypy', 'pypy', 'jython',
                        'jython'],
        'timing': [-2, 5, 12, 40, 22, 30]
    }

    # x-axis labels pulled from the interpreter column, stacking labels from
    #  sample column
    bar = Bar(data, values='timing', label='interpreter', stack='sample',
              agg='mean',
              title="Python Interpreter Sampling", legend='top_right',
              width=400)

    p2 = Bar(table, title='Programming Languages popularity')

    output_file("bar.html")

    show(p2)
