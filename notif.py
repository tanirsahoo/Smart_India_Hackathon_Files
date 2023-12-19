
import time
from plyer import notification
 
 
if __name__=="__main__":
 
        notification.notify(app_name = "Settings",title = "WARNING", message="You are being recorded." , timeout=2)
        time.sleep(7)