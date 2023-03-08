def _handle_exceptions(data):
    """
    This function sanitizes user's input.
    """
    
    try:
        data = int(data)
    except:
        raise Exception("Pass in numeric data only.")