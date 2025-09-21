#in this we are creating different methods, where each method is doing some complex tasks.


#You're creating a monthly report for a cafes's sales.Instead of putting all 
#logic in one place, break it down.
# TASK : write a function generate_report that calls:
#fetch_sales()
#filter_valid_orders()
#summarze_data()

def fetch_sales():
    print("Fetching the sales data")

def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarising sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")

generate_report()