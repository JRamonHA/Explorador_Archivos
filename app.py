import pandas as pd
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_widget

f = './data/Tmx.csv'
tmx = pd.read_csv(f, index_col=0, parse_dates=True)
columnas = list(tmx.columns)

ui.page_opts(title="Explorador de archivos")

with ui.sidebar():
        ui.input_select("var", "Selecciona una variable", choices=columnas)
        ui.input_switch("month", "Promedio mensual", value=True)  

@render_widget
def grafica():
    var = input.var()
    df = tmx.resample('ME').mean().reset_index() if input.month() else tmx.reset_index()
    fig = px.line(
        df,
        x='time',  
        y=var,
        title=f"{var}",
        labels={'time': 'Fecha', var: var}
    )
    return fig