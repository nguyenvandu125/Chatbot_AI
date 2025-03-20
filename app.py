import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Tải API key từ file .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Giao diện Streamlit
st.title("Chatbot AI")
st.write("Hãy nhập câu hỏi của bạn vào bên dưới!")

# Khởi tạo lịch sử chat
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Hiển thị lịch sử chat
for msg in st.session_state["messages"]:
    role = "Bạn" if msg["role"] == "user" else "Chatbot"
    st.markdown(f"**{role}:** {msg['content']}")

# Ô nhập liệu để người dùng nhập câu hỏi
user_input = st.text_input("Nhập tin nhắn:")

if st.button("Gửi"):
    if user_input:
        # Thêm tin nhắn của người dùng vào lịch sử
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Gọi OpenAI API để lấy phản hồi
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state["messages"]
        )

        chatbot_response = response["choices"][0]["message"]["content"]

        # Thêm phản hồi của chatbot vào lịch sử
        st.session_state["messages"].append({"role": "assistant", "content": chatbot_response})

        # Cập nhật giao diện
        st.experimental_rerun()
