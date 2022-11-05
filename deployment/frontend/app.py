import json
import numpy as np
import streamlit as st
from keras.utils import load_img
import requests
from keras.applications import VGG16
from PIL import Image
from streamlit_option_menu import option_menu


st.set_page_config(layout="centered", page_icon="📑", page_title="Siganture Forgery Detection")


selected = option_menu(
    menu_title=None,
    options= ["Home","Program","Registration"],
    icons=["house","robot","file-person"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    )

def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(https://www.rhbgroup.com/~/media/images/laos/about-us/our-people/profile-bg.ashx?h=745&la=en&w=480);
             background-repeat: no-repeat;
             background-size: 1250px 1120px;
             background-position: center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

# logo = Image.open(requests.get("https://icon2.cleanpng.com/20180630/gza/kisspng-universal-declaration-of-human-rights-world-confer-5b382420dcae75.6560601615304059209039.jpg",stream=True).raw).resize((430,170))
# st.image(logo)

def repeat_axis(x):
    rgb_batch = np.repeat(x[..., np.newaxis], 3, -1)
    return rgb_batch

def cosine_similarity(x,y):
    dot_product = x@y
    cos = dot_product/(np.linalg.norm(x) * np.linalg.norm(y))
    return cos

def avg_cos_similar (a,b,c,d,e,f):
    if (a == f).all() or (b == f).all() or (c == f).all() or (e == f).all() or (d == f).all() :
        avg_cos = (cosine_similarity(a,f) + cosine_similarity(b,f) + cosine_similarity(c,f) + cosine_similarity(d,f) + cosine_similarity(e,f)-1)/4        
    else:
        avg_cos = (cosine_similarity(a,f) + cosine_similarity(b,f) + cosine_similarity(c,f) + cosine_similarity(d,f) + cosine_similarity(e,f))/5
    return round(avg_cos,5)


if selected =="Home":
    st.header(" Mengapa diperlukan alat deteksi pemalsuan tanda tangan ?")
    st.write(  '''Saat ini kita telah memasuki area digital, namun masih banyak nasabah atau pelanggan yang masih menggunakan tanda tangan mereka sebagai bentuk otentikasi utama untuk berbagai transaksi. 
    Tanda tangan mereka mengesahkan cek, dokumen rekening baru, dokumen pinjaman, dan banyak lagi, dan untuk meminimalkan risiko penipuan, bank memerlukan solusi yang tepat untuk mendeteksi pemalsuan dengan cepat dan akurat.
    ''')
    st.header(" Tipe-tipe pemalsuan tanda tangan  ?")
    st.write("Ada beberapa jenis pemalsuan tanda tangan")
    st.subheader("Pemalsuan tanpa dasar")
    st.write(''' Tanda tangan palsu ini memiliki sedikit atau tidak ada kemiripan dengan tanda tangan pelanggan yang sebenarnya karena pemalsu tidak memiliki akses ke tanda tangan tersebut. 
    Misalnya, pencuri membuka akun baru menggunakan Nomor Jaminan Sosial curian yang mereka beli dari web gelap atau jika mereka menulis cek  dari buku cek curian.
    '''
    )
    st.subheader("Pemalsuan dengan dasar")
    st.write(''' Juga dikenal sebagai pemalsuan tidak terampil, pemalsuan ini dibuat dengan menelusuri tanda tangan yang sebenarnya. 
    Mereka cenderung terlihat sangat mirip dengan tanda tangan yang sebenarnya dan perbedaannya seringkali tidak terdeteksi oleh mata manusia saja. 
    Namun, mereka fokus pada akurasi daripada kelancaran.
    '''
    )
    st.subheader("Pemalsuan Profesional")
    st.write(''' Jenis pemalsuan yang paling sulit untuk dideteksi, 
    tanda tangan ini dibuat oleh penjahat yang telah menghabiskan banyak waktu berlatih dan memiliki kemampuan untuk meniru tanda tangan yang sebenarnya dengan cara yang terlihat akurat dan relatif lancar dengan mata telanjang.
    
    sumber: https://sqnbankingsystems.com/blog/how-to-improve-forgery-detection-at-your-financial-institution/   
    '''
    )

if selected =="Program":
    st.header("Handwritten Signature Forgery Detection")
    title = st.text_input('Masukan Nomor Rekening Nasabah',value="",help='masukan tanpa titik(.), koma(,), atau strip(-), seperti: 00000001',max_chars=8)
    title1= title[-3:]
    if (title ==""):
        st.write("Masukan Nomor Rekening Anda")
    else:
        try:
            image1=load_img(f"C:/Users/ASUS TUF/Documents/9. Materi Data Scientist/FTDS013/Assignment/0. dataset P2M3/Dataset_Signature_Final/Dataset/dataset2/real/{title1}01{title1}.png", color_mode='grayscale', target_size= (256,256,3))
            image2=load_img(f"C:/Users/ASUS TUF/Documents/9. Materi Data Scientist/FTDS013/Assignment/0. dataset P2M3/Dataset_Signature_Final/Dataset/dataset2/real/{title1}02{title1}.png", color_mode='grayscale', target_size= (256,256,3))
            image3=load_img(f"C:/Users/ASUS TUF/Documents/9. Materi Data Scientist/FTDS013/Assignment/0. dataset P2M3/Dataset_Signature_Final/Dataset/dataset2/real/{title1}03{title1}.png", color_mode='grayscale', target_size= (256,256,3))
            image4=load_img(f"C:/Users/ASUS TUF/Documents/9. Materi Data Scientist/FTDS013/Assignment/0. dataset P2M3/Dataset_Signature_Final/Dataset/dataset2/real/{title1}04{title1}.png", color_mode='grayscale', target_size= (256,256,3))
            image5=load_img(f"C:/Users/ASUS TUF/Documents/9. Materi Data Scientist/FTDS013/Assignment/0. dataset P2M3/Dataset_Signature_Final/Dataset/dataset2/real/{title1}05{title1}.png", color_mode='grayscale', target_size= (256,256,3))
            st.image(image1) 

        except :
            st.markdown('Belum memiki rekening? lakukan pendaftaran pada Tab **Registration** ')
            st.error('Rekening tidak ditemukan, harap masukan nomor yang valid !')
        

    uploaded_files_0 = st.file_uploader(f"Masukan tanda tangan Nasabah {title}", type=['jpg','png','jpeg']) 
    if uploaded_files_0 is not None:
        st.image(uploaded_files_0)  
        
    if st.button ('Predict'):
        uploaded_files = Image.open(uploaded_files_0).resize((256,256)).convert('L')
        uploaded_files = np.array(uploaded_files)/255   
        data           = uploaded_files[np.newaxis,...]
        data           = np.repeat(data[..., np.newaxis], 3, -1)
        model          = VGG16(include_top=False, weights='imagenet',input_shape=(256,256,3))
        new_data1       = model.predict(data)
        new_data2      = new_data1.tolist()

    # Cosine Similarity

        image1=np.array(image1)/255
        image2=np.array(image2)/255
        image3=np.array(image3)/255
        image4=np.array(image4)/255
        image5=np.array(image5)/255

        image1=image1[np.newaxis,...]
        image2=image2[np.newaxis,...]
        image3=image3[np.newaxis,...]
        image4=image4[np.newaxis,...]
        image5=image5[np.newaxis,...]

        image1=repeat_axis(image1)
        image2=repeat_axis(image2)
        image3=repeat_axis(image3)
        image4=repeat_axis(image4)
        image5=repeat_axis(image5)

        image1= model.predict(image1)
        image2= model.predict(image2)
        image3= model.predict(image3)
        image4= model.predict(image4)
        image5= model.predict(image5)

        image1=image1.reshape(-1)
        image2=image2.reshape(-1)
        image3=image3.reshape(-1)
        image4=image4.reshape(-1)
        image5=image5.reshape(-1)
        image6=new_data1.reshape(-1)

        cosin6 = avg_cos_similar(image1,image2,image3,image4,image5,image6)
        cosin1 = avg_cos_similar(image1,image2,image3,image4,image5,image1)
        cosin2 = avg_cos_similar(image1,image2,image3,image4,image5,image2)
        cosin3 = avg_cos_similar(image1,image2,image3,image4,image5,image3)
        cosin4 = avg_cos_similar(image1,image2,image3,image4,image5,image4)
        cosin5 = avg_cos_similar(image1,image2,image3,image4,image5,image5)

        if ((cosin1+cosin2+cosin3+cosin4+cosin5)/5-cosin6)>0.036:
            st.subheader("Tanda tangan yang diunggah terdeteksi tidak relevan")
            st.caption("Silahkan unggah kembali tanda tangan nasabah")
        else:
        # inference
            URL = "https://model-signature-backend.herokuapp.com/v1/models/signature_model:predict"
            param = json.dumps({
                    "signature_name":"serving_default",
                    "instances":new_data2
                    })
            r = requests.post(URL, data=param)

            if r.status_code == 200:
                res = r.json()
                if res['predictions'][0][0] > 0.5:
                    st.subheader("Tanda tangan nasabah terdeteksi palsu")
                    st.markdown("**Kode konfirmasi telah dikirimkan ke Email Anda**")
                else:
                    st.subheader("Selamat tanda tangan nasabah terdeteksi asli")
                    st.markdown("**Silahkan lanjutkan transaksi nasabah**")
            else:
                st.title("Unexpected Error")     

if selected =="Registration":
    st.title("Registrasi tanda tangan Nasabah")
    st.subheader(" Masukan data diri nasabah ")
    with st.form("form1", clear_on_submit=True):
        name = st.text_input("Nama nasabah")
        email = st.text_input("Email nasabah")
        signature1 =st.file_uploader("Unggah tanda tangan nasabah I")
        signature2 =st.file_uploader("Unggah tanda tangan nasabah II")
        signature3 =st.file_uploader("Unggah tanda tangan nasabah III")
        signature4 =st.file_uploader("Unggah tanda tangan nasabah IV")
        signature5 =st.file_uploader("Unggah tanda tangan nasabah V")

        submit=st.form_submit_button("Selesaikan registrasi")
       


