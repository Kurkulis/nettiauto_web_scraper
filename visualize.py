import pandas

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn


df = pandas.read_csv('listings.csv')

data = dict(
    car_model=df['Model'],
    price=df['Price'],
    motor=df['Motor'],
    year=df['Year']
)

source = ColumnDataSource(data)

output_file('index.html')

columns = [
    TableColumn(field='car_model', title="Model"),
    TableColumn(field='price', title="Price"),
    TableColumn(field='motor', title="Motor"),
    TableColumn(field='year', title="Year")
]

data_table = DataTable(source=source, columns=columns)

show(widgetbox(data_table))
