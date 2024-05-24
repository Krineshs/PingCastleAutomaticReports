import pandas as pd

pd.options.mode.chained_assignment = None

#Function to filter computers based on the input csv specifically the True values within colums IsCurrentUserAllowed and IsEveryoneAllowed
def filter_computers(prev_report_path, new_report_path, output_path):
    #columnsa = pd.read_csv(prev_report_path, sep="\t")
    columnsb = pd.read_csv(new_report_path, sep="\t")

    filtered_data = columnsb[(columnsb['IsCurrentUserAllowed'] == True) | (columnsb['IsEveryoneAllowed'] == True)][['Computer', 'Share', 'IsCurrentUserAllowed', 'IsEveryoneAllowed']]
    filtered_data.to_csv(output_path, index=False)
