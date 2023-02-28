from __future__ import annotations
from datetime import datetime

from shiny import *

app_ui = ui.page_fluid(
    ui.input_action_button("close", "Close the session"),
)


def server(input: Inputs, output: Outputs, session: Session):
    def log():
        print("Session ended at: " + datetime.now().strftime("%H:%M:%S"))

    session.on_ended(log)

    @reactive.Effect
    @reactive.event(input.close)
    async def _():
        await session.close()


app = App(app_ui, server)
