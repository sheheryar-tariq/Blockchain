
# Name: M. Sheheryar Tariq
# StudentID: 24819196

# Run using streamlit run {filepath}

import streamlit as st
import hashlib
import time


class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.ctime()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        return hashlib.sha256(content.encode()).hexdigest()


class BlockchainApp:
    def __init__(self):
        if "chain" not in st.session_state:
            st.session_state.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block 🚀", "0")

    def get_chain(self):
        return st.session_state.chain

    def add_block(self, data):
        chain = self.get_chain()
        last_block = chain[-1]
        new_block = Block(len(chain), data, last_block.hash)
        chain.append(new_block)

    def validate_chain(self):
        chain = self.get_chain()
        for i in range(1, len(chain)):
            current = chain[i]
            previous = chain[i - 1]

            if current.hash != current.calculate_hash():
                return False, f"Block {i} hash doesn't match its data!"

            if current.prev_hash != previous.hash:
                return False, f"Block {i} is not linked to Block {i-1}!"

        return True, "All blocks are valid and properly linked ✅"


app = BlockchainApp()

st.set_page_config(page_title="🧱 Simple Blockchain", layout="wide")
st.title("🧱 Blockchain Demo with Streamlit")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("➕ Add New Block")
    user_data = st.text_area("Transaction / Block Data", height=150)
    if st.button("Add Block"):
        if user_data.strip() == "":
            st.warning("Please enter some data first!")
        else:
            app.add_block(user_data)
            st.success("Block added!")

    st.header("🛡️ Validate Blockchain")
    if st.button("Run Validation Check"):
        valid, msg = app.validate_chain()
        if valid:
            st.success(msg)
        else:
            st.error(msg)

with col2:
    st.header("🔗 Blockchain Structure")
    for block in reversed(app.get_chain()):
        with st.container():
            st.markdown(
                f"""
                <div style='padding:15px;border:1px solid #444;
                            border-radius:10px;background:#000;color:#fff;
                            margin-bottom:10px'>
                <b>🧱 Block #{block.index}</b><br>
                <b>🕒 Time:</b> {block.timestamp}<br>
                <b>📦 Data:</b> {block.data}</b><br>
                <b>🔑 Hash:</b> <code style='color:#0f0'>{block.hash}</code><br>
                <b>↩️ Prev Hash:</b> <code style='color:#0ff'>{block.prev_hash}</code>
                </div>
            """,
                unsafe_allow_html=True,
            )
