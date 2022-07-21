import os 
import shutil

from pprint import pprint


folders = []
base_dir = os.path.dirname(os.path.realpath(__file__))


def get_directory_list():
    global folders
    global base_dir

    for root, d_names, f_names in os.walk(base_dir):
        for name in d_names:
            folders.append(os.path.join(root, name))
    folders = sorted(folders)
    
    return folders


def delete_pycache():
    global folders 

    for folder in folders:
        if folder.endswith("__pycache__"):
            shutil.rmtree(folder)

    print("All __pycache__ files deleted.")
    return None


def delete_migrations():
    global folders

    for folder in folders:
        if folder.endswith("migrations"):
            for item in os.listdir(folder):
                if not item.endswith("__init__.py"):
                    os.remove(os.path.join(folder, item))

    print("All migration files deleted.")
    return None


def delete_sqlite3():
    global base_dir
    
    db_file = os.path.join(base_dir, "db.sqlite3")
    
    if os.path.exists(db_file):
        os.remove(db_file)
    
    print("db.sqlite3 deleted.")
    return None


def main():
    global folders

    try: 
        get_directory_list()
        delete_pycache()
        delete_migrations()
        delete_sqlite3()
        print("All operations performed successfully.")
        
    except Exception as e:
        print("There was some error")


if __name__ == "__main__":
    main()  