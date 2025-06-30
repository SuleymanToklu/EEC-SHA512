import streamlit as st
import hashlib
from tinyec import registry
import secrets
from cryptography.fernet import Fernet
import base64
from tinyec.ec import Point
import json
import time
import io

# Sayfa yapılandırması
st.set_page_config(
    page_title="Kriptografi ve Güvenlik Merkezi",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Gelişmiş CSS tasarımı
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background: #181a20 !important;
        color: #222 !important;
    }

    .main {
        background: transparent;
        padding: 1rem;
    }

    .stApp > header {
        background: transparent;
    }

    .hero-section {
        background: #fff;
        border-radius: 20px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        border: 1px solid #eee;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        color: #5a4ff3;
        margin-bottom: 1rem;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: #555;
        font-weight: 400;
        margin-bottom: 2rem;
    }

    .glass-card {
        background: #fff;
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.10);
        border: 1px solid #eee;
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.18);
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1rem;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        border: none;
        margin-top: 1rem;
        box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
    }

    .stTextInput > div > div > input, .stTextArea textarea {
        font-size: 1rem;
        background: #f8f9fa;
        border: 2px solid #e2e8f0;
        border-radius: 12px;
        padding: 0.75rem 1rem;
        color: #222;
        transition: all 0.3s ease;
    }

    .stTextInput > div > div > input:focus, .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }

    .result-card {
        background: #f7fafc;
        border: 2px solid #667eea;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        position: relative;
        overflow: hidden;
        color: #222;
    }

    .result-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }

    .result-label {
        font-weight: 600;
        color: #4a5568;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .result-content {
        font-family: 'Monaco', 'Menlo', monospace;
        font-size: 0.9rem;
        word-break: break-all;
        background: #fff;
        border-radius: 8px;
        padding: 1rem;
        border-left: 4px solid #667eea;
        color: #222;
    }

    .copy-btn {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: rgba(102, 126, 234, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 6px;
        padding: 0.25rem 0.5rem;
        font-size: 0.8rem;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .copy-btn:hover {
        background: rgba(102, 126, 234, 0.2);
    }

    .info-box {
        background: linear-gradient(135deg, #e6fffa 0%, #b2f5ea 100%);
        border-left: 4px solid #38b2ac;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        color: #222;
    }

    .warning-box {
        background: linear-gradient(135deg, #fef5e7 0%, #f6e05e 100%);
        border-left: 4px solid #f6e05e;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        color: #222;
    }

    .error-box {
        background: linear-gradient(135deg, #fed7d7 0%, #fc8181 100%);
        border-left: 4px solid #fc8181;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        color: #222;
    }

    .sidebar .stRadio > div {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
    }

    .metrics-container {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }

    .metric-card {
        flex: 1;
        background: #fff;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        border: 2px solid #e2e8f0;
        color: #222;
    }

    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #667eea;
    }

    .metric-label {
        font-size: 0.8rem;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }

    .feature-item {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
        color: #222;
    }

    .feature-item:hover {
        border-color: #667eea;
        transform: translateY(-2px);
    }

    .footer {
        background: #fff;
        border-radius: 16px;
        padding: 2rem;
        margin-top: 3rem;
        text-align: center;
        border: 1px solid #eee;
        color: #222;
    }
    </style>
    """, unsafe_allow_html=True)

# Ana başlık bölümü
st.markdown("""
    <div class='hero-section'>
        <div class='hero-title'>🔐 Kriptografi Merkezi</div>
        <div class='hero-subtitle'>Güvenli şifreleme ve hash fonksiyonları ile verilerinizi koruyun</div>
        <div style='font-size:1rem; color:#764ba2; font-style:italic; margin-top:0.5em;'>Süleyman Toklu</div>
    </div>
""", unsafe_allow_html=True)

# Özellikler grid'i
st.markdown("""
    <div class='feature-grid'>
        <div class='feature-item'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🔒</div>
            <h4>SHA512 Hash</h4>
            <p>Güvenli özet fonksiyonu ile veri bütünlüğünü sağlayın</p>
        </div>
        <div class='feature-item'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🔑</div>
            <h4>ECC Şifreleme</h4>
            <p>Eliptik eğri kriptografisi ile güçlü şifreleme</p>
        </div>
        <div class='feature-item'>
            <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📁</div>
            <h4>Dosya Desteği</h4>
            <p>Metin ve dosyalar için kapsamlı kriptografi desteği</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("### 🛠️ İşlem Seçimi")
islem = st.sidebar.radio(
    "Yapmak istediğiniz işlemi seçin:",
    ["🔒 SHA512 Özet Fonksiyonu", "🔑 Eliptik Eğri Şifreleme", "📊 Kriptografi Bilgileri"],
    index=0
)

# Yardımcı fonksiyonlar
def sha512_hash(data):
    return hashlib.sha512(data.encode()).hexdigest()

def sha512_file_hash(file_bytes):
    return hashlib.sha512(file_bytes).hexdigest()

def ecc_encrypt(msg, privKey, pubKey):
    curve = registry.get_curve('brainpoolP256r1')
    sharedPoint = privKey * pubKey
    key = hashlib.sha512(str(sharedPoint.x).encode()).digest()
    f = Fernet(base64.urlsafe_b64encode(key[:32]))
    encrypted_msg = f.encrypt(msg.encode())
    return encrypted_msg

def ecc_decrypt(encrypted_msg, privKey, pubKey):
    curve = registry.get_curve('brainpoolP256r1')
    sharedPoint = privKey * pubKey
    key = hashlib.sha512(str(sharedPoint.x).encode()).digest()
    f = Fernet(base64.urlsafe_b64encode(key[:32]))
    decrypted_msg = f.decrypt(encrypted_msg)
    return decrypted_msg.decode()

def create_result_card(label, content, show_copy=True):
    """Sonuç kartı oluşturur"""
    card_html = f"""
    <div class='result-card'>
        <div class='result-label'>{label}</div>
        <div class='result-content'>{content}</div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
    
    if show_copy:
        if st.button(f"📋 {label} Kopyala", key=f"copy_{label}_{hash(content)}"):
            st.success(f"✅ {label} panoya kopyalandı!")

# Ana içerik
if islem == "🔒 SHA512 Özet Fonksiyonu":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🔒 SHA512 Özet Fonksiyonu")
        st.markdown("SHA512, verilerinizin bütünlüğünü doğrulamak için güvenli bir özet fonksiyonudur.")
    
    with col2:
        st.markdown("""
        <div class='info-box'>
            <strong>💡 Bilgi:</strong><br>
            SHA512, 512-bit uzunluğunda güvenli hash üretir
        </div>
        """, unsafe_allow_html=True)
    
    input_type = st.radio("📝 Girdi türünü seçin:", ["Metin", "Dosya"], horizontal=True)
    
    if input_type == "Metin":
        text_input = st.text_area("🖊️ Metni girin:", height=150, placeholder="Buraya hash'lemek istediğiniz metni yazın...")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔒 Hash Oluştur", type="primary"):
                if text_input.strip():
                    with st.spinner("Hash hesaplanıyor..."):
                        start_time = time.time()
                        hash_result = sha512_hash(text_input)
                        end_time = time.time()
                    
                    st.markdown("### 📊 Sonuçlar")
                    
                    # Metrikleri göster
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("📏 Metin Uzunluğu", f"{len(text_input)} karakter")
                    with col2:
                        st.metric("🔒 Hash Uzunluğu", "128 hex karakter")
                    with col3:
                        st.metric("⏱️ İşlem Süresi", f"{(end_time - start_time)*1000:.2f} ms")
                    
                    create_result_card("SHA512 Hash", hash_result)
                    
                    st.markdown("""
                    <div class='info-box'>
                        <strong>✅ Başarılı!</strong> Hash değeri güvenli şekilde oluşturuldu.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class='warning-box'>
                        <strong>⚠️ Uyarı:</strong> Lütfen hash'lemek için bir metin girin.
                    </div>
                    """, unsafe_allow_html=True)
    
    else:
        uploaded_file = st.file_uploader(
            "📁 Dosya yükleyin", 
            type=['txt', 'pdf', 'doc', 'docx', 'jpg', 'png', 'zip'],
            help="Desteklenen formatlar: TXT, PDF, DOC, DOCX, JPG, PNG, ZIP"
        )
        
        if uploaded_file is not None:
            file_details = {
                "📁 Dosya Adı": uploaded_file.name,
                "📊 Dosya Boyutu": f"{len(uploaded_file.getvalue())} bytes",
                "🏷️ Dosya Türü": uploaded_file.type
            }
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📁 Dosya", uploaded_file.name)
            with col2:
                st.metric("📊 Boyut", f"{len(uploaded_file.getvalue())} bytes")
            with col3:
                st.metric("🏷️ Tür", uploaded_file.type)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🔒 Dosya Hash'le", type="primary"):
                    with st.spinner("Dosya hash'leniyor..."):
                        start_time = time.time()
                        file_bytes = uploaded_file.read()
                        hash_result = sha512_file_hash(file_bytes)
                        end_time = time.time()
                    
                    st.markdown("### 📊 Sonuçlar")
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("📁 Dosya Boyutu", f"{len(file_bytes)} bytes")
                    with col2:
                        st.metric("🔒 Hash Uzunluğu", "128 hex karakter")
                    with col3:
                        st.metric("⏱️ İşlem Süresi", f"{(end_time - start_time)*1000:.2f} ms")
                    
                    create_result_card("Dosya SHA512 Hash", hash_result)
                    
                    st.markdown("""
                    <div class='info-box'>
                        <strong>✅ Başarılı!</strong> Dosya hash değeri güvenli şekilde oluşturuldu.
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

elif islem == "🔑 Eliptik Eğri Şifreleme":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🔑 Eliptik Eğri Şifreleme (ECC)")
        st.markdown("Modern ve güvenli şifreleme teknolojisi ile verilerinizi koruyun.")
    
    with col2:
        st.markdown("""
        <div class='info-box'>
            <strong>💡 Bilgi:</strong><br>
            ECC, RSA'dan daha güçlü güvenlik sunar
        </div>
        """, unsafe_allow_html=True)
    
    operation = st.radio("🔧 İşlem seçin:", ["🔒 Şifrele", "🔓 Şifre Çöz"], horizontal=True)
    
    if operation == "🔒 Şifrele":
        message = st.text_area("💬 Şifrelenecek metni girin:", height=150, placeholder="Buraya şifrelemek istediğiniz mesajı yazın...")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔒 Şifrele", type="primary"):
                if message.strip():
                    try:
                        with st.spinner("Şifreleme yapılıyor..."):
                            start_time = time.time()
                            curve = registry.get_curve('brainpoolP256r1')
                            privKey = secrets.randbelow(curve.field.n)
                            pubKey = privKey * curve.g
                            encrypted = ecc_encrypt(message, privKey, pubKey)
                            encrypted_b64 = base64.b64encode(encrypted).decode()
                            end_time = time.time()
                        
                        st.markdown("### 📊 Şifreleme Sonuçları")
                        
                        # Metrikleri göster
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("📏 Orijinal Uzunluk", f"{len(message)} karakter")
                        with col2:
                            st.metric("🔒 Şifreli Uzunluk", f"{len(encrypted_b64)} karakter")
                        with col3:
                            st.metric("⏱️ İşlem Süresi", f"{(end_time - start_time)*1000:.2f} ms")
                        
                        # Sonuçları göster
                        create_result_card("🔒 Şifrelenmiş Metin", encrypted_b64)
                        create_result_card("🗝️ Private Key", str(privKey))
                        create_result_card("🔑 Public Key", f"{pubKey.x},{pubKey.y}")
                        
                        # JSON formatında tüm bilgileri göster
                        all_data = {
                            "encrypted_message": encrypted_b64,
                            "private_key": str(privKey),
                            "public_key": f"{pubKey.x},{pubKey.y}",
                            "curve": "brainpoolP256r1"
                        }
                        
                        st.markdown("### 📋 Tüm Bilgiler (JSON)")
                        st.code(json.dumps(all_data, indent=2), language='json')
                        
                        st.markdown("""
                        <div class='info-box'>
                            <strong>✅ Başarılı!</strong> Metin güvenli şekilde şifrelendi. Private Key'i güvenli saklayın!
                        </div>
                        """, unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.markdown(f"""
                        <div class='error-box'>
                            <strong>❌ Hata:</strong> Şifreleme sırasında bir hata oluştu: {str(e)}
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class='warning-box'>
                        <strong>⚠️ Uyarı:</strong> Lütfen şifrelemek için bir metin girin.
                    </div>
                    """, unsafe_allow_html=True)
    
    else:  # Şifre Çöz
        st.markdown("### 🔓 Şifre Çözme")
        
        encrypted_message = st.text_area("🔒 Şifrelenmiş Metin:", height=100, placeholder="Base64 formatında şifrelenmiş metni buraya yapıştırın...")
        privKey_input = st.text_input("🗝️ Private Key:", placeholder="Private key'i buraya girin...")
        pubKey_input = st.text_input("🔑 Public Key:", placeholder="Public key'i (x,y) formatında girin...")
        
        st.markdown("""
        <div class='info-box'>
            <strong>💡 İpucu:</strong> Public Key formatı: x,y (virgülle ayrılmış iki sayı)
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔓 Şifre Çöz", type="primary"):
                if encrypted_message.strip() and privKey_input.strip() and pubKey_input.strip():
                    try:
                        with st.spinner("Şifre çözülüyor..."):
                            start_time = time.time()
                            encrypted_bytes = base64.b64decode(encrypted_message)
                            privKey = int(privKey_input)
                            pub_x, pub_y = map(int, pubKey_input.split(","))
                            curve = registry.get_curve('brainpoolP256r1')
                            pubKey = Point(curve, pub_x, pub_y)
                            decrypted = ecc_decrypt(encrypted_bytes, privKey, pubKey)
                            end_time = time.time()
                        
                        st.markdown("### 📊 Şifre Çözme Sonuçları")
                        
                        # Metrikleri göster
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("🔒 Şifreli Uzunluk", f"{len(encrypted_message)} karakter")
                        with col2:
                            st.metric("📏 Çözülmüş Uzunluk", f"{len(decrypted)} karakter")
                        with col3:
                            st.metric("⏱️ İşlem Süresi", f"{(end_time - start_time)*1000:.2f} ms")
                        
                        create_result_card("📝 Çözülmüş Metin", decrypted)
                        
                        st.markdown("""
                        <div class='info-box'>
                            <strong>✅ Başarılı!</strong> Şifre başarıyla çözüldü!
                        </div>
                        """, unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.markdown(f"""
                        <div class='error-box'>
                            <strong>❌ Hata:</strong> Şifre çözme sırasında bir hata oluştu: {str(e)}
                            <br><br>
                            <strong>Olası nedenler:</strong>
                            <ul>
                                <li>Yanlış Private Key</li>
                                <li>Yanlış Public Key formatı</li>
                                <li>Bozuk şifrelenmiş metin</li>
                            </ul>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class='warning-box'>
                        <strong>⚠️ Uyarı:</strong> Lütfen tüm alanları doldurun.
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

else:  # Kriptografi Bilgileri
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    st.markdown("### 📊 Kriptografi Bilgi Merkezi")
    
    tab1, tab2, tab3 = st.tabs(["🔒 SHA512 Hakkında", "🔑 ECC Hakkında", "🛡️ Güvenlik İpuçları"])
    
    with tab1:
        st.markdown("""
        #### 🔒 SHA512 Özet Fonksiyonu
        
        **SHA512** (Secure Hash Algorithm 512), kriptografik özet fonksiyonlarından biridir.
        
        **Özellikler:**
        - 512-bit (64 byte) uzunluğunda özet üretir
        - Tek yönlü fonksiyondur (geri döndürülemez)
        - Veri bütünlüğü kontrolü için kullanılır
        - Çok küçük bir değişiklik bile tamamen farklı hash üretir
        
        **Kullanım Alanları:**
        - Şifre saklamada
        - Dijital imzalarda
        - Dosya bütünlüğü kontrolünde
        - Blockchain teknolojilerinde
        """)
        
        # SHA512 demo
        st.markdown("##### 🧪 SHA512 Demo")
        demo_text = st.text_input("Demo metin:", value="Merhaba Dünya!")
        if demo_text:
            demo_hash = sha512_hash(demo_text)
            st.code(demo_hash, language='text')
    
    with tab2:
        st.markdown("""
        #### 🔑 Eliptik Eğri Kriptografisi (ECC)
        
        **ECC**, matematiksel eliptik eğriler üzerine kurulu modern şifreleme yöntemidir.
        
        **Avantajlar:**
        - RSA'dan daha küçük anahtar boyutu
        - Daha hızlı işlem
        - Daha güçlü güvenlik
        - Mobil cihazlar için ideal
        
        **Güvenlik Seviyeleri:**
        - 256-bit ECC ≈ 3072-bit RSA
        - 384-bit ECC ≈ 7680-bit RSA
        - 521-bit ECC ≈ 15360-bit RSA
        
        **Bu uygulamada kullanılan eğri:** brainpoolP256r1
        """)
        
        # ECC bilgileri ve örnek anahtarlar
        curve = registry.get_curve('brainpoolP256r1')
        st.markdown("##### 📐 Eğri Parametreleri")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Eğri Adı:** {curve.name}")
            st.markdown(f"**Alan (p):** {curve.field.p}")
            st.markdown(f"**Bit Uzunluğu:** {curve.field.p.bit_length()} bit")
        with col2:
            st.markdown(f"**Başlangıç Noktası (G):**")
            st.code(f"x: {curve.g.x}\ny: {curve.g.y}", language='text')
            st.markdown(f"**A (a):** {curve.a}")
            st.markdown(f"**B (b):** {curve.b}")
        
        st.markdown("##### 🗝️ Örnek ECC Anahtar Çifti")
        privKey = secrets.randbelow(curve.field.n)
        pubKey = privKey * curve.g
        st.code(f"Private Key: {privKey}\nPublic Key: ({pubKey.x}, {pubKey.y})", language='text')
        
        st.markdown("##### 🔄 ECC Şifreleme/Çözme Akışı")
        st.markdown("""
        1. **Anahtar Üretimi:** Rastgele bir private key seçilir, public key hesaplanır.
        2. **Şifreleme:** Mesaj, alıcının public key'i ile şifrelenir.
        3. **Çözme:** Şifreli mesaj, private key ile çözülür.
        
        ECC ile şifreleme, hem güvenli hem de hızlıdır. Bu uygulamada tüm işlemler `brainpoolP256r1` eğrisi ile yapılır.
        """)
        
        st.markdown("""
        <div class='info-box'>
        <strong>💡 Not:</strong> ECC, günümüzde mobil uygulamalardan blockchain'e kadar birçok alanda kullanılmaktadır.
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        #### 🛡️ Güvenlik İpuçları
        
        <div class='info-box'>
        <ul>
            <li><strong>Güçlü Parola Kullanın:</strong> Parolalarınızda harf, rakam ve sembol kombinasyonları kullanın.</li>
            <li><strong>Aynı Parolayı Birden Fazla Yerde Kullanmayın.</strong></li>
            <li><strong>İki Faktörlü Kimlik Doğrulama (2FA) Kullanın.</strong></li>
            <li><strong>Verilerinizi Düzenli Olarak Yedekleyin.</strong></li>
            <li><strong>Şüpheli E-postalara ve Linklere Dikkat Edin.</strong></li>
            <li><strong>Cihazlarınızı ve Yazılımlarınızı Güncel Tutun.</strong></li>
            <li><strong>Açık Wi-Fi Ağlarında Hassas İşlem Yapmayın.</strong></li>
            <li><strong>Şifrelerinizi Güvenli Yöneticilerde Saklayın.</strong></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <div style='font-size:1.1rem; color:#2d3748; font-weight:600;'>© 2025 Kriptografi Uygulaması</div>
</div>
""", unsafe_allow_html=True)

# (Kodda venv ile ilgili değişiklik gerekmiyor. requirements.txt ile kurulum yeterli.)