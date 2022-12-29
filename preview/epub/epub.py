# based on https://github.com/futurepress/epub.js


SCRIPT_INFO = {
    "name": "epub",
    "type": 0,
    "extensions": ["epub"],
    "arguments": ["${input_file}", "${output_file}.html", "*SEER_NO_CACHE*"],
    "version": "1.0.0",
}

# replace jszip-3.10.1.min.js
# replace main.css
# replace epub-0.3.93.min.js
# replace ${input_file}
# save file as ${output_file}
if __name__ == "__main__":
    pass