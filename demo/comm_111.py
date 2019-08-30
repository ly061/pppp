data_lan = [{"Language": "en", "Lanid": "en-GB"},
            {"Language": "zh-cn", "Lanid": "zh-CN"},
            {"Language": "zh", "Lanid": "zh-TW"},
            {"Language": "ja", "Lanid": "ja-JP"},
            {"Language": "fr", "Lanid": "fr-FR"},
            {"Language": "kr", "Lanid": "ko-KR"},
            {"Language": "es", "Lanid": "es-ES"},
            {"Language": "pt", "Lanid": "pt-PT"},
            {"Language": "ar", "Lanid": "ar-EG"}]

# def get_lan_id(language_input):
#     for lan_num in range(len(data_lan)):
#         if data_lan[lan_num]["Language"] == language_input:
#             id = data_lan[lan_num]["Lanid"]
#             print(id)

# get_lan_id("es")

def get_id(language_input):
    for data_son in data_lan:
        if  language_input == data_son.get("language"):
            id = data_son.get("Lanid")
            print(id)
get_id("es")

