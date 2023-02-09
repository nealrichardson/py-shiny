from shiny import *

app_ui = ui.page_fixed(
    ui.input_checkbox("somevalue", "Some value", False), ui.output_ui("value")
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.ui
    def value():
        return input.somevalue()


app = App(app_ui, server)
