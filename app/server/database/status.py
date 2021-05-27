def return_status(code, result, **kwargs):
    body = kwargs["body"] if ("body" in kwargs) else []
    return {"code": code, "result": result, "body": body}
