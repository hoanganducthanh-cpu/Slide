import streamlit as st
from PIL import Image
import os
import base64
import io
from datetime import datetime

# ===================== CẤU HÌNH =====================
st.set_page_config(
    page_title="Đào tạo PCCC - Nhà máy Điện gió Yang Trung",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

LOGO_PATH = "images/Horizontal_logo_pese_1.png"
BG_PATH = "images/trang_trai_gio.jpg"


@st.cache_data
def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return ""


@st.cache_data
def load_image(path):
    if os.path.exists(path):
        return Image.open(path)
    return None


# ===================== CSS =====================
st.markdown("""
<style>
    .main { background: #ffffff; }
    .block-container { padding: 0.5rem 1rem 2rem 1rem; max-width: 1400px; }

    /* ================= HEADER MỚI (nền trắng + viền đỏ, giống ảnh mẫu) ================= */
    .header-wrap {
        background: #ffffff;
        border-top: 4px solid #1a237e;
        border-bottom: 4px solid #1a237e;
        padding: 12px 24px;
        margin-bottom: 0;
        position: relative;
        box-shadow: 0 2px 6px rgba(0,0,0,.08);
    }
    .header-logo-box {
        display: inline-block;
        vertical-align: middle;
        width: 130px;
    }
    .header-logo-box img {
        height: 55px;
        vertical-align: middle;
    }
    .header-text-box {
        display: inline-block;
        vertical-align: middle;
        padding-left: 20px;
        width: calc(100% - 200px);
        text-align: center;
    }
    .header-text-box .company {
        font-size: 22px;
        font-weight: 800;
        color: #1a237e;
        letter-spacing: .5px;
        line-height: 1.3;
    }
    .header-text-box .center {
        font-size: 18px;
        font-weight: 700;
        color: #CC0000;
        letter-spacing: .5px;
        margin-top: 4px;
    }
    .header-slide-no {
        display: inline-block;
        vertical-align: middle;
        width: 60px;
        text-align: right;
        font-size: 12px;
        font-weight: 600;
        color: #999;
    }

    /* ================= TIÊU ĐỀ SLIDE (nền đỏ, chữ trắng) ================= */
    .slide-title-bar {
        background: linear-gradient(135deg, #cc0000, #990000);
        color: #ffffff;
        padding: 12px 22px;
        font-size: 17px;
        font-weight: 700;
        margin: 14px 0 16px 0;
        border-radius: 6px;
        letter-spacing: .3px;
        box-shadow: 0 3px 8px rgba(204,0,0,.2);
    }

    /* ================= COVER ================= */
    .cover-wrapper {
        border-radius: 10px;
        overflow: hidden;
        min-height: 620px;
        box-shadow: 0 10px 40px rgba(0,0,0,.3);
    }
    .cover-left {
        display: inline-block;
        vertical-align: top;
        width: 58%;
        background: linear-gradient(135deg, #8B0000 0%, #A00000 50%, #C00000 100%);
        color: #fff;
        padding: 40px 45px;
        box-sizing: border-box;
        min-height: 620px;
        position: relative;
    }
    .cover-left .logo {
        position: absolute;
        top: 25px;
        left: 35px;
        height: 55px;
    }
    .cover-left .top-line {
        width: 100%;
        height: 1px;
        background: rgba(255,255,255,.25);
        margin: 55px 0 22px 0;
    }
    .cover-left h1 {
        font-size: 42px;
        font-weight: 900;
        line-height: 1.12;
        letter-spacing: 1px;
        color: #fff;
        margin: 0;
    }
    .cover-left .sub {
        font-size: 19px;
        font-weight: 700;
        color: #ffd700;
        margin-top: 14px;
        letter-spacing: 2px;
        line-height: 1.3;
    }
    .cover-left .divider {
        width: 100%;
        height: 1px;
        background: rgba(255,255,255,.3);
        margin: 20px 0;
    }
    .cover-left .company {
        font-size: 14px;
        font-weight: 600;
        color: #fff;
        line-height: 1.5;
        margin-bottom: 6px;
    }
    .cover-left .center {
        font-size: 13px;
        color: rgba(255,255,255,.85);
        line-height: 1.5;
        margin-bottom: 22px;
    }
    .cover-left .info {
        font-size: 13px;
        color: #fff;
        line-height: 2;
    }
    .cover-right {
        display: inline-block;
        vertical-align: top;
        width: 42%;
        min-height: 620px;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        box-sizing: border-box;
        position: relative;
    }
    .cover-right::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(90deg, rgba(139,0,0,.5) 0%, transparent 30%);
        pointer-events: none;
    }

    /* ================= SECTION ================= */
    .section {
        background: linear-gradient(135deg, #800020, #cc0000);
        padding: 80px 40px;
        border-radius: 10px;
        text-align: center;
        color: #fff;
        min-height: 420px;
    }
    .section h2 { font-size: 40px; font-weight: 800; letter-spacing: 2px; }
    .section .sub { font-size: 22px; color: #fff; font-weight: 300; letter-spacing: 2px; margin-top: 12px; }
    .section p { font-size: 15px; color: rgba(255,255,255,.85); margin-top: 16px; max-width: 700px; margin-left: auto; margin-right: auto; }

    /* ================= CLOSING ================= */
    .closing {
        background: linear-gradient(135deg, #CC0000, #D32F2F);
        padding: 80px 40px;
        border-radius: 10px;
        text-align: center;
        color: #fff;
        min-height: 420px;
    }
    .closing h2 { font-size: 42px; font-weight: 800; }

    /* ================= CARD ================= */
    .card {
        background: #F5F5F5;
        border-left: 4px solid #CC0000;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 14px;
        color: #333;
    }
    .kpi {
        background: #F5F5F5;
        border-left: 4px solid #CC0000;
        border-radius: 8px;
        padding: 14px;
        text-align: center;
    }
    .kpi .v { font-size: 20px; font-weight: 700; color: #CC0000; }
    .kpi .l { font-size: 12px; color: #666; }

    .pass-card {
        background: #F5F5F5;
        border-radius: 10px;
        padding: 20px 10px;
        text-align: center;
    }
    .pass-card .lt {
        width: 50px; height: 50px;
        background: #CC0000; color: #fff;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 24px; font-weight: 800;
        margin: 0 auto 10px;
    }
    .pass-card h4 { color: #CC0000; margin: 6px 0; }
    .pass-card p { font-size: 12px; color: #333; }

    ul.cl { padding: 0; }
    ul.cl li { list-style: none; padding: 6px 0 6px 24px; position: relative; font-size: 14px; color: #333; border-bottom: 1px solid #f0f0f0; }
    ul.cl li::before { content: '✓'; position: absolute; left: 0; color: #CC0000; font-weight: 700; }

    .flow-box {
        border: 2px solid #CC0000;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 14px;
        background: #fff;
        color: #333;
    }
    .flow-box.act { background: #CC0000; color: #fff; }

    .dots-wrap { display: flex; justify-content: center; gap: 6px; padding: 12px 0 4px 0; flex-wrap: wrap; }
    .dot { width: 9px; height: 9px; border-radius: 50%; background: rgba(204,0,0,.25); display: inline-block; }
    .dot.active { background: #CC0000; transform: scale(1.4); box-shadow: 0 0 8px rgba(204,0,0,.5); }
</style>
""", unsafe_allow_html=True)


# ===================== DỮ LIỆU SLIDES =====================
SLIDES = [
    {"type": "cover",
     "title": "ĐÀO TẠO PHÒNG CHÁY CHỮA CHÁY",
     "subtitle": "NHÀ MÁY ĐIỆN GIÓ YANG TRUNG – CHƠ LONG",
     "lines": [
        "CÔNG TY TNHH DỊCH VỤ VÀ KỸ THUẬT NĂNG LƯỢNG PECC2",
        "TRUNG TÂM QUẢN LÝ VẬN HÀNH NHÀ MÁY ĐIỆN",
        "Người trình bày: Trương Hoàng An  |  Mã quy trình: CLWP-QT-07",
     ]},
    {"type": "toc", "title": "MỤC LỤC – KẾT CẤU CHƯƠNG TRÌNH ĐÀO TẠO",
     "items": [
        ("A", "Nền tảng về cháy & khung pháp lý PCCC", "Khái niệm sự cháy, điều kiện, nguyên nhân, quy định pháp luật, hồ sơ PCCC"),
        ("B", "Hệ thống PCCC tại nhà máy", "Báo cháy Hochiki L@titude, chữa cháy nước/FM-200/phun sương"),
        ("C", "Quy trình kiểm tra, vận hành & bảo trì", "Kiểm tra định kỳ, thao tác tủ báo cháy, bảo dưỡng thiết bị"),
        ("D", "Ứng phó khẩn cấp & xử lý sự cố", "Quy trình chữa cháy, PASS, vận hành FM-200, kỹ năng thoát hiểm"),
     ]},
    {"type": "section", "title": "PHẦN A",
     "subtitle": "NỀN TẢNG VỀ CHÁY & KHUNG PHÁP LÝ PCCC",
     "lines": ["Hiểu bản chất sự cháy, quy định pháp luật và trách nhiệm PCCC — nền tảng để vận hành đúng hệ thống thiết bị của nhà máy."]},
    {"type": "cards", "title": "PCCC – TẠI SAO CẦN THIẾT?", "cols": 3,
     "items": [
        ("🛡️", "Bảo vệ tính mạng & tài sản", "Nhà máy điện có nguy cơ cháy nổ cao (điện, pin, dầu MBA)."),
        ("⚡", "Đảm bảo ổn định điện", "Nhà máy cung cấp năng lượng tái tạo quốc gia."),
        ("📋", "Yêu cầu pháp lý", "Luật PCCC & CNCH, NĐ 105/2025, TT 36/2025, QCVN 10:2025."),
     ]},
    {"type": "cards", "title": "KHÁI NIỆM VỀ SỰ CHÁY", "cols": 3,
     "items": [
        ("📐", "Theo khoa học PCCC", "Quá trình biến đổi lý–hóa: chất cháy + chất oxy hóa + nguồn nhiệt → tỏa nhiệt, phát sáng."),
        ("⚖️", "Theo Luật PCCC", "Phản ứng hóa học có tỏa nhiệt, phát ánh sáng hoặc khói, gây thiệt hại."),
        ("⚗️", "Bản chất", "Phản ứng hóa học – Tỏa nhiệt – Phát sáng."),
     ]},
    {"type": "table", "title": "BA YẾU TỐ CẦN THIẾT CHO SỰ CHÁY",
     "headers": ["Yếu tố", "Khái niệm", "Ví dụ tại nhà máy"],
     "rows": [
        ["🔥 Chất cháy", "Chất phản ứng với oxy hóa", "Cáp điện, dầu MBA, pin lưu trữ"],
        ["⚡ Nguồn nhiệt", "Nguồn cung cấp năng lượng", "Chập mạch, quá tải, ma sát, sét"],
        ["🌬️ Chất oxy hóa", "Chất tham gia phản ứng", "Oxy trong không khí (~21%)"],
     ]},
    {"type": "list", "title": "BỐN ĐIỀU KIỆN CẦN THIẾT CHO SỰ CHÁY",
     "lines": [
        "**1. Tiếp xúc trực tiếp** – Chất cháy, chất oxy hóa, nguồn nhiệt phải tiếp xúc.",
        "**2. Thời gian tiếp xúc đủ lớn** – Đủ thời gian để phản ứng cháy xảy ra.",
        "**3. Nồng độ trong giới hạn bắt cháy** – Nồng độ chất cháy & oxy hóa nằm trong vùng bắt cháy.",
        "**4. Đạt nhiệt độ tự bắt cháy** – Nguồn nhiệt nung nóng hỗn hợp tới nhiệt độ tự bắt cháy.",
        "→ Chỉ cần loại bỏ **MỘT** trong 4 điều kiện là ngăn được cháy.",
     ]},
    {"type": "cards", "title": "NGUYÊN NHÂN CHÁY", "cols": 3,
     "items": [
        ("🌩️", "Tự nhiên", "Sét đánh, tự cháy vật liệu."),
        ("⚡", "Sự cố bất ngờ", "Ngắn mạch, quá tải, hỏng thiết bị."),
        ("😕", "Vô ý", "Thiếu hiểu biết, sai thao tác."),
        ("🚫", "Vi phạm quy định", "Hàn cắt, thắp hương sai nơi."),
        ("🔴", "Cố ý", "Phá hoại, che giấu tội phạm."),
        ("❓", "Nguyên nhân khác", "Tai nạn, bất khả kháng."),
     ]},
    {"type": "table", "title": "NGUY CƠ CHÁY ĐẶC THÙ TẠI NHÀ MÁY ĐIỆN GIÓ",
     "headers": ["Khu vực", "Nguy cơ cháy chính", "Nguồn nhiệt điển hình"],
     "rows": [
        ["Trạm biến áp 22kV", "Dầu cách điện MBA, cáp trung thế", "Chập mạch, quá tải, phóng điện"],
        ["Phòng Pin/Accu", "Cháy hóa chất pin lưu trữ", "Quá nhiệt pin, chập mạch nội bộ"],
        ["Phòng Datacenter/điều khiển", "Cháy thiết bị điện tử", "Quá tải, chập mạch bo mạch"],
        ["Tuabin gió (nacelle)", "Cháy dầu bôi trơn, hộp số", "Ma sát cơ khí, sét đánh"],
     ]},
    {"type": "two-col", "title": "PHẠM VI ÁP DỤNG & ĐỐI TƯỢNG",
     "left_title": "📍 Phạm vi áp dụng",
     "left_lines": [
        "Toàn bộ Nhà máy Điện Gió Yang Trung – Chơ Long",
        "Mã quy trình: CLWP-QT-07",
        "Tất cả khu vực văn phòng, nhà xưởng, trạm BA, tuabin",
     ],
     "right_title": "👤 Đối tượng áp dụng",
     "right_lines": [
        "Cán bộ quản lý nhà máy",
        "Kỹ thuật vận hành",
        "Vận hành viên các ca",
        "Nhân viên bảo vệ",
     ],
     "note": "**Chỉ huy chữa cháy:** Người đứng đầu → Đội trưởng PCCC → Trưởng ca"},
    {"type": "cards", "title": "HỒ SƠ QUẢN LÝ PCCC CỦA NHÀ MÁY", "cols": 3,
     "items": [
        ("📄", "PC01", "Thông tin cơ sở"),
        ("📜", "Nội quy PCCC", "Quyết định & nội quy"),
        ("📐", "Thẩm duyệt", "Thiết kế PCCC"),
        ("👨‍🚒", "Đội PCCC", "Thành lập đội"),
        ("📋", "PC06", "Chữa cháy, CNCH"),
        ("🧯", "Sổ PT", "Xuất nhập, bảo dưỡng"),
        ("📊", "Nghiệm thu", "Kiểm định TB"),
        ("🎓", "CN huấn luyện", "Đã qua đào tạo"),
        ("📎", "Khác", "Bản vẽ, BH..."),
     ]},
    {"type": "two-col", "title": "TRÁCH NHIỆM & CHẾ ĐỘ KIỂM TRA PCCC",
     "left_title": "🔄 Thường xuyên",
     "left_lines": ["Không quá 1 tháng/lần", "Duy trì an toàn nguồn lửa/nhiệt", "Phương tiện PCCC, lối thoát nạn"],
     "right_title": "📅 Định kỳ",
     "right_lines": ["6 tháng hoặc 1 năm tùy phân loại", "Biên bản Mẫu PC02"],
     "note": "**Trách nhiệm hình sự:** Điều 313 BLHS – phạt tù đến 12 năm."},
    {"type": "section", "title": "PHẦN B",
     "subtitle": "HỆ THỐNG PCCC TẠI NHÀ MÁY ĐIỆN GIÓ YANG TRUNG – CHƠ LONG",
     "lines": ["Cấu trúc, thiết bị và nguyên lý hoạt động của hệ thống báo cháy & chữa cháy thực tế đang lắp đặt tại nhà máy."]},
    {"type": "two-col", "title": "TỔNG QUAN HỆ THỐNG PCCC",
     "left_title": "🔥 Hệ thống báo cháy",
     "left_lines": ["Tủ Hochiki L@titude (2 loop)", "Đầu báo khói/nhiệt, module địa chỉ", "Chuông còi đèn cảnh báo"],
     "right_title": "💧 Hệ thống chữa cháy",
     "right_lines": ["Bơm chữa cháy 75kW", "Tủ HCVR-3 FM-200", "Phun sương trạm BA", "Bình MFZ/ABC"],
     },
    {"type": "flow", "title": "SƠ ĐỒ KHỐI HỆ THỐNG PCCC",
     "rows": [
        ["Phát hiện cháy", "Báo cháy trung tâm", "Cảnh báo sơ tán"],
        ["Kích hoạt chữa cháy", "Bơm / FM-200 / Phun sương", "Kiểm soát đám cháy"],
     ]},
    {"type": "list", "title": "NGUYÊN LÝ HOẠT ĐỘNG BÁO CHÁY",
     "lines": [
        "🔍 Đầu báo khói/nhiệt phát hiện dấu hiệu cháy",
        "📡 Tín hiệu truyền về trung tâm Hochiki L@titude",
        "🔔 Kích hoạt chuông, còi, đèn cảnh báo",
        "🖥️ Hiển thị vị trí cháy trên màn hình tủ báo",
     ]},
    {"type": "cards", "title": "CÁC THÀNH PHẦN HỆ THỐNG BÁO CHÁY", "cols": 4,
     "items": [
        ("🔍", "Đầu báo", "Khói quang, khói địa chỉ, nhiệt"),
        ("🔌", "Module", "CZM, SOM, DIMM, R2ML, SCI"),
        ("💻", "Trung tâm", "L@titude LA303H1-10"),
        ("🔔", "Cảnh báo", "Chuông, còi, đèn, nút nhấn"),
     ]},
    {"type": "table", "title": "PHÂN LOẠI ĐẦU BÁO CHÁY",
     "headers": ["Loại đầu báo", "Nguyên lý", "Ứng dụng", "Đặc điểm"],
     "rows": [
        ["Khói quang thường", "Tán xạ ánh sáng khi có khói", "Khu vực thông thường", "Giá rẻ, dễ thay thế"],
        ["Khói địa chỉ", "Tán xạ + CPU + DCP Protocol", "Hệ thống lớn", "Xác định chính xác vị trí"],
        ["Nhiệt gia tăng", "Màng đàn hồi + buồng khí", "Bếp, nhà máy, bụi ẩm", "Chống báo giả"],
        ["Nhiệt chống nổ FFH-2E120", "Cảm biến nhiệt chống cháy nổ", "Trạm BA, KV nguy hiểm", "An toàn cao"],
     ]},
    {"type": "table", "title": "SO SÁNH CONVENTIONAL vs ADDRESSABLE",
     "headers": ["Tiêu chí", "Conventional", "Addressable"],
     "rows": [
        ["Vị trí báo", "Theo zone", "Chính xác từng ID"],
        ["Giao thức", "Analog", "DCP Protocol"],
        ["Báo giả", "Có thể", "Phát hiện độ bẩn"],
        ["Môi trường", "VP, hành lang", "Bếp, xưởng, BA"],
     ]},
    {"type": "cards", "title": "CÁC MODULE TRONG HỆ THỐNG BÁO CHÁY", "cols": 5,
     "items": [
        ("🔌", "DCP-CZM", "Chuyển đầu báo thường → địa chỉ"),
        ("🔌", "DCP-SOM", "Giám sát đầu ra NAC"),
        ("🔌", "DCP-DIMM", "Giám sát đầu vào 2 kênh"),
        ("🔌", "DCP-R2ML", "Relay điều khiển"),
        ("🔌", "DCP-SCI", "Cách ly ngắn mạch Loop"),
     ]},
    {"type": "list", "title": "TỦ HOCHIKI L@TITUDE LA303H1-10",
     "lines": [
        "**2 loop** địa chỉ",
        "**Bo S721** – Xử lý trung tâm",
        "**Bo S722** – Báo cháy",
        "**Bo S769** – 4 kênh NAC",
        "**Bo S770** – Relay",
        "**Nguồn S406** – 24Vdc, sạc pin 7-60AH",
     ]},
    {"type": "two-col", "title": "VẬN HÀNH TỦ BÁO CHÁY & CÁC TRẠNG THÁI",
     "left_title": "Thao tác xem trạng thái",
     "left_lines": [
        "1. Nhấn **MENU** → ENTER",
        "2. Chọn **SYSTEM STATUS**",
        "3. Chọn **POINT STATUS**",
        "4. Xem trạng thái **LOOP**",
     ],
     "right_title": "Trạng thái hiển thị",
     "right_lines": ["✅ Bình thường", "⚠️ Sự cố (Trouble)", "🔥 Báo cháy – FIRE"]},
    {"type": "table", "title": "CÁC NÚT NHẤN TRÊN TỦ BÁO CHÁY",
     "headers": ["Nút", "Chức năng", "Trạng thái"],
     "rows": [
        ["SILENCE", "Tắt chuông báo", "FIRE / TROUBLE"],
        ["RESET", "Reset hệ thống sau xử lý", "Sau xử lý cháy"],
        ["TEST", "Kiểm tra đèn, chuông, còi", "Bảo trì"],
        ["BUZZER", "Kiểm tra còi báo", "Bảo trì"],
     ]},
    {"type": "cards", "title": "HỆ THỐNG CHỮA CHÁY – TỔNG QUAN", "cols": 3,
     "items": [
        ("💧", "Chữa cháy nước", "Bơm chính 75kW, dự phòng 75kW, Jockey"),
        ("🧯", "Khí FM-200", "Tủ HCVR-3, 3 bình, bảo vệ khu kín"),
        ("💨", "Phun sương BA", "HV14 360°, STV-NZ phun khí"),
     ]},
    {"type": "kpi", "title": "BƠM CHỮA CHÁY & CHẾ ĐỘ VẬN HÀNH",
     "kpis": [("75 kW", "Bơm chính Electric"), ("75 kW", "Bơm dự phòng Electric"), ("Jockey", "Bơm bù áp")],
     "note": "⚙️ Tự động: Tủ ECS điều khiển theo tín hiệu áp suất/báo cháy  |  ✋ Bằng tay: Start/Stop trực tiếp trên tủ bơm"},
    {"type": "list", "title": "TỦ HCVR-3 FM-200 & KHU VỰC BẢO VỆ",
     "lines": [
        "**03 bình FM-200** trong tủ van",
        "**3 khu vực bảo vệ** độc lập",
        "**42 bar** ở 21°C",
        "**Auto / Manual** van chuyển mạch",
        "Khu vực: 🏗️ Datacenter | 📦 Pin/Accu | ⚡ 22kV",
     ]},
    {"type": "two-col", "title": "BÌNH CHỮA CHÁY MFZ/ABC, CO₂ & KIỂM TRA",
     "left_title": "🧯 MFZ/ABC8 – Bột khô",
     "left_lines": ["Dập cháy A, B, C", "An toàn thiết bị điện"],
     "right_title": "🧯 Bình CO₂",
     "right_lines": ["Chữa cháy TB điện tử", "Không cặn"],
     "note": "Kiểm tra: 📊 Kim áp XANH | 🔒 Chốt an toàn | 🔍 Không móp/rỉ | 📅 Còn hạn KĐ"},
    {"type": "kpi", "title": "HỆ THỐNG PHUN SƯƠNG CAO ÁP & TRẠM BA",
     "kpis": [("90°C", "Nhiệt kích hoạt"), ("D65/D50", "Ống STK"), ("1.2m", "Khoảng cách HV14")],
     "note": "💨 Đầu HV14 phun sương 360°  |  🌊 Đầu STV-NZ phun khí 360°  |  ⚡ Bảo vệ toàn bộ trạm biến áp"},
    {"type": "table", "title": "PHÂN LOẠI ĐÁM CHÁY & CHẤT CHỮA CHÁY",
     "headers": ["Chất chữa cháy", "Loại", "Ưu/Nhược điểm"],
     "rows": [
        ["Bột MFZ/ABC", "A, B, C", "Đa năng, an toàn điện / Bẩn"],
        ["CO₂", "B, E", "Sạch, không cặn / Ngạt kín"],
        ["FM-200", "A, B, E", "Sạch, bảo vệ điện tử / Đắt"],
        ["Phun sương", "A, B, E", "Làm mát, ít hư hại / Áp cao"],
     ]},
    {"type": "cards", "title": "THIẾT BỊ PHỤ TRỢ CHỮA CHÁY", "cols": 4,
     "items": [
        ("🔌", "Họng DN65", ""), ("🧰", "Tủ chữa cháy", ""),
        ("🔧", "Cuộn vòi", ""), ("💨", "HV14/STV-NZ", ""),
     ]},
    {"type": "section", "title": "PHẦN C",
     "subtitle": "QUY TRÌNH KIỂM TRA, VẬN HÀNH & BẢO TRÌ",
     "lines": ["Áp dụng 3 phương pháp kiểm tra PCCC vào việc kiểm tra thực tế thiết bị, kết hợp lịch bảo trì định kỳ tại nhà máy."]},
    {"type": "cards", "title": "BA PHƯƠNG PHÁP KIỂM TRA PCCC", "cols": 3,
     "items": [
        ("📚", "1. Nghiên cứu tài liệu", "Đối chiếu hồ sơ thiết kế, lý lịch tủ báo, sổ bảo dưỡng"),
        ("👁️", "2. Quan sát", "Kiểm tra trực quan đầu báo, bình CC, lối thoát nạn"),
        ("📏", "3. Đo, đếm", "Đo áp suất bơm, bình FM-200, thông số kỹ thuật"),
     ]},
    {"type": "table", "title": "NỘI DUNG KIỂM TRA ĐỊNH KỲ",
     "headers": ["Hạng mục", "Nội dung", "Tần suất"],
     "rows": [
        ["Tủ báo cháy L@titude", "Normal/Trouble, nguồn AC/DC", "Hàng ngày"],
        ["Bơm chữa cháy", "Áp suất, Auto, chạy thử", "Hàng tuần"],
        ["Đầu báo, chuông, còi", "Vệ sinh, kiểm tra hoạt động", "Hàng tháng"],
        ["Hệ thống FM-200", "Áp suất, chốt AT, Auto", "6 tháng"],
     ]},
    {"type": "flow", "title": "THAO TÁC KHI CÓ BÁO CHÁY",
     "rows": [
        ["🔔 Báo cháy kích hoạt", "Kiểm tra vị trí trên tủ", "Kiểm tra thực tế"],
        ["🔥 Cháy thật: Gọi 114 + Di tản", "✅ Báo giả: Sửa lỗi + Reset", ""],
     ]},
    {"type": "table", "title": "BẢO TRÌ & LỊCH ĐỊNH KỲ",
     "headers": ["Tần suất", "Hạng mục", "Ghi chú"],
     "rows": [
        ["Ngày", "Tủ báo cháy, bình CC", "Trạng thái"],
        ["Tuần", "Bơm CC, van", "Chạy thử, áp"],
        ["Tháng", "Đầu báo, chuông, còi", "Vệ sinh"],
        ["Quý", "Nút báo, chuông, còi", "Chức năng"],
        ["6 tháng", "FM-200", "Tổng thể"],
     ]},
    {"type": "table", "title": "XỬ LÝ SỰ CỐ BÁO CHÁY",
     "headers": ["Sự cố", "Dấu hiệu", "Nguyên nhân", "Khắc phục"],
     "rows": [
        ["Mất nguồn", "Màn tối", "Mất điện, cầu chì", "Ktra cầu chì, ắc quy"],
        ["Chạm đất", "Trouble", "Dây chạm vỏ", "Ktra dây, đầu báo"],
        ["Ngắn mạch", "Mất loop", "Module chập", "Ktra từng TB"],
        ["Báo giả", "Fire nhả", "Bụi, côn trùng", "Vệ sinh đầu báo"],
        ["Mất chuông", "Fire, ko chuông", "NAC/relay hỏng", "Ktra NAC, relay"],
     ]},
    {"type": "table", "title": "XỬ LÝ SỰ CỐ BƠM CHỮA CHÁY",
     "headers": ["Hiện tượng", "Nguyên nhân", "Khắc phục"],
     "rows": [
        ["Động cơ không chạy", "Mất nguồn, contactor hỏng", "Ktra nguồn, contactor"],
        ["Bơm chạy không nước", "Mồi nước, van hút đóng", "Mồi lại, mở van"],
        ["Quá tải", "Rơ-le nhiệt sai, dòng cao", "Chỉnh rơ-le, ktra dòng"],
        ["Rung, ồn", "Mất cân bằng, đế lỏng", "Cân chỉnh, bắt chặt"],
        ["Bù áp chạy liên tục", "Van 1 chiều rò", "Phát hiện rò"],
     ]},
    {"type": "list", "title": "TỒN TẠI, THIẾU SÓT KHI TỰ KIỂM TRA",
     "lines": [
        "Chưa xây dựng kế hoạch PCCC hàng năm, tuyên truyền, huấn luyện",
        "Hồ sơ quản lý PCCC không đầy đủ, chưa cập nhật nhân sự",
        "Không niêm yết HD vận hành tủ báo cháy, quy trình bơm",
        "Thiếu thực tập phương án chữa cháy (tối thiểu 1 lần/năm)",
        "Không phúc tra khắc phục kiến nghị lần kiểm tra trước",
        "**Khuyến nghị:** Lập KH năm, phân công phụ trách, niêm yết HD, tổ chức thực tập 1 lần/năm.",
     ]},
    {"type": "section", "title": "PHẦN D",
     "subtitle": "ỨNG PHÓ KHẨN CẤP & KỸ NĂNG XỬ LÝ",
     "lines": ["Quy trình hành động khi có cháy thật, thao tác chữa cháy ban đầu và kỹ năng vận hành hệ thống chữa cháy tự động."]},
    {"type": "list", "title": "QUY TRÌNH ỨNG PHÓ KHẨN CẤP",
     "lines": [
        "**Bước 1 – Phát hiện:** Hét 'CHÁY!' → Nhấn nút báo cháy → Ngắt cầu dao điện",
        "**Bước 2 – Ứng phó:** Gọi 114 → Sơ tán → Dùng bình CC ban đầu → Di chuyển vật dễ cháy",
        "**Bước 3 – Phối hợp:** Di chuyển theo lối thoát hiểm → Đón lực lượng PCCC → Theo chỉ huy",
     ]},
    {"type": "list", "title": "VẬN HÀNH HCVR-3 FM-200 (6 BƯỚC)",
     "lines": [
        "**1. Phát hiện:** Đầu báo khói/nhiệt kích hoạt (VESDA)",
        "**2. Đếm ngược:** Thời gian trễ tắt đèn, quạt, đóng cửa",
        "**3. Phun khí:** Van điện từ mở → FM-200 phun",
        "**4. Duy trì:** Giữ nồng độ dập tắt vài phút",
        "**5. Reset:** Khóa van bằng tay, nạp lại FM-200",
        "**6. Kiểm tra:** Áp suất & mức khí sau phun",
     ]},
    {"type": "pass", "title": "HƯỚNG DẪN SỬ DỤNG BÌNH CHỮA CHÁY – PASS",
     "items": [
        ("P", "Pull", "Rút chốt an toàn"),
        ("A", "Aim", "Hướng vào gốc lửa"),
        ("S", "Squeeze", "Bóp tay cầm phun"),
        ("S", "Sweep", "Quét ngang qua"),
     ]},
    {"type": "closing", "title": "PHÒNG CHÁY HƠN CHỮA CHÁY",
     "subtitle": "AN TOÀN LÀ TRÊN HẾT",
     "lines": [
        "Phát hiện sớm – Xử lý kịp thời – An toàn bền vững",
        "Nhà máy Điện gió Yang Trung – Chơ Long • CLWP-QT-07",
     ]},
]


# ===================== RENDER HEADER (giống ảnh mẫu) =====================
def render_header(idx, total):
    """Header giống ảnh mẫu: nền trắng + viền xanh navy + logo PESE + tên công ty."""
    logo_b64 = img_to_base64(LOGO_PATH)
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" alt="PESE">' if logo_b64 else ''
    st.markdown(f"""
    <div class="header-wrap">
        <span class="header-logo-box">{logo_html}</span><span class="header-text-box">
            <div class="company">CÔNG TY TNHH DỊCH VỤ VÀ KỸ THUẬT NĂNG LƯỢNG PECC2</div>
            <div class="center">TRUNG TÂM QUẢN LÝ VẬN HÀNH NHÀ MÁY ĐIỆN</div>
        </span><span class="header-slide-no">{idx}/{total}</span>
    </div>
    """, unsafe_allow_html=True)


def render_title_bar(title):
    """Tiêu đề slide: nền đỏ, chữ trắng."""
    st.markdown(f'<div class="slide-title-bar">📑 {title}</div>', unsafe_allow_html=True)


# ===================== RENDER SLIDE =====================
def render_slide(slide, idx, total):
    stype = slide.get("type", "content")

    if stype == "cover":
        logo_b64 = img_to_base64(LOGO_PATH)
        bg_b64 = img_to_base64(BG_PATH)
        logo_html = f'<img class="logo" src="data:image/png;base64,{logo_b64}">' if logo_b64 else ''
        bg_style = f"background-image:url('data:image/jpeg;base64,{bg_b64}');" if bg_b64 else 'background:#333;'

        st.markdown(f"""
        <div class="cover-wrapper">
            <div class="cover-left">
                {logo_html}
                <div class="top-line"></div>
                <h1>ĐÀO TẠO PHÒNG<br>CHÁY CHỮA CHÁY</h1>
                <div class="sub">NHÀ MÁY ĐIỆN GIÓ YANG TRUNG –<br>CHƠ LONG</div>
                <div class="divider"></div>
                <div class="company">CÔNG TY TNHH DỊCH VỤ VÀ KỸ THUẬT NĂNG LƯỢNG<br>PECC2</div>
                <div class="center">TRUNG TÂM QUẢN LÝ VẬN HÀNH NHÀ MÁY ĐIỆN</div>
                <div class="info">
                    <strong>Người trình bày:</strong> Trương Hoàng An<br>
                    <strong>Mã quy trình:</strong> CLWP-QT-07
                </div>
            </div><div class="cover-right" style="{bg_style}"></div>
        </div>
        """, unsafe_allow_html=True)
        return

    if stype == "section":
        st.markdown(f"""
        <div class="section">
            <h2>{slide['title']}</h2>
            <div class="sub">{slide.get('subtitle','')}</div>
            <p>{' '.join(slide.get('lines', []))}</p>
        </div>
        """, unsafe_allow_html=True)
        return

    if stype == "closing":
        st.markdown(f"""
        <div class="closing">
            <h2>{slide['title']}</h2>
            <div class="sub">{slide.get('subtitle','')}</div>
            <p style="margin-top:24px">{slide['lines'][0]}</p>
            <p style="margin-top:12px;color:rgba(255,255,255,.6);font-size:12px">{slide['lines'][1]}</p>
        </div>
        """, unsafe_allow_html=True)
        return

    # Header + Title cho các slide khác
    render_header(idx, total)
    render_title_bar(slide.get("title", ""))

    if stype == "toc":
        cols = st.columns(2)
        colors = [("#CC0000", "linear-gradient(145deg,#fff5f5,#fff)"),
                  ("#E65100", "linear-gradient(145deg,#fff8f0,#fff)"),
                  ("#1565C0", "linear-gradient(145deg,#f5f5ff,#fff)"),
                  ("#2E7D32", "linear-gradient(145deg,#f5fff5,#fff)")]
        for i, (badge, title, desc) in enumerate(slide["items"]):
            with cols[i % 2]:
                c, bg = colors[i]
                st.markdown(f"""
                <div style="background:{bg};border:2px solid {c};border-radius:14px;padding:16px 18px;margin-bottom:14px;display:flex;gap:14px;box-shadow:0 8px 20px rgba(0,0,0,.08)">
                    <div style="width:44px;height:44px;border-radius:12px;background:{c};color:#fff;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:800;flex-shrink:0">{badge}</div>
                    <div>
                        <div style="font-size:14px;font-weight:700;margin-bottom:4px;color:#222">{title}</div>
                        <div style="font-size:12px;color:#666;line-height:1.4">{desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        return

    if stype == "cards":
        cols_n = slide.get("cols", 3)
        cols = st.columns(cols_n)
        for i, item in enumerate(slide["items"]):
            icon, title, desc = item
            with cols[i % cols_n]:
                st.markdown(f"""
                <div class="card" style="text-align:center;padding:18px 12px">
                    <div style="font-size:32px">{icon}</div>
                    <div style="color:#CC0000;font-size:14px;font-weight:700;margin-top:6px">{title}</div>
                    <div style="font-size:12px;color:#333;margin-top:4px">{desc}</div>
                </div>
                """, unsafe_allow_html=True)
        return

    if stype == "list":
        html = "<ul class='cl'>" + "".join([f"<li>{l}</li>" for l in slide["lines"]]) + "</ul>"
        st.markdown(html, unsafe_allow_html=True)
        return

    if stype == "table":
        headers = slide["headers"]
        rows = slide["rows"]
        table_md = "| " + " | ".join(headers) + " |\n"
        table_md += "|" + "|".join(["---"] * len(headers)) + "|\n"
        for r in rows:
            table_md += "| " + " | ".join(str(x) for x in r) + " |\n"
        st.markdown(table_md)
        return

    if stype == "two-col":
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**{slide.get('left_title','')}**")
            st.markdown("<ul class='cl'>" + "".join([f"<li>{l}</li>" for l in slide.get("left_lines", [])]) + "</ul>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"**{slide.get('right_title','')}**")
            st.markdown("<ul class='cl'>" + "".join([f"<li>{l}</li>" for l in slide.get("right_lines", [])]) + "</ul>", unsafe_allow_html=True)
        if slide.get("note"):
            st.info(slide["note"])
        return

    if stype == "flow":
        for row in slide["rows"]:
            cols = st.columns(len(row) * 2 - 1)
            for i, box in enumerate(row):
                with cols[i * 2]:
                    cls = "flow-box act" if box and i == 0 else "flow-box"
                    st.markdown(f"<div class='{cls}'>{box if box else '&nbsp;'}</div>", unsafe_allow_html=True)
                if i < len(row) - 1:
                    with cols[i * 2 + 1]:
                        st.markdown("<div class='arrow'>→</div>", unsafe_allow_html=True)
        return

    if stype == "kpi":
        cols = st.columns(len(slide["kpis"]))
        for i, (v, l) in enumerate(slide["kpis"]):
            with cols[i]:
                st.markdown(f"""
                <div class="kpi">
                    <div class="v">{v}</div>
                    <div class="l">{l}</div>
                </div>
                """, unsafe_allow_html=True)
        if slide.get("note"):
            st.info(slide["note"])
        return

    if stype == "pass":
        cols = st.columns(4)
        for i, (letter, name, desc) in enumerate(slide["items"]):
            with cols[i]:
                st.markdown(f"""
                <div class="pass-card">
                    <div class="lt">{letter}</div>
                    <h4>{name}</h4>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)
        return


# ===================== TẠO PPTX =====================
def build_pptx():
    try:
        from pptx import Presentation
        from pptx.util import Inches, Pt
        from pptx.dml.color import RGBColor
        from pptx.enum.text import PP_ALIGN

        prs = Presentation()
        prs.slide_width = Inches(13.333)
        prs.slide_height = Inches(7.5)
        blank = prs.slide_layouts[6]

        RED = RGBColor(0xCC, 0x00, 0x00)
        DARK_RED = RGBColor(0x80, 0x00, 0x00)
        NAVY = RGBColor(0x1A, 0x23, 0x7E)
        YELLOW = RGBColor(0xFF, 0xD7, 0x00)
        WHITE = RGBColor(0xFF, 0xFF, 0xFF)
        BLACK = RGBColor(0x22, 0x22, 0x22)
        GRAY = RGBColor(0x66, 0x66, 0x66)

        for idx_s, slide in enumerate(SLIDES):
            stype = slide.get("type", "content")
            s = prs.slides.add_slide(blank)

            if stype == "cover":
                left_box = s.shapes.add_shape(1, Inches(0), Inches(0), Inches(7.7), Inches(7.5))
                left_box.fill.solid()
                left_box.fill.fore_color.rgb = DARK_RED
                left_box.line.fill.background()

                if os.path.exists(BG_PATH):
                    s.shapes.add_picture(BG_PATH, Inches(7.7), Inches(0),
                                         width=Inches(5.633), height=Inches(7.5))
                if os.path.exists(LOGO_PATH):
                    s.shapes.add_picture(LOGO_PATH, Inches(0.35), Inches(0.3), height=Inches(0.7))

                tb = s.shapes.add_textbox(Inches(0.5), Inches(2.0), Inches(7.0), Inches(2.2))
                tf = tb.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                r = p.add_run()
                r.text = "ĐÀO TẠO PHÒNG\nCHÁY CHỮA CHÁY"
                r.font.size = Pt(44); r.font.bold = True; r.font.color.rgb = WHITE

                tb2 = s.shapes.add_textbox(Inches(0.5), Inches(4.0), Inches(7.0), Inches(1.0))
                tf2 = tb2.text_frame; tf2.word_wrap = True
                p2 = tf2.paragraphs[0]; r2 = p2.add_run()
                r2.text = "NHÀ MÁY ĐIỆN GIÓ YANG TRUNG – CHƠ LONG"
                r2.font.size = Pt(20); r2.font.bold = True; r2.font.color.rgb = YELLOW

                tb3 = s.shapes.add_textbox(Inches(0.5), Inches(5.2), Inches(7.0), Inches(2.0))
                tf3 = tb3.text_frame; tf3.word_wrap = True
                info_lines = [
                    "CÔNG TY TNHH DỊCH VỤ VÀ KỸ THUẬT NĂNG LƯỢNG PECC2",
                    "TRUNG TÂM QUẢN LÝ VẬN HÀNH NHÀ MÁY ĐIỆN",
                    "", "Người trình bày: Trương Hoàng An", "Mã quy trình: CLWP-QT-07",
                ]
                for i, line in enumerate(info_lines):
                    p3 = tf3.paragraphs[0] if i == 0 else tf3.add_paragraph()
                    r3 = p3.add_run(); r3.text = line; r3.font.size = Pt(12)
                    r3.font.color.rgb = WHITE if "Người" in line or "Mã" in line else RGBColor(0xDD, 0xDD, 0xDD)

            elif stype == "section":
                bg = s.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
                bg.fill.solid(); bg.fill.fore_color.rgb = DARK_RED; bg.line.fill.background()
                tb = s.shapes.add_textbox(Inches(1), Inches(2.5), Inches(11.333), Inches(1.5))
                tf = tb.text_frame; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
                r = p.add_run(); r.text = slide['title']
                r.font.size = Pt(48); r.font.bold = True; r.font.color.rgb = WHITE
                tb2 = s.shapes.add_textbox(Inches(1), Inches(4.0), Inches(11.333), Inches(1.5))
                tf2 = tb2.text_frame; p2 = tf2.paragraphs[0]; p2.alignment = PP_ALIGN.CENTER
                r2 = p2.add_run(); r2.text = slide.get('subtitle', '')
                r2.font.size = Pt(24); r2.font.color.rgb = WHITE
                if slide.get('lines'):
                    tb3 = s.shapes.add_textbox(Inches(1.5), Inches(5.3), Inches(10.333), Inches(1.5))
                    tf3 = tb3.text_frame; p3 = tf3.paragraphs[0]; p3.alignment = PP_ALIGN.CENTER
                    r3 = p3.add_run(); r3.text = ' '.join(slide.get('lines', []))
                    r3.font.size = Pt(14); r3.font.color.rgb = RGBColor(0xEE, 0xEE, 0xEE)

            elif stype == "closing":
                bg = s.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
                bg.fill.solid(); bg.fill.fore_color.rgb = RED; bg.line.fill.background()
                tb = s.shapes.add_textbox(Inches(1), Inches(2.5), Inches(11.333), Inches(1.5))
                tf = tb.text_frame; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
                r = p.add_run(); r.text = slide['title']
                r.font.size = Pt(48); r.font.bold = True; r.font.color.rgb = WHITE
                tb2 = s.shapes.add_textbox(Inches(1), Inches(4.0), Inches(11.333), Inches(1))
                tf2 = tb2.text_frame; p2 = tf2.paragraphs[0]; p2.alignment = PP_ALIGN.CENTER
                r2 = p2.add_run(); r2.text = slide.get('subtitle', '')
                r2.font.size = Pt(28); r2.font.color.rgb = WHITE
                tb3 = s.shapes.add_textbox(Inches(1), Inches(5.3), Inches(11.333), Inches(1.5))
                tf3 = tb3.text_frame; tf3.word_wrap = True
                for i, line in enumerate(slide.get('lines', [])):
                    p3 = tf3.paragraphs[0] if i == 0 else tf3.add_paragraph()
                    p3.alignment = PP_ALIGN.CENTER
                    r3 = p3.add_run(); r3.text = line
                    r3.font.size = Pt(14); r3.font.color.rgb = RGBColor(0xEE, 0xEE, 0xEE)

            else:
                # Header trắng + viền navy
                hdr = s.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(0.95))
                hdr.fill.solid(); hdr.fill.fore_color.rgb = WHITE
                hdr.line.color.rgb = NAVY; hdr.line.width = Pt(2)

                if os.path.exists(LOGO_PATH):
                    s.shapes.add_picture(LOGO_PATH, Inches(0.2), Inches(0.2), height=Inches(0.55))

                tb_hdr = s.shapes.add_textbox(Inches(1.8), Inches(0.1), Inches(11.0), Inches(0.75))
                tf_hdr = tb_hdr.text_frame; tf_hdr.word_wrap = True
                p_h = tf_hdr.paragraphs[0]; p_h.alignment = PP_ALIGN.CENTER
                r_h = p_h.add_run(); r_h.text = "CÔNG TY TNHH DỊCH VỤ VÀ KỸ THUẬT NĂNG LƯỢNG PECC2"
                r_h.font.size = Pt(14); r_h.font.bold = True; r_h.font.color.rgb = NAVY
                p_h2 = tf_hdr.add_paragraph(); p_h2.alignment = PP_ALIGN.CENTER
                r_h2 = p_h2.add_run(); r_h2.text = "TRUNG TÂM QUẢN LÝ VẬN HÀNH NHÀ MÁY ĐIỆN"
                r_h2.font.size = Pt(12); r_h2.font.bold = True; r_h2.font.color.rgb = RED

                # Tiêu đề slide: nền đỏ, chữ trắng
                title_bg = s.shapes.add_shape(1, Inches(0.4), Inches(1.05), Inches(12.533), Inches(0.55))
                title_bg.fill.solid(); title_bg.fill.fore_color.rgb = RED
                title_bg.line.fill.background()
                tb_title = s.shapes.add_textbox(Inches(0.5), Inches(1.08), Inches(12.4), Inches(0.5))
                tf_t = tb_title.text_frame
                p_t = tf_t.paragraphs[0]
                r_t = p_t.add_run(); r_t.text = slide.get('title', '')
                r_t.font.size = Pt(18); r_t.font.bold = True; r_t.font.color.rgb = WHITE

                # Nội dung
                tb_content = s.shapes.add_textbox(Inches(0.5), Inches(1.85), Inches(12.333), Inches(5.3))
                tf_content = tb_content.text_frame; tf_content.word_wrap = True

                def add_line(text, bold=False, size=14, color=BLACK):
                    if len(tf_content.paragraphs) == 1 and tf_content.paragraphs[0].text == "":
                        p = tf_content.paragraphs[0]
                    else:
                        p = tf_content.add_paragraph()
                    r = p.add_run(); r.text = str(text)
                    r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color

                if stype == "toc":
                    for badge, title, desc in slide["items"]:
                        add_line(f"▸ {badge}. {title}", bold=True, size=16, color=RED)
                        add_line(f"     {desc}", size=12, color=GRAY)
                elif stype == "cards":
                    for icon, title, desc in slide["items"]:
                        add_line(f"{icon} {title}", bold=True, size=15, color=RED)
                        if desc: add_line(f"     {desc}", size=12, color=GRAY)
                elif stype == "list":
                    for line in slide["lines"]:
                        add_line(f"▸ {line.replace('**','')}", size=13)
                elif stype == "table":
                    add_line(" | ".join(slide["headers"]), bold=True, size=12, color=WHITE)
                    for row in slide["rows"]:
                        add_line(" | ".join(str(x) for x in row), size=11)
                elif stype == "two-col":
                    add_line(slide.get("left_title", ""), bold=True, size=15, color=RED)
                    for l in slide.get("left_lines", []): add_line(f"  • {l}", size=12)
                    add_line("", size=8)
                    add_line(slide.get("right_title", ""), bold=True, size=15, color=RED)
                    for l in slide.get("right_lines", []): add_line(f"  • {l}", size=12)
                    if slide.get("note"):
                        add_line("", size=8)
                        add_line(slide["note"].replace("**", ""), size=12, color=RED)
                elif stype == "flow":
                    for row in slide["rows"]:
                        add_line("  →  ".join([b for b in row if b]), size=14, bold=True, color=RED)
                elif stype == "kpi":
                    add_line(" | ".join([f"{v} ({l})" for v, l in slide["kpis"]]), size=18, bold=True, color=RED)
                    if slide.get("note"):
                        add_line("", size=8); add_line(slide["note"], size=12)
                elif stype == "pass":
                    for letter, name, desc in slide["items"]:
                        add_line(f"{letter} – {name}: {desc}", size=15, bold=True, color=RED)

        buf = io.BytesIO()
        prs.save(buf)
        buf.seek(0)
        return buf.getvalue()
    except ImportError:
        return None


# ===================== ĐIỀU KHIỂN =====================
if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0

TOTAL = len(SLIDES)

render_slide(SLIDES[st.session_state.slide_idx], st.session_state.slide_idx + 1, TOTAL)

st.markdown("<br>", unsafe_allow_html=True)

nav1, nav2, nav3, nav4 = st.columns([1, 2.5, 1, 1.5])

with nav1:
    if st.button("◀ Trước", key="prev_btn", use_container_width=True):
        st.session_state.slide_idx = (st.session_state.slide_idx - 1) % TOTAL
        st.rerun()

with nav2:
    dots_html = "<div class='dots-wrap'>"
    for i in range(TOTAL):
        cls = "dot active" if i == st.session_state.slide_idx else "dot"
        dots_html += f"<span class='{cls}'></span>"
    dots_html += "</div>"
    st.markdown(dots_html, unsafe_allow_html=True)

with nav3:
    if st.button("Tiếp ▶", key="next_btn", use_container_width=True):
        st.session_state.slide_idx = (st.session_state.slide_idx + 1) % TOTAL
        st.rerun()

with nav4:
    if st.button("📥 Tải PPTX", key="dl_btn", use_container_width=True):
        with st.spinner("Đang tạo file PPTX..."):
            pptx_bytes = build_pptx()
            if pptx_bytes:
                st.session_state["pptx_data"] = pptx_bytes
            else:
                st.error("Cần cài `python-pptx`: thêm `python-pptx` vào requirements.txt")

if "pptx_data" in st.session_state and st.session_state["pptx_data"]:
    st.download_button(
        label="⬇️ Nhấn để tải file PPTX",
        data=st.session_state["pptx_data"],
        file_name=f"DaoTao_PCCC_YangTrung_{datetime.now().strftime('%Y%m%d_%H%M')}.pptx",
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        use_container_width=True,
    )

with st.expander("🔍 Chuyển nhanh đến slide"):
    options = [f"{i+1}. {s.get('title', s.get('subtitle',''))}" for i, s in enumerate(SLIDES)]
    sel = st.selectbox("Chọn slide", options, index=st.session_state.slide_idx,
                       label_visibility="collapsed")
    new_idx = options.index(sel)
    if new_idx != st.session_state.slide_idx:
        st.session_state.slide_idx = new_idx
        st.rerun()
