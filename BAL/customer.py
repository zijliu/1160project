import DAL.db as d

dta = d.DB()


def get_all_customers():
    return dta.execute_select_query("Sales", "Customer")


def get_customer(_id: int):
    return dta.execute_select_query("Sales", "Customer", params={'Id': _id})


def get_customer_by_last_name(_name: str):
    return dta.execute_select_query("Sales", "Customer", params={'Last_Name': _name})


def get_students_data():
    return dta.execute_select_query("StatsCan", "Workstats", params={'is_student': 'True'})


def get_full_dataset():
    return dta.execute_select_query("StatsCan", "Workstats")


def get_province_data(_province: str):
    return dta.execute_select_query("StatsCan", "Workstats", params={'prov_name': _province})


def get_data_per_lfs_code(_lfs_code: str):
    return dta.execute_select_query("StatsCan", "Workstats", params={'lfsstat': _lfs_code})
