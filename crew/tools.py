## https://serper.dev/
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from crewai_tools import (
    FileReadTool,
)
# os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# inititlaize the tool for internet searching capabilities
tool = SerperDevTool()
file_tool = FileReadTool()


