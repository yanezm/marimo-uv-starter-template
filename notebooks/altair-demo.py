# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "altair==6.0.0",
#     "marimo",
#     "pyarrow",
#     "vega-datasets==0.9.0",
# ]
# ///

import marimo

__generated_with = "0.19.11"
app = marimo.App(width="full", auto_download=["html"])

with app.setup:
    import marimo as mo
    import altair as alt
    from vega_datasets import data


@app.cell
def _():
    mo.md(
        """
        # Hello, marimo! 👋

        **marimo** is a next-generation Python notebook where:

        - Cells **re-run automatically** when their inputs change — no manual re-execution needed
        - UI elements like sliders and dropdowns are **first-class Python objects**
        - The notebook is stored as a plain **`.py` file**, so it works with git and your editor
        - Execution order follows **data flow**, not cell position — no hidden state

        Work through the three sections below to see these ideas in action.
        """
    )
    return


@app.cell
def _():
    mo.md("## 1 · Markdown cells")
    return


@app.cell
def _():
    mo.md(
        """
        Any cell that returns `mo.md(...)` renders as formatted text.

        You can write **bold**, _italic_, `inline code`, bullet lists, and even LaTeX:

        $$E = mc^2$$

        Everything is just Python — there is no special cell type to switch to.
        """
    )
    return


@app.cell
def _():
    mo.md("## 2 · Reactive UI elements")
    return


@app.cell
def _():
    mo.md(
        """
        Create a UI element and **return it** from a cell to display it.
        Any other cell that references the element's variable will re-run
        automatically whenever the value changes.
        """
    )
    return


@app.cell
def _():
    slider = mo.ui.slider(start=1, stop=10, value=5, label="Pick a number (1 – 10)")
    slider
    return (slider,)


@app.cell
def _(slider):
    mo.md(f"You picked **{slider.value}**. Move the slider — this cell updates instantly.")
    return


@app.cell
def _():
    mo.md("## 3 · Interactive charts with Altair")
    return


@app.cell
def _():
    mo.md(
        """
        The chart below uses the classic **cars** dataset from Vega.

        **Try it:** click and drag on the scatter plot to select a group of cars.
        The bar chart, table, and histograms below all react to your selection
        automatically — no callbacks or event handlers required.
        """
    )
    return


@app.cell
def _():
    cars = data.cars()

    brush = alt.selection_interval()

    scatter = (
        alt.Chart(cars)
        .mark_point()
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin",
        )
        .add_params(brush)
    )

    bars = (
        alt.Chart(cars)
        .mark_bar()
        .encode(y="Origin:N", color="Origin:N", x="count(Origin):Q")
        .transform_filter(brush)
    )

    chart = mo.ui.altair_chart(scatter & bars)
    chart
    return (chart,)


@app.cell
def _(chart):
    mo.md(
        f"**{len(chart.value)} car(s) selected.** "
        "The table and histograms below update as you change your selection."
    )
    return


@app.cell
def _(chart):
    filtered_data = mo.ui.table(chart.value)
    filtered_data
    return (filtered_data,)


@app.cell
def _(filtered_data):
    mo.stop(not len(filtered_data.value), mo.md("_Select rows in the table above to see histograms._"))
    mpg_hist = mo.ui.altair_chart(
        alt.Chart(filtered_data.value)
        .mark_bar()
        .encode(alt.X("Miles_per_Gallon:Q", bin=True), y="count()")
        .properties(title="Miles per Gallon")
    )
    horsepower_hist = mo.ui.altair_chart(
        alt.Chart(filtered_data.value)
        .mark_bar()
        .encode(alt.X("Horsepower:Q", bin=True), y="count()")
        .properties(title="Horsepower")
    )
    mo.hstack([mpg_hist, horsepower_hist], justify="space-around", widths="equal")
    return


if __name__ == "__main__":
    app.run()
