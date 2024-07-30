
# Car Files Organizer

This Python script organizes car-related files into structured `data` and `stream` directories based on the `.ytd` files found in a specified main folder. It also identifies any subfolders that do not contain the required files.

## Features

- Recursively scans a main folder for `.ytd` files and creates corresponding subfolders in the `data` and `stream` directories.
- Copies `.yft` and `.ytd` files into their respective subdirectories within the `stream` folder.
- Copies `.meta` files, and files named `carvariations`, `carcols`, `handling`, or `vehicles` into their respective subdirectories within the `data` folder.
- Logs initial subfolders that do not contain any of the required files to a `problematic_folders.txt` file.

## Usage

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/car-files-organizer.git
   cd car-files-organizer
   ```

2. **Ensure you have Python 3 installed**. You can download it from [python.org](https://www.python.org/).

3. **Run the script**:
   ```sh
   python organizecarfiles.py
   ```

4. **Enter the path to the main folder** when prompted. The script will process the files and create the necessary directory structure.

## Example

Before running the script:
```
main_folder/
├── subfolder1/
│   ├── file1.ytd
│   ├── file2.yft
│   ├── file3.meta
│   ├── carvariations.meta
├── subfolder2/
│   ├── ...
```

After running the script:
```
main_folder/
├── data/
│   ├── file1/
│   │   ├── file3.meta
│   │   ├── carvariations.meta
├── stream/
│   ├── file1/
│   │   ├── file1.ytd
│   │   ├── file2.yft
├── problematic_folders.txt
```

The `problematic_folders.txt` file will contain a list of initial subfolders that did not contain any `.ytd`, `.yft`, `.meta`, or specified named files.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the GNU License. See the `LICENSE` file for details.
