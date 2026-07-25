<div align="center">

# 🖥️⚡ H A R D W A R E &nbsp; A I ⚡🖥️

### Your AI-Powered PC Hardware Guru — CPUs, GPUs, RAM & Everything In Between

**`Made with Streamlit`** · **`Powered by Groq`** · **`Built with LangChain`** · **`Python 3.9+`** · **`MIT Licensed`**

**Status:** 🟢 Online &nbsp;|&nbsp; **Vibe:** 🔥 Immaculate &nbsp;|&nbsp; **Hardware IQ:** 🧠 300+

</div>

---

## 🎬 What Is This Thing?

Imagine your smartest PC-building friend, except they never get tired, never say *"idk bro just Google it,"* and respond in under a second thanks to **Groq's absurdly fast LLaMA 3.1 inference**. That's this app.

Ask it about CPUs, GPUs, RAM, motherboards, PSUs, cooling, or why your PC won't POST — it'll break it down like a pro, step by step, with a UI that looks like it belongs in a sci-fi command center. 🚀

> 💬 *"Is 16GB RAM enough for gaming in 2026?"*
> 🤖 *Gets you a structured, no-fluff, expert-grade answer in seconds.*

---

## 🌈 Feature Showcase

<table>
<tr>
<td width="33%" align="center">

### 🎯
**Laser-Focused**
Hardware questions only. Ask it about pizza recipes and it'll (politely) roast you.

</td>
<td width="33%" align="center">

### ⚡
**Blazing Fast**
Groq-powered inference means answers land before you finish reading the spinner text.

</td>
<td width="33%" align="center">

### 🎨
**Cinematic UI**
Glassmorphism cards, gradient glow, hover animations — built to impress, not just function.

</td>
</tr>
<tr>
<td width="33%" align="center">

### 🧩
**Compatibility Checks**
CPU + Motherboard + PSU math, sorted.

</td>
<td width="33%" align="center">

### 🗂️
**Session Memory**
Every question you've asked, saved and revisitable in one click.

</td>
<td width="33%" align="center">

### ⚙️
**Tunable Brain**
Slide the temperature, swap the model — total control from the sidebar.

</td>
</tr>
</table>

---

## 🧰 Tech Stack

| Layer | Tech | Why |
|:--|:--|:--|
| 🖼️ UI | `Streamlit` + custom CSS | Full app in one Python file, styled like a real product |
| 🧠 LLM | `Groq` — `llama-3.1-8b-instant` | Ridiculous speed, low latency |
| 🔗 Orchestration | `LangChain` (`ChatGroq`, `ChatPromptTemplate`) | Clean prompt → model pipeline |
| 🔐 Secrets | `python-dotenv` | Keeps your API key out of the code |

---

## ⚡ Quickstart

```bash
# 1️⃣  Clone it
git clone <your-repo-url>
cd <your-repo-folder>

# 2️⃣  Install the goods
pip install streamlit python-dotenv langchain-groq langchain-core

# 3️⃣  Drop your API key in a .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# 4️⃣  Launch 🚀
streamlit run app.py
```

Then open **`http://localhost:8501`** and start interrogating your PC's specs.

---

## 🕹️ How To Use

```
┌─────────────────────────────────────────────┐
│  1. Type your hardware question              │
│  2. (Optional) tweak temperature / model     │
│  3. Smash 🚀 Ask AI                          │
│  4. Get a structured expert breakdown        │
│  5. Revisit past questions in the sidebar    │
└─────────────────────────────────────────────┘
```

Every answer follows the same battle-tested format:

1. 🧩 **Simple Explanation**
2. 🪜 **Step-by-Step Guidance**
3. ✅ **Best Practices**
4. ⚠️ **Precautions** (when it matters)

---

## 📌 Supported Topics

<div align="center">

| 🧠 CPU | 🎮 GPU | 💾 RAM | 🗄️ Storage | 🧩 Motherboard |
|:---:|:---:|:---:|:---:|:---:|
| 🔌 PSU | ❄️ Cooling | 🖥️ Monitors | ⌨️ Peripherals | 🛠️ Troubleshooting |

</div>

Anything outside this universe gets a firm but friendly:

> ⛔ *"Sorry, I only answer computer hardware-related questions."*

---

## 📁 Project Structure

```
hardware-ai-assistant/
│
├── 🐍 app.py          → The entire app — UI, styling, AI logic
├── 🔐 .env             → Your GROQ_API_KEY (never commit this!)
└── 📖 README.md        → You are here
```

---

## ⚙️ Configuration Cheat Sheet

| Setting | Default | Effect |
|:--|:--:|:--|
| `model` | `llama-3.1-8b-instant` | Which Groq model answers you |
| `temperature` | `0.3` | 🥶 Low = precise & consistent · 🔥 High = creative & varied |
| Session history | ✅ enabled | Resets on page reload (per-session only) |

---

## 🔒 Security

- 🙅 Never commit `.env` or your `GROQ_API_KEY`
- ✅ Add `.env` to `.gitignore`
- 🔁 Rotate your key immediately if it ever leaks

---

## 🧯 Troubleshooting

| 😵 Symptom | 🕵️ Cause | 🩹 Fix |
|:--|:--|:--|
| `ChatGroq` won't initialize | Missing/invalid API key | Double-check `.env` → `GROQ_API_KEY` |
| Blank / stuck response | Network or Groq API hiccup | Retry, check [Groq status](https://groqstatus.com) |
| UI looks flat / unstyled | Browser cache | Hard refresh (`Ctrl+Shift+R`) |
| "Sorry, I only answer hardware questions" on a hardware question | Prompt phrased too vaguely | Be specific — mention the component |

---

## 🗺️ Roadmap Ideas

- [ ] 🔊 Voice input for hands-free questions
- [ ] 📊 Component price comparison lookup
- [ ] 🧾 Exportable PDF build guides
- [ ] 🌗 Light/dark theme toggle

---

## 📄 License

Released under the **MIT License** — use it, remix it, ship it. Add your own `LICENSE` file if distributing publicly.

<div align="center">

### 🖥️ Built for people who take their PC builds *very* seriously.

⭐ **If this saved you a Reddit thread, consider it a win.** ⭐

</div>
