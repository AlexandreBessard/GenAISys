from IPython.display import display, HTML, clear_output
from ipywidgets import Dropdown, Text, Checkbox, VBox, Layout, Output, Button, HBox

from genaisys.event_driven import on_user_change, handle_submit, handle_button_click

# Module-level shared state (accessible from other modules)
active_user = "User01"
debug_output = Output()
conversation_output = Output()
user01 = "User01"
user_histories = {user01: [], "User02": [], "User03": []}
# Create a checkbox to toggle agent response
agent_checkbox = Checkbox(
    value=True,
    description='Agent',
    layout=Layout(width='100px')
)
# Create the input box widget
input_box = Text(
    placeholder="Type your message here and press Enter or click Send",
    layout=Layout(width='400px')
)

if __name__ == '__main__':
    # Init conversation histories for all users and active user
    print("Executing...")
    conversation_active = True
    # Create a dropdown to select the user
    user_selector = Dropdown(
        options=[user01, "User02", "User03"], # lists the available users that can be expanded
        value=active_user,
        description="User:",
        layout=Layout(width="200px")
    )
    # Event handler
    # Event listener that will detect when the value of user_selector changes
    user_selector.observe(on_user_change, names='value')
    # Create the input box widget
    input_box = Text(
        placeholder="Type your message here and press Enter or click Send",
        layout=Layout(width='400px')
    )
    # Use the traditional on_submit for Enter key
    input_box.on_submit(handle_submit)
    # Create a send button as alternative
    send_button = Button(
        description='Send',
        button_style='primary',
        layout=Layout(width='80px')
    )
    send_button.on_click(handle_button_click)

    # Create a checkbox to toggle agent response
    agent_checkbox = Checkbox(
        value=True,
        description='Agent',
        layout=Layout(width='100px')
    )

    # Display the interface
    print("Setting up interface...")
    display(HTML("<h3>GenAI Chat Interface</h3>"))
    display(user_selector)
    display(HBox([input_box, send_button]))
    display(agent_checkbox)
    display(HTML("<hr><h4>Conversation:</h4>"))
    display(conversation_output)
    display(HTML("<hr><h4>Debug Output:</h4>"))
    display(debug_output)

    with debug_output:
        print("DEBUG: Interface setup complete. Ready for input.")