from datetime import datetime
import time
def test_1():
    assert 1 == 1
    
def test_printtime():
    current_time = datetime.now()
    # Format with date, time, seconds and milliseconds
    formatted_datetime = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"initial time : {formatted_datetime}")  # Example output: 2025-04-06 14:32:45.123
    # sleep for 1 second
    time.sleep(1)
    current_time = datetime.now()
    # Format with date, time, seconds and milliseconds
    formatted_datetime = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    # hopefilly see 1 second difference .
    print(f"final time : {formatted_datetime}")   
    
    