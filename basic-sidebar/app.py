import pandas as pd
import plotly.express as px
from shiny.express import input, render, ui

f = './data/Tmx.csv'
tmx = pd.read_csv(f, index_col=0, parse_dates=True)
columnas = list(tmx.columns)

ui.page_opts(title="Explorador EPWs")

with ui.sidebar():
    ui.input_select("var", "Selecciona una variable", choices=columnas)
    ui.input_switch("month", "Promedio de remuestreo por mes", value=True)

@render.ui
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
    return ui.HTML(fig.to_html(full_html=False, include_plotlyjs='cdn'))
