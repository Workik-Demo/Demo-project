from typing import Dict, Any
import json

def format_response(data: Any) -> Dict:
    return {
        "status": "success",
        "data": data
    }