"""
Debug entry point for Streamlit app.
Right-click this file in PyCharm and select 'Debug' to run with breakpoints.
"""
from streamlit.web import cli as stcli
import sys

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py", "--server.runOnSave=false"]
    stcli.main()