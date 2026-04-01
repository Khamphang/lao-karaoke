import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from streamlit_autorefresh import st_autorefresh

# ---- Firebase Init ----
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://tbw-sys-1-test-karaoke-project-default-rtdb.asia-southeast1.firebasedatabase.app"
    })

# ---- Page Config ----
st.set_page_config(
    page_title="TBW System 1 Test — Karaoke Queue 🎤",
    page_icon="🎤",
    layout="wide"
)

# Auto-refresh ທຸກ 10 ວິນາທີ
st_autorefresh(interval=10000)

# ---- Load Queue from Firebase ----
def get_queue():
    data = db.reference("/queue").get()
    if not data:
        return []
    items = []
    for key, val in data.items():
        items.append({"key": key, **val})
    return items

def remove_first(queue):
    if queue:
        db.reference(f"/queue/{queue[0]['key']}").delete()

# ---- UI ----
st.markdown(
    "<h1 style='text-align:center; color:#FFD700;'>🎉 Karaoke ປີໃໝ່ລາວ 2026 🎉</h1>",
    unsafe_allow_html=True
)
st.divider()

queue = get_queue()

if not queue:
    st.markdown(
        "<h2 style='text-align:center; color:#FFD700;'>ຍັງບໍ່ມີຄຳຂໍ — ສົ່ງຄຳຂໍເພງໄດ້ເລີຍ! 🎤</h2>",
        unsafe_allow_html=True
    )
else:
    # ---- ກຳລັງຮ້ອງ ----
    current = queue[0]
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(
            f"<div style='background:#2d0000; padding:30px; border-radius:15px; border:2px solid #FFD700;'>"
            f"<h2 style='color:#FFD700;'>✨ ກຳລັງຮ້ອງ</h2>"
            f"<h1 style='color:white;'>🎤 {current['name']}</h1>"
            f"<h2 style='color:#FFD700;'>🎵 {current['song']}</h2>"
            f"<p style='color:#ccc;'>ນັກຮ້ອງ: {current.get('artist', '-')}</p>"
            f"</div>",
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            "<div style='background:#1a0000; padding:20px; border-radius:15px; border:1px solid #FFD700;'>"
            "<h3 style='color:#FFD700;'>📋 ລໍຖ້ານຳ</h3>",
            unsafe_allow_html=True
        )
        if len(queue) > 1:
            for i, item in enumerate(queue[1:], start=1):
                st.markdown(
                    f"<p style='color:white;'>{i}. <b>{item['name']}</b> — {item['song']}</p>",
                    unsafe_allow_html=True
                )
        else:
            st.markdown("<p style='color:#888;'>ບໍ່ມີຄຳຂໍຕໍ່ໄປ</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # ---- Admin: ໂດດໜ້າ ----
    if st.button("⏭ ຈົບເພງ / ໂດດໜ້າ", use_container_width=True):
        remove_first(queue)
        st.rerun()

st.divider()
st.caption("🌸 ສຸ່ຂ ສັນ ວັນ ປີໃໝ່ລາວ 2026 — refresh ທຸກ 10 ວິ 🌸")
