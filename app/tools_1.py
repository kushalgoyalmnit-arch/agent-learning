def calculator(expression):
    return eval(expression)

def get_time():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")