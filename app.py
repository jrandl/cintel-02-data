import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Palmer Penguin's Data: Josiah Randleman", fillable=True)

with ui.sidebar(bg="#f8f8f8", open="open"):  
    ui.h2("Sidebar")
    
    ui.input_selectize(
        "selected_attribute",  # Unique identifier for the input
        "Choose A Selected Attribute:",  # Label for the input
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
        multiple=False  # Allow multiple selections
    )

    ui.input_numeric("plotly_bin_count", "Plotly Histogram Bins:", 10)

    ui.input_slider("seaborn_bin_count", "Seaborn Bins:", min=0, max=100, value=25)

    ui.input_checkbox_group(
        "selected_species_list",
        "Choose Species:",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected= ["Adelie"],
        inline=False,
    )

    ui.hr()

    ui.a("GitHub", href="https://github.com/jrandl/cintel-02-data", target="_blank")

#with ui.layout_columns():
#
#    @render_plotly
#    def plot1():
#        return px.histogram(px.data.tips(), y="tip")
#
#    @render_plotly
#    def plot2():
#        return px.histogram(px.data.tips(), y="total_bill")
