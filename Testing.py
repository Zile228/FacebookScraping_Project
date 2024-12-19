from GroupScraping import FacebookGroup
import pandas as pd

NCSKTCN = FacebookGroup(r"C:\Users\ASUS\chromedriver-win64\chromedriver-win64\chromedriver.exe")
NCSKTCN.login("youremail", "yourpassword")
post = NCSKTCN.scrape("yourlink")

df = pd.DataFrame({"Post": post})
df.to_csv("Yourcsv.csv", index = False)

