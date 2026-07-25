import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


st.set_page_config(
    page_title="Computer Hardware AI Assistant",
    page_icon="🖥️",
    layout="wide"
)



with st.sidebar:
    st.title("🖥️ Hardware AI")
    st.markdown("---")

    st.subheader("📌 Supported Topics")
    st.write("• CPU")
    st.write("• GPU")
    st.write("• RAM")
    st.write("• Motherboard")
    st.write("• SSD / HDD / NVMe")
    st.write("• PSU")
    st.write("• PC Building")
    st.write("• Cooling Systems")
    st.write("• Hardware Troubleshooting")

    st.markdown("---")
    st.info("💡 Ask only computer hardware related questions.")


st.title("🖥️ Computer Hardware AI Assistant")
st.caption("Your personal assistant for PC hardware and troubleshooting.")

st.divider()



with st.container():
    st.info(
        """
        Welcome! 👋

        Ask any question related to computer hardware like:
        - Processor recommendations
        - GPU comparisons
        - RAM upgrades
        - SSD vs HDD
        - Motherboard compatibility
        - PC troubleshooting
        """
    )


question = st.text_area(
    "🔍 Enter Your Hardware Question",
    height=180,
    placeholder="Example: Is 16GB RAM enough for gaming?"
)


col1, col2 = st.columns([1, 5])

with col1:
    ask = st.button("🚀 Ask AI", use_container_width=True)

if ask:

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_template(
        """
        You are a Computer Hardware Expert.
        Your job is to answer ONLY computer hardware-related questions.

        Topics include:
        - CPU (Processor)
        - GPU (Graphics Card)
        - RAM
        - Motherboard
        - Storage (HDD, SSD, NVMe)
        - Power Supply (PSU)
        - Computer Cabinets
        - Cooling Systems
        - Monitors
        - Keyboards and Mice
        - Compatibility of Components
        - Hardware Installation
        - Hardware Troubleshooting
        - Upgrading PC Components
        - Computer Peripherals

        If the user asks anything outside computer hardware,
        reply:

        "Sorry, I only answer computer hardware-related questions."

        Question:
        {question}

        Provide:
        1. Simple Explanation
        2. Step-by-step guidance
        3. Best Practices
        4. Precautions if needed
        """
    )

    chain = prompt | llm

    
    with st.spinner("🤖 Thinking..."):
        response = chain.invoke({"question": question})

    st.divider()

    
    st.subheader("📖 AI Response")
    st.success(response.content)

st.divider()


