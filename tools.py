from langchain.tools import ToolRuntime
from langchain.tools import tool
import requests


@tool
def submit_user_information(email: str, phone_number: str, name: str = None, company_name: str = None) -> str:
    """Submit user information
    Args:
        email (str) s
        phone_number (str)
        name (str, optional)
        company_name (str, optional)
    """
    response = requests.post(
        "https://dev.kitaab.ai/api/event-registration/",
        json={
            "email": email,
            "phone_number": phone_number,
            "name": name,
            "company_name": company_name,
        }
    )
    if response.status_code == 200:
        return "user information submitted successfully"
    else:
        print(response.text)
        return response.text