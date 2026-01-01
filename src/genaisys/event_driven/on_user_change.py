from .update_display import update_display

def on_user_change(change):
    from . import main
    # Create local references
    debug_output = main.debug_output
    active_user = change['new']
    with debug_output:
        print(f"DEBUG: User changed to: {active_user}")
    update_display()  # Update the display to show the new active user's history