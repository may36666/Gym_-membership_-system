import face_recognition
import json

# 會員圖片文件名
member_images = ["Qixuan.jpg"]

# 會員信息
members_data = {"members": []}
member_info = [
    {"name": "Qixuan", "member": True}
]
# 處理每張會員圖片並獲取臉部特徵編碼
for i, image_name in enumerate(member_images):
    # 載入圖片文件
    image = face_recognition.load_image_file(image_name)
    
    # 假設每張圖片只包含一張臉
    face_encoding = face_recognition.face_encodings(image)[0]
    
    # 添加臉部特徵編碼到會員信息
    member_info[i]["encoding"] = face_encoding.tolist()

# 添加會員信息到會員資料
members_data["members"] = member_info

# 保存資料到JSON文件
json_file_path = "members.json"
with open(json_file_path, 'w') as json_file:
    json.dump(members_data, json_file)

print(f"會員資料已保存到 {json_file_path}")
