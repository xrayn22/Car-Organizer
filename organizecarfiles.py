import os
import shutil

def organize_car_files(main_folder):
    data_folder = os.path.join(main_folder, 'data')
    stream_folder = os.path.join(main_folder, 'stream')
    
    # Create data and stream folders if they don't exist
    os.makedirs(data_folder, exist_ok=True)
    os.makedirs(stream_folder, exist_ok=True)
    
    ytd_folders = {}
    initial_subfolders = {os.path.join(main_folder, d): True for d in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, d))}
    
    # First pass: Identify all .ytd files and create their respective folders
    for root, dirs, files in os.walk(main_folder):
        found_ytd = False
        for file in files:
            if file.endswith('.ytd'):
                ytd_name = os.path.splitext(file)[0]
                
                ytd_data_folder = os.path.join(data_folder, ytd_name)
                ytd_stream_folder = os.path.join(stream_folder, ytd_name)
                os.makedirs(ytd_data_folder, exist_ok=True)
                os.makedirs(ytd_stream_folder, exist_ok=True)
                
                ytd_folders[ytd_name] = (ytd_data_folder, ytd_stream_folder)
                found_ytd = True
                # Mark the initial subfolder as containing needed files
                for initial_subfolder in initial_subfolders:
                    if root.startswith(initial_subfolder):
                        initial_subfolders[initial_subfolder] = False
                        break

    # Second pass: Copy relevant files to their respective folders
    for root, dirs, files in os.walk(main_folder):
        for f in files:
            src_path = os.path.join(root, f)
            
            if f.endswith('.yft') or f.endswith('.ytd'):
                ytd_name = os.path.splitext(f)[0]
                if ytd_name in ytd_folders:
                    dest_path = os.path.join(ytd_folders[ytd_name][1], f)
                    if src_path != dest_path:
                        shutil.copy2(src_path, dest_path)
                        print(f"Copied {src_path} to {dest_path}")

            if f.endswith('.meta') or f.startswith(('carvariations', 'carcols', 'handling', 'vehicles')):
                # Find the closest .ytd file in the hierarchy
                closest_ytd = None
                current_root = root
                while current_root != main_folder:
                    current_root = os.path.dirname(current_root)
                    for r, d, files in os.walk(current_root):
                        for file in files:
                            if file.endswith('.ytd'):
                                ytd_name = os.path.splitext(file)[0]
                                if ytd_name in ytd_folders:
                                    closest_ytd = ytd_name
                                    break
                        if closest_ytd:
                            break
                    if closest_ytd:
                        break
                
                if closest_ytd:
                    dest_path = os.path.join(ytd_folders[closest_ytd][0], f)
                    if src_path != dest_path:
                        shutil.copy2(src_path, dest_path)
                        print(f"Copied {src_path} to {dest_path}")
                        # Mark the initial subfolder as containing needed files
                        for initial_subfolder in initial_subfolders:
                            if root.startswith(initial_subfolder):
                                initial_subfolders[initial_subfolder] = False
                                break

    # Write initial subfolders that didn't have any required files to a text file
    with open(os.path.join(main_folder, 'problematic_folders.txt'), 'w') as f:
        for folder, is_problematic in initial_subfolders.items():
            if is_problematic:
                f.write(folder + '\n')
        print(f"Wrote problematic folders to {f.name}")

if __name__ == "__main__":
    main_folder = input("Enter the path to the main folder: ")
    organize_car_files(main_folder)
