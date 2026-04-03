# 🎤 Lao New Year Karaoke Queue

ລະບົບຂໍເພງ Karaoke ສຳລັບງານບຸນປີໃໝ່ລາວ 2026

## ໂຄງສ້າງ

```
guest (mobile) ──► register.py ──► Firebase ──► song_queue.py (TV)
```

## ການ Setup (4 ຂັ້ນຕອນ)

### 1. Firebase Setup
1. ໄປທີ່ https://console.firebase.google.com
2. Create project ໃໝ່ (ຊື່: `lao-karaoke`)
3. ໄປທີ່ **Realtime Database** → Create database → Start in test mode
4. ໄປທີ່ **Project Settings** → **Service accounts** → Generate new private key
5. Download ໄຟລ໌ JSON → rename ເປັນ `firebase_key.json` → ວາງໃນ folder ນີ້

### 2. ແກ້ Database URL
ເປີດ `register.py` ແລະ `song_queue.py` — ແກ້ບ່ອນນີ້:
```python
"databaseURL": "https://YOUR_PROJECT_ID-default-rtdb.firebaseio.com"
```
ປ່ຽນ `YOUR_PROJECT_ID` ເປັນ ID ຂອງ project ທ່ານ (ເຫັນໃນ Firebase console)

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Local
```bash
# ໜ້າ TV (ເປີດໃນ browser ຕໍ່ TV)
streamlit run song_queue.py --server.port 8501

# ໜ້າ mobile (ເປີດ port ອື່ນ)
streamlit run register.py --server.port 8502
```

## Deploy ຂຶ້ນ Cloud (ຟຣີ)

1. Push code ຂຶ້ນ GitHub (ຢ່າ push `firebase_key.json`!)
2. ໄປທີ່ https://share.streamlit.io
3. Connect GitHub repo
4. Deploy `register.py` → ໄດ້ URL ສຳລັບ guest
5. Deploy `song_queue.py` → ໄດ້ URL ສຳລັບ TV
6. ໃນ Streamlit Cloud: Settings → Secrets → ໃສ່ firebase credentials

## ການໃຊ້ງານໃນງານ

1. ເປີດ `song_queue.py` ໃນ TV/projector (fullscreen F11)
2. ສ້າງ QR code ຈາກ URL ຂອງ `register.py`
3. ພິມ QR code / ສະແດງໃນໜ້າ TV
4. Guest scan QR → ເລືອກເພງ → ຂຶ້ນ queue ທັນທີ
5. ກົດ "ຈົບເພງ / ໂດດໜ້າ" ເມື່ອຮ້ອງຈົບ

## ໄຟລ໌
| ໄຟລ໌ | ຈຸດປະສົງ |
|------|---------|
| `register.py` | ໜ້າ mobile — ຂໍເພງ |
| `song_queue.py` | ໜ້າ TV — ສະແດງ queue |
| `firebase_key.json` | Firebase credentials (ຢ່າ share!) |
| `requirements.txt` | Python dependencies |
| `.streamlit/config.toml` | Theme ສີທອງ-ແດງ |

---

## Credits & Inspiration

This project was inspired by and studied from:

- **[Streamlit + Firebase Karaoke Event App](https://github.com/WindJammer6/18.-Deployed-Streamlit-Python-and-Firebase-Web-Application-Project-for-a-Karaoke-Event)**
  by [WindJammer6](https://github.com/WindJammer6)
  — Architecture concept: Streamlit form → Firebase Realtime DB → Queue display

- **[Firebase Realtime Database](https://firebase.google.com/docs/database)**
  by Google — Real-time data sync backend

- **[Streamlit](https://streamlit.io)** — Python web app framework

> Built as part of **TBW System 1** learning test project by [Khamphang](https://github.com/Khamphang)
