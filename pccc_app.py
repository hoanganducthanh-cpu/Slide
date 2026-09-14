import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QStackedWidget,
                             QScrollArea, QFrame, QGridLayout)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPixmap, QPalette, QColor, QKeySequence, QShortcut


# ===================== DỮ LIỆU SLIDE =====================
# Mỗi slide: (tiêu đề, nội dung dạng list các dòng hoặc dict)
SLIDES = [
    {
        "title": "ĐÀO TẠO PHÒNG CHÁY CHỮA CHÁY",
        "subtitle": "NHÀ MÁY ĐIỆN GIÓ YANG TRUNG – CHƠ LONG",
        "lines": [
            "CÔNG TY TNHH DỊCH VỤ VÀ KỸ THUẬT NĂNG LƯỢNG PECC2",
            "TRUNG TÂM QUẢN LÝ VẬN HÀNH NHÀ MÁY ĐIỆN",
            "Người trình bày: Trương Hoàng An",
            "Mã quy trình: CLWP-QT-07",
        ],
        "type": "cover",
    },
    {
        "title": "MỤC LỤC – KẾT CẤU CHƯƠNG TRÌNH ĐÀO TẠO",
        "lines": [
            "A. Nền tảng về cháy & khung pháp lý PCCC",
            "B. Hệ thống PCCC tại nhà máy",
            "C. Quy trình kiểm tra, vận hành & bảo trì",
            "D. Ứng phó khẩn cấp & xử lý sự cố",
        ],
        "type": "toc",
    },
    {
        "title": "PHẦN A",
        "subtitle": "NỀN TẢNG VỀ CHÁY & KHUNG PHÁP LÝ PCCC",
        "lines": ["Hiểu bản chất sự cháy, quy định pháp luật và trách nhiệm PCCC."],
        "type": "section",
    },
    {
        "title": "PCCC – TẠI SAO CẦN THIẾT?",
        "lines": [
            "🛡️ Bảo vệ tính mạng & tài sản",
            "⚡ Đảm bảo ổn định điện",
            "📋 Yêu cầu pháp lý: Luật PCCC & CNCH, NĐ 105/2025, TT 36/2025",
        ],
        "type": "content",
    },
    {
        "title": "KHÁI NIỆM VỀ SỰ CHÁY",
        "lines": [
            "Theo khoa học PCCC: Quá trình biến đổi lý–hóa phức tạp, tỏa nhiệt & phát sáng.",
            "Theo Luật PCCC: Phản ứng hóa học có tỏa nhiệt, phát ánh sáng hoặc khói.",
            "⚗️ Phản ứng hóa học | 🌡️ Tỏa nhiệt | 💡 Phát sáng",
        ],
        "type": "content",
    },
    {
        "title": "BA YẾU TỐ CẦN THIẾT CHO SỰ CHÁY",
        "lines": [
            "🔥 Chất cháy: Cáp điện, dầu MBA, pin lưu trữ...",
            "⚡ Nguồn nhiệt: Chập mạch, quá tải, sét đánh...",
            "🌬️ Chất oxy hóa: Oxy trong không khí (~21%)",
        ],
        "type": "table",
    },
    {
        "title": "BỐN ĐIỀU KIỆN CẦN THIẾT CHO SỰ CHÁY",
        "lines": [
            "1. Tiếp xúc trực tiếp",
            "2. Thời gian tiếp xúc đủ lớn",
            "3. Nồng độ trong giới hạn bắt cháy",
            "4. Đạt nhiệt độ tự bắt cháy",
            "→ Chỉ cần loại bỏ MỘT điều kiện là ngăn được cháy.",
        ],
        "type": "content",
    },
    {
        "title": "NGUYÊN NHÂN CHÁY",
        "lines": [
            "🌩️ Tự nhiên | ⚡ Sự cố bất ngờ | 😕 Vô ý",
            "🚫 Vi phạm quy định | 🔴 Cố ý | ❓ Nguyên nhân khác",
        ],
        "type": "content",
    },
    {
        "title": "NGUY CƠ CHÁY ĐẶC THÙ TẠI NHÀ MÁY ĐIỆN GIÓ",
        "lines": [
            "Trạm biến áp 22kV: Dầu cách điện, cáp trung thế",
            "Phòng Pin/Accu: Cháy hóa chất pin lưu trữ",
            "Phòng Datacenter: Cháy thiết bị điện tử",
            "Tuabin gió (nacelle): Cháy dầu bôi trơn, hộp số",
        ],
        "type": "table",
    },
    {
        "title": "PHẠM VI ÁP DỤNG & ĐỐI TƯỢNG",
        "lines": [
            "📍 Phạm vi: Toàn bộ nhà máy, mã CLWP-QT-07",
            "👤 Đối tượng: CBQL, kỹ thuật vận hành, vận hành viên, bảo vệ",
            "Chỉ huy chữa cháy: Người đứng đầu → Đội trưởng → Trưởng ca",
        ],
        "type": "content",
    },
    {
        "title": "HỒ SƠ QUẢN LÝ PCCC CỦA NHÀ MÁY",
        "lines": [
            "📄 PC01 – Thông tin cơ sở | 📜 Nội quy PCCC",
            "📐 Thẩm duyệt | 👨‍🚒 Đội PCCC | 📋 PC06",
            "🧯 Sổ PT | 📊 Nghiệm thu | 🎓 CN huấn luyện | 📎 Khác",
        ],
        "type": "content",
    },
    {
        "title": "TRÁCH NHIỆM & CHẾ ĐỘ KIỂM TRA PCCC",
        "lines": [
            "🔄 Thường xuyên: Không quá 1 tháng/lần",
            "📅 Định kỳ: 6 tháng hoặc 1 năm – Mẫu PC02",
            "⚠️ Trách nhiệm hình sự: Điều 313 BLHS – phạt tù đến 12 năm",
        ],
        "type": "content",
    },
    {
        "title": "PHẦN B",
        "subtitle": "HỆ THỐNG PCCC TẠI NHÀ MÁY ĐIỆN GIÓ YANG TRUNG – CHƠ LONG",
        "lines": ["Cấu trúc, thiết bị và nguyên lý hoạt động."],
        "type": "section",
    },
    {
        "title": "TỔNG QUAN HỆ THỐNG PCCC",
        "lines": [
            "🔥 Hệ thống báo cháy: Tủ Hochiki L@titude (2 loop)",
            "💧 Hệ thống chữa cháy: Bơm 75kW, FM-200, phun sương",
        ],
        "type": "content",
    },
    {
        "title": "SƠ ĐỒ KHỐI HỆ THỐNG PCCC",
        "lines": [
            "Phát hiện cháy → Báo cháy trung tâm → Cảnh báo sơ tán",
            "Kích hoạt chữa cháy → Bơm/FM-200/Phun sương → Kiểm soát",
        ],
        "type": "flow",
    },
    {
        "title": "NGUYÊN LÝ HOẠT ĐỘNG BÁO CHÁY",
        "lines": [
            "🔍 Đầu báo khói/nhiệt phát hiện dấu hiệu cháy",
            "📡 Tín hiệu truyền về trung tâm Hochiki L@titude",
            "🔔 Kích hoạt chuông, còi, đèn cảnh báo",
            "🖥️ Hiển thị vị trí cháy trên màn hình",
        ],
        "type": "content",
    },
    {
        "title": "CÁC THÀNH PHẦN HỆ THỐNG BÁO CHÁY",
        "lines": [
            "🔍 Đầu báo | 🔌 Module | 💻 Trung tâm L@titude LA303H1-10 | 🔔 Cảnh báo",
        ],
        "type": "content",
    },
    {
        "title": "PHÂN LOẠI ĐẦU BÁO CHÁY",
        "lines": [
            "Khói quang thường | Khói địa chỉ | Nhiệt gia tăng | Nhiệt chống nổ FFH-2E120",
        ],
        "type": "table",
    },
    {
        "title": "SO SÁNH CONVENTIONAL vs ADDRESSABLE",
        "lines": [
            "Conventional: Báo theo zone | Addressable: Chính xác từng ID",
            "Giao thức: Analog vs DCP Protocol",
        ],
        "type": "table",
    },
    {
        "title": "CÁC MODULE TRONG HỆ THỐNG BÁO CHÁY",
        "lines": [
            "DCP-CZM | DCP-SOM | DCP-DIMM | DCP-R2ML | DCP-SCI",
        ],
        "type": "content",
    },
    {
        "title": "TỦ HOCHIKI L@TITUDE LA303H1-10",
        "lines": [
            "2 loop địa chỉ | Bo S721 xử lý | Bo S722 báo cháy",
            "Bo S769 4 kênh NAC | Bo S770 Relay | Nguồn S406 24Vdc",
        ],
        "type": "content",
    },
    {
        "title": "VẬN HÀNH TỦ BÁO CHÁY & CÁC TRẠNG THÁI",
        "lines": [
            "1. Nhấn MENU → ENTER | 2. Chọn SYSTEM STATUS",
            "3. Chọn POINT STATUS | 4. Xem trạng thái LOOP",
            "Trạng thái: ✅ Bình thường | ⚠️ Sự cố | 🔥 Báo cháy",
        ],
        "type": "content",
    },
    {
        "title": "CÁC NÚT NHẤN TRÊN TỦ BÁO CHÁY",
        "lines": [
            "SILENCE – Tắt chuông | RESET – Reset hệ thống",
            "TEST – Kiểm tra đèn, chuông | BUZZER – Kiểm tra còi",
        ],
        "type": "table",
    },
    {
        "title": "HỆ THỐNG CHỮA CHÁY – TỔNG QUAN",
        "lines": [
            "💧 Chữa cháy nước: Bơm chính 75kW, dự phòng 75kW, Jockey",
            "🧯 Khí FM-200: Tủ HCVR-3, 3 bình",
            "💨 Phun sương BA: HV14 360°, STV-NZ",
        ],
        "type": "content",
    },
    {
        "title": "BƠM CHỮA CHÁY & CHẾ ĐỘ VẬN HÀNH",
        "lines": [
            "Bơm chính 75kW | Bơm dự phòng 75kW | Jockey bù áp",
            "⚙️ Tự động: Tủ ECS điều khiển | ✋ Bằng tay: Start/Stop",
        ],
        "type": "content",
    },
    {
        "title": "TỦ HCVR-3 FM-200 & KHU VỰC BẢO VỆ",
        "lines": [
            "03 bình FM-200 | 3 khu vực bảo vệ | 42 bar ở 21°C",
            "Auto/Manual van chuyển mạch",
            "🏗️ Datacenter | 📦 Pin/Accu | ⚡ 22kV",
        ],
        "type": "content",
    },
    {
        "title": "BÌNH CHỮA CHÁY MFZ/ABC, CO₂ & KIỂM TRA",
        "lines": [
            "🧯 MFZ/ABC8 – Bột khô: Dập cháy A, B, C",
            "🧯 Bình CO₂: Chữa cháy TB điện tử",
            "Kiểm tra: Kim áp XANH, chốt an toàn, không móp/rỉ, còn hạn",
        ],
        "type": "content",
    },
    {
        "title": "HỆ THỐNG PHUN SƯƠNG CAO ÁP & TRẠM BA",
        "lines": [
            "💨 Đầu HV14 phun sương 360° | 🌊 Đầu STV-NZ phun khí 360°",
            "⚡ Trạm biến áp: 90°C kích hoạt, ống STK D65/D50, cách 1.2m",
        ],
        "type": "content",
    },
    {
        "title": "PHÂN LOẠI ĐÁM CHÁY & CHẤT CHỮA CHÁY",
        "lines": [
            "A – Rắn | B – Lỏng | C – Khí | E – Điện",
            "Bột MFZ/ABC: A,B,C | CO₂: B,E | FM-200: A,B,E | Phun sương: A,B,E",
        ],
        "type": "table",
    },
    {
        "title": "THIẾT BỊ PHỤ TRỢ CHỮA CHÁY",
        "lines": ["🔌 Họng DN65 | 🧰 Tủ chữa cháy | 🔧 Cuộn vòi | 💨 HV14/STV-NZ"],
        "type": "content",
    },
    {
        "title": "PHẦN C",
        "subtitle": "QUY TRÌNH KIỂM TRA, VẬN HÀNH & BẢO TRÌ",
        "lines": ["Áp dụng 3 phương pháp kiểm tra PCCC vào thực tế."],
        "type": "section",
    },
    {
        "title": "BA PHƯƠNG PHÁP KIỂM TRA PCCC",
        "lines": [
            "📚 1. Nghiên cứu tài liệu: Đối chiếu hồ sơ thiết kế",
            "👁️ 2. Quan sát: Kiểm tra trực quan đầu báo, bình CC",
            "📏 3. Đo, đếm: Đo áp suất bơm, bình FM-200",
        ],
        "type": "content",
    },
    {
        "title": "NỘI DUNG KIỂM TRA ĐỊNH KỲ",
        "lines": [
            "Tủ báo cháy: Hàng ngày | Bơm chữa cháy: Hàng tuần",
            "Đầu báo, chuông, còi: Hàng tháng | FM-200: 6 tháng",
        ],
        "type": "table",
    },
    {
        "title": "THAO TÁC KHI CÓ BÁO CHÁY",
        "lines": [
            "🔔 Báo cháy kích hoạt → Kiểm tra vị trí trên tủ",
            "→ Kiểm tra thực tế → Cháy thật: Gọi 114 + Di tản",
            "→ Báo giả: Sửa lỗi + Reset",
        ],
        "type": "content",
    },
    {
        "title": "BẢO TRÌ & LỊCH ĐỊNH KỲ",
        "lines": [
            "Ngày: Tủ báo cháy, bình CC | Tuần: Bơm CC, van",
            "Tháng: Đầu báo, chuông, còi | Quý: Nút báo | 6 tháng: FM-200",
        ],
        "type": "table",
    },
    {
        "title": "XỬ LÝ SỰ CỐ BÁO CHÁY",
        "lines": [
            "Mất nguồn: Màn tối → Ktra cầu chì, ắc quy",
            "Chạm đất: Trouble → Ktra dây, đầu báo",
            "Ngắn mạch: Mất loop → Ktra từng TB",
            "Báo giả: Fire nhả → Vệ sinh đầu báo",
            "Mất chuông: Fire, ko chuông → Ktra NAC, relay",
        ],
        "type": "table",
    },
    {
        "title": "XỬ LÝ SỰ CỐ BƠM CHỮA CHÁY",
        "lines": [
            "Động cơ không chạy: Mất nguồn, contactor hỏng",
            "Bơm chạy không nước: Mồi nước, van hút đóng",
            "Quá tải: Rơ-le nhiệt sai, dòng cao",
            "Rung, ồn: Mất cân bằng, đế lỏng",
            "Bù áp chạy liên tục: Van 1 chiều rò",
        ],
        "type": "table",
    },
    {
        "title": "TỒN TẠI, THIẾU SÓT KHI TỰ KIỂM TRA",
        "lines": [
            "Chưa xây dựng kế hoạch PCCC hàng năm",
            "Hồ sơ quản lý PCCC không đầy đủ",
            "Không niêm yết HD vận hành tủ báo cháy",
            "Thiếu thực tập phương án chữa cháy (1 lần/năm)",
            "Không phúc tra khắc phục kiến nghị lần trước",
        ],
        "type": "content",
    },
    {
        "title": "PHẦN D",
        "subtitle": "ỨNG PHÓ KHẨN CẤP & KỸ NĂNG XỬ LÝ",
        "lines": ["Quy trình hành động khi có cháy thật."],
        "type": "section",
    },
    {
        "title": "QUY TRÌNH ỨNG PHÓ KHẨN CẤP",
        "lines": [
            "Bước 1 – Phát hiện: Hét 'CHÁY!' → Nhấn nút → Ngắt cầu dao",
            "Bước 2 – Ứng phó: Gọi 114 → Sơ tán → Dùng bình CC",
            "Bước 3 – Phối hợp: Di chuyển theo lối thoát hiểm → Đón PCCC",
        ],
        "type": "timeline",
    },
    {
        "title": "VẬN HÀNH HCVR-3 FM-200 (6 BƯỚC)",
        "lines": [
            "1. Phát hiện: Đầu báo khói/nhiệt kích hoạt",
            "2. Đếm ngược: Thời gian trễ tắt đèn, quạt",
            "3. Phun khí: Van điện từ mở → FM-200 phun",
            "4. Duy trì: Giữ nồng độ dập tắt vài phút",
            "5. Reset: Khóa van bằng tay, nạp lại FM-200",
            "6. Kiểm tra: Áp suất & mức khí sau phun",
        ],
        "type": "process",
    },
    {
        "title": "HƯỚNG DẪN SỬ DỤNG BÌNH CHỮA CHÁY – PASS",
        "lines": [
            "P – Pull: Rút chốt an toàn",
            "A – Aim: Hướng vào gốc lửa",
            "S – Squeeze: Bóp tay cầm phun",
            "S – Sweep: Quét ngang qua",
        ],
        "type": "pass",
    },
    {
        "title": "PHÒNG CHÁY HƠN CHỮA CHÁY",
        "subtitle": "AN TOÀN LÀ TRÊN HẾT",
        "lines": [
            "Phát hiện sớm – Xử lý kịp thời – An toàn bền vững",
            "Nhà máy Điện gió Yang Trung – Chơ Long • CLWP-QT-07",
        ],
        "type": "closing",
    },
]


# ===================== WIDGET SLIDE =====================
class SlideWidget(QScrollArea):
    def __init__(self, data: dict, index: int, total: int):
        super().__init__()
        self.data = data
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setStyleSheet("QScrollArea{border:none;background:#fff}")

        content = QWidget()
        content.setStyleSheet("background:#fff")
        self.setWidget(content)

        layout = QVBoxLayout(content)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header (trừ cover & section & closing)
        stype = data.get("type", "content")
        if stype not in ("cover", "section", "closing"):
            header = self._make_header(data, index, total)
            layout.addWidget(header)

        body = QWidget()
        body_layout = QVBoxLayout(body)
        body_layout.setContentsMargins(30, 18, 30, 18)
        body_layout.setSpacing(10)

        # Tiêu đề (nếu không phải cover/section/closing)
        if stype not in ("cover", "section", "closing"):
            title = QLabel(data.get("title", ""))
            title.setFont(QFont("Arial", 15, QFont.Weight.Bold))
            title.setStyleSheet("color:#CC0000")
            body_layout.addWidget(title)

        # Subtitle
        if "subtitle" in data:
            sub = QLabel(data["subtitle"])
            if stype in ("cover", "section", "closing"):
                sub.setFont(QFont("Arial", 22, QFont.Weight.Bold))
                sub.setStyleSheet("color:#ffd700" if stype == "cover" else "color:#fff")
                sub.setWordWrap(True)
            else:
                sub.setFont(QFont("Arial", 13))
                sub.setStyleSheet("color:#555")
            body_layout.addWidget(sub)

        # Nội dung
        for line in data.get("lines", []):
            lbl = QLabel(line)
            lbl.setWordWrap(True)
            if stype == "cover":
                lbl.setStyleSheet("color:#fff;font-size:14px")
            elif stype == "section":
                lbl.setStyleSheet("color:#fff;font-size:14px")
            elif stype == "closing":
                lbl.setStyleSheet("color:#fff;font-size:14px")
            else:
                lbl.setStyleSheet("color:#333;font-size:13px;padding:4px 0")
            body_layout.addWidget(lbl)

        if stype in ("cover", "section", "closing"):
            bg = "#800000" if stype == "cover" else ("#800020" if stype == "section" else "#CC0000")
            body.setStyleSheet(f"background:{bg}")
            # Căn giữa
            body_layout.insertStretch(0)
            body_layout.addStretch()

        layout.addWidget(body, 1)

        # Nút điều hướng & số slide
        nav = self._make_nav(index, total)
        layout.addWidget(nav)

    def _make_header(self, data, index, total):
        header = QFrame()
        header.setFixedHeight(55)
        header.setStyleSheet("background:linear-gradient(135deg,#cc0000,#990000)")
        h_layout = QVBoxLayout(header)
        h_layout.setContentsMargins(20, 4, 20, 4)

        row1 = QHBoxLayout()
        company = QLabel("CÔNG TY TNHH DV & KT NĂNG LƯỢNG PECC2\nTRUNG TÂM QLVH NHÀ MÁY ĐIỆN")
        company.setStyleSheet("color:rgba(255,255,255,.9);font-size:9px")
        row1.addWidget(company)
        row1.addStretch()
        num = QLabel(f"{index} / {total}")
        num.setStyleSheet("color:rgba(255,255,255,.65);font-size:10px")
        row1.addWidget(num)

        row2 = QHBoxLayout()
        t = QLabel(data.get("title", ""))
        t.setStyleSheet("color:#fff;font-size:13px;font-weight:700")
        row2.addWidget(t)
        row2.addStretch()

        h_layout.addLayout(row1)
        h_layout.addLayout(row2)
        return header

    def _make_nav(self, index, total):
        nav = QFrame()
        nav.setFixedHeight(45)
        nav.setStyleSheet("background:#1a1a2e")
        n_layout = QHBoxLayout(nav)
        n_layout.setContentsMargins(20, 5, 20, 5)

        prev_btn = QPushButton("◀ Trước")
        prev_btn.setStyleSheet(
            "QPushButton{background:#CC0000;color:#fff;border:none;padding:6px 16px;border-radius:6px;font-weight:600}"
            "QPushButton:hover{background:#B71C1C}"
        )
        prev_btn.clicked.connect(lambda: self.window().change_slide(-1))
        n_layout.addWidget(prev_btn)
        n_layout.addStretch()

        info = QLabel(f"Slide {index} / {total}")
        info.setStyleSheet("color:rgba(255,255,255,.7);font-size:12px")
        n_layout.addWidget(info)
        n_layout.addStretch()

        next_btn = QPushButton("Tiếp ▶")
        next_btn.setStyleSheet(
            "QPushButton{background:#CC0000;color:#fff;border:none;padding:6px 16px;border-radius:6px;font-weight:600}"
            "QPushButton:hover{background:#B71C1C}"
        )
        next_btn.clicked.connect(lambda: self.window().change_slide(1))
        n_layout.addWidget(next_btn)

        return nav


# ===================== CỬA SỔ CHÍNH =====================
class PCCCApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Đào tạo PCCC - Nhà máy Điện gió Yang Trung - Chơ Long")
        self.resize(1100, 750)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.total = len(SLIDES)
        self.current = 0

        for i, data in enumerate(SLIDES, start=1):
            self.stack.addWidget(SlideWidget(data, i, self.total))

        # Phím tắt
        QShortcut(QKeySequence(Qt.Key.Key_Right), self, lambda: self.change_slide(1))
        QShortcut(QKeySequence(Qt.Key.Key_Left), self, lambda: self.change_slide(-1))
        QShortcut(QKeySequence(Qt.Key.Key_Down), self, lambda: self.change_slide(1))
        QShortcut(QKeySequence(Qt.Key.Key_Up), self, lambda: self.change_slide(-1))

    def change_slide(self, direction: int):
        self.current = (self.current + direction) % self.total
        self.stack.setCurrentIndex(self.current)


# ===================== MAIN =====================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PCCCApp()
    window.show()
    sys.exit(app.exec())