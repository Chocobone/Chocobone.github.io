import os
import re
import urllib.parse

# Directory containing your notes
notes_dir = '_notes'
image_assets_path = '/assets/images/'

# Regex for Obsidian image wikilinks: ![[image.png]] or ![[image.png|300]]
image_regex = re.compile(r'!\[\[([^\]|]+\.(png|jpg|jpeg|gif|svg|webp))(\|([^\]]+))?\]\]', re.IGNORECASE)

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_image(match):
        filename = match.group(1)
        width = match.group(4)

        # URL-encode the filename but keep slashes if any (though usually just filename)
        encoded_filename = urllib.parse.quote(filename.strip())
        # Replace %2F back to / in case there are subdirectories (though unusual in Obsidian)
        encoded_filename = encoded_filename.replace('%2F', '/')

        img_src = f"{image_assets_path}{encoded_filename}"
        img_attr = f" width='{width}'" if width else ""
        return f"<img src='{img_src}' alt='{filename}'{img_attr} class='internal-image' />"

    new_content = image_regex.sub(replace_image, content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

def main():
    for root, dirs, files in os.walk(notes_dir):
        for file in files:
            if file.endswith('.md'):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
