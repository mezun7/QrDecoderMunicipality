# QrDecoderMunicipality

## Installation

You should install CV4.

MAC: https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/

Ubuntu: https://www.pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/

Other requirements are Python-based. They are located in file requirements.txt

#### config.json
Sample file:

    {
  
        "originals": "/Users/shuhrat/PycharmProjects/pythonProject/originals",
        "result_path": "/Users/shuhrat/PycharmProjects/pythonProject/result",
        "working_dir": "/Users/shuhrat/PycharmProjects/pythonProject/work_dir",
        "allowed_ext": ["png", "jpg", "jpeg"]

    }
Originals - folder of original files;

Result_path - where result will be saved;

Working_dir - tmp files will be stored in this folder;

allowed_ext - Extensions that are allowed to process;