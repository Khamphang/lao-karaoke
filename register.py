import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

# ---- Firebase Init ----
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://tbw-sys-1-test-karaoke-project-default-rtdb.asia-southeast1.firebasedatabase.app"
    })

# ---- Page Config ----
st.set_page_config(
    page_title="TBW System 1 Test — ຂໍເພງ 🎤",
    page_icon="🎤",
    layout="centered"
)

# ---- Header ----
st.markdown("## 🎉 ສະບາຍດີປີໃໝ່ລາວ 2026")
st.markdown("### 🎤 ຂໍເພງ Karaoke")
st.divider()

# ---- Form ----
with st.form("request_form", clear_on_submit=True):
    name = st.text_input("ຊື່ຂອງທ່ານ", max_chars=20, placeholder="ໃສ່ຊື່...")
    song = st.text_input("ຊື່ເພງ", max_chars=50, placeholder="ໃສ່ຊື່ເພງ...")
    artist = st.text_input("ຊື່ນັກຮ້ອງ (ທາງເລືອກ)", max_chars=30, placeholder="ໃສ່ຊື່ນັກຮ້ອງ...")
    submitted = st.form_submit_button("📩 ສົ່ງຄຳຂໍ", use_container_width=True)

if submitted:
    if not name.strip() or not song.strip():
        st.error("ກະລຸນາໃສ່ຊື່ ແລະ ຊື່ເພງ")
    else:
        try:
            db.reference("/queue").push({
                "name": name.strip(),
                "song": song.strip(),
                "artist": artist.strip() if artist.strip() else "-"
            })
            st.success(f"✅ ໄດ້ຮັບຄຳຂໍຂອງ **{name}** ແລ້ວ!")
            st.info(f"🎵 ເພງ: {song}")
        except Exception as e:
            st.error(f"ເກີດຂໍ້ຜິດພາດ: {e}")

st.divider()
st.caption("🌸 ສຸ່ຂ ສັນ ວັນ ປີໃໝ່ລາວ 2026 🌸")
