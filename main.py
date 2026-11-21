import dataset_generator as dg
import crud_operations as crud
import analytics_engine as ae
from tabulate import tabulate

def main():
    dg.create_dataset()
    while True:
        menu_rows = [
            ["1", "Display"],
            ["2", "Add"],
            ["3", "Search"],
            ["4", "Update"],
            ["5", "Delete"],
            ["6", "DataStructures"],
            ["7", "NumPy"],
            ["8", "PandasReport"],
            ["9", "Exit"]
        ]
        print()
        print(tabulate(menu_rows, headers=["Choice", "Operation"], tablefmt="grid"))
        ch = input("Choice: ").strip()
        if ch == "1": crud.display_all()
        elif ch == "2": crud.add_record()
        elif ch == "3": crud.search_record()
        elif ch == "4": crud.update_record()
        elif ch == "5": crud.delete_record()
        
        elif ch == "6": ae.data_structures_demo()
        elif ch == "7": ae.numpy_analysis()
        elif ch == "8": ae.pandas_report()
        elif ch == "9": break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()