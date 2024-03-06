import os
import shutil
import concurrent.futures

def organize_files(src_folder):
    def move_file(file, file_type):
        try:
            destination_path = os.path.join(src_folder, file_type)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            shutil.move(os.path.join(src_folder, file), os.path.join(destination_path, file))
        except Exception as e:
            print(f"Error moving {file}: {str(e)}")

    def categorize_file(file):
        file_extension = file.split('.')[-1].lower()
        categories = {
            "video": ["mp4", "avi", "mkv", "mov"],
            "audio": ["mp3", "wav", "flac", "ogg", "amr"],
            "documents": ["docx", "xlsx", "pptx", "pdf", "txt", "doc"],
            "images": ["jpg", "jpeg", "png", "bmp", "gif"]
            
        }

        for category, extensions in categories.items():
            if file_extension in extensions:
                move_file(file, category)
                return

        # Для невідомих розширень
        move_file(file, 'other')

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for root, _, files in os.walk(src_folder, topdown=False):
            for file in files:
                executor.submit(categorize_file, file)

    
    for root, dirs, _ in os.walk(src_folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

if __name__ == "__main__":
    source_folder = input("Введіть шлях до папки 'Хлам': ")
    organize_files(source_folder)
