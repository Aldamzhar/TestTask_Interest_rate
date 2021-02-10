def interest_rate(json_object, return_interest_paid_percent): # here, assumed interest is in percent
    return_interest_paid = return_interest_paid_percent / 100
    num_of_years = json_object["periods"] # I assume that the field for number of years is called periods
    cumulative = json_object["principal"] * (((1 + return_interest_paid)**num_of_years) - 1)
    return cumulative

# print(interest_rate({"periods": 5, "principal": 10000}, 10)) I assume that this might be the format of a dictionary (json) and interest paid parameters
# sample for checking functionality