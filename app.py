# =============================================================================
# Himanshu AI - Crop Disease Detection + Chat Agent
# Flask + LangChain + OpenAI GPT-4o Vision + Memory
# =============================================================================

import os
import base64
import json
from flask import Flask, request, jsonify, render_template, session
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "himanshu-ai-secret-2026")
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs('uploads', exist_ok=True)

# OpenAI model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
    max_tokens=4096,
    api_key=os.getenv("OPENAI_API_KEY")
)

ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'webp', 'gif'}

# Tanda Area Soil Profile (embedded)
SOIL_SUMMARY = """
TANDA AREA MITTI KA DATA:
- Nitrogen (N): Bahut kami, 91% LOW
- Organic Carbon: Kam hai, 67% LOW  
- Potassium (K): Accha hai, 56% HIGH
- Phosphorus (P): 71% MEDIUM
- pH: 99% NEUTRAL (best for farming)
- EC: 100% Non-Saline
- Iron, Copper, Manganese, Sulfur, Zinc, Boron: Sab sufficient
MATLAB: Nitrogen aur Organic Carbon ki kami hai, baaki sab theek.
"""

SYSTEM_PROMPT = f"""Tu "Himanshu AI" hai — kisano ka apna dost aur fasal doctor.

SAKHT NIYAM:
1. Tu SIRF Hinglish mein bolega — matlab Hindi ke shabd ko English letters mein likhna hai.
2. KABHI BHI angrezi ke shabd mat use kar. Jaise "disease" mat bol, "bimari" bol. "Treatment" mat bol, "ilaaj" bol. "Soil" mat bol, "mitti" bol. "Symptoms" mat bol, "lakshan" bol. "Prevention" mat bol, "bachav" bol. "Recommendation" mat bol, "salah" bol.
3. Jawab hamesha SAAF aur SAJHA ke de — heading, bullet points, aur bold use kar jaise:
   - **Bold** heading ke liye
   - Bullet points se list bana
   - Chhote chhote para mein baat kar
4. Jab kisan TEXT mein baat kare toh formatted text mein jawab de, JSON bilkul mat de.
5. Jab kisan PHOTO bheje toh sirf tab JSON mein jawab de.
6. Dost ki tarah baat kar — seedhi, simple, choti baatein. Gaaon wala andaaz.
7. Kheti, fasal, khaad, mitti, mausam, beej — in sab pe madad kar.
8. Kheti ke bahar ka sawaal aaye toh pyaar se bol "Bhai, mujhe sirf kheti ki samajh hai."
9. Pichli saari baatein yaad rakh — conversation memory tere paas hai.
10. Har jawab mein is area ki mitti ka data dhyan mein rakh.

IS ILAKE KI MITTI KA DATA:
{SOIL_SUMMARY}
"""

IMAGE_PROMPT = """Is photo ko dekh aur bata kya dikkat hai.

Agar photo mein paudha/fasal hai toh SIRF ye JSON de (koi aur text mat likh):
{{
    "is_plant": true/false,
    "is_healthy": true/false,
    "crop_name": "fasal ka naam hinglish mein",
    "disease_name": "bimari ka naam hinglish mein (agar hai)",
    "severity": "Kam/Thodi/Zyada/Bahut Zyada",
    "confidence": "0-100%",
    "description": "2-3 line mein simple bata kya dikkat hai, hinglish mein",
    "causes": ["pehla karan", "dusra karan"],
    "symptoms": ["pehla lakshan", "dusra lakshan"],
    "treatment": ["pehla ilaaj", "dusra ilaaj"],
    "prevention": ["pehla bachav", "dusra bachav"],
    "fertilizer_recommendation": "kaunsi khaad deni chahiye — hinglish mein",
    "soil_impact": "is ilake ki mitti ki wajah se kya asar hua — hinglish mein",
    "additional_tips": "koi extra salah — hinglish mein"
}}

Agar photo mein fasal/paudha nahi hai toh:
{{"is_plant": false, "description": "bhai is photo mein koi fasal ya paudha nahi dikh raha. apni fasal ki saaf photo bhejo."}}

YAAD RAKH: Koi bhi angrezi shabd mat use kar. Sirf Hinglish mein likh."""


def allowed_file(f):
    return '.' in f and f.rsplit('.', 1)[1].lower() in ALLOWED_EXT


def get_history():
    """Get conversation history from session."""
    if 'history' not in session:
        session['history'] = []
    return session['history']


def add_to_history(role, content):
    """Add message to conversation history (keep last 20 messages)."""
    history = get_history()
    history.append({"role": role, "content": content})
    if len(history) > 20:
        history = history[-20:]
    session['history'] = history


def build_messages(extra_messages=None):
    """Build full message list with system prompt + history + new messages."""
    messages = [SystemMessage(content=SYSTEM_PROMPT)]

    # Add conversation history
    for msg in get_history():
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))

    # Add new messages
    if extra_messages:
        messages.extend(extra_messages)

    return messages


# ======================== ROUTES ========================

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """Text chat with memory."""
    data = request.get_json()
    message = data.get('message', '').strip()

    if not message:
        return jsonify({"error": "Kuch toh likho bhai!"}), 400

    # Add user message to history
    add_to_history("user", message)

    # Build messages with history
    messages = build_messages([HumanMessage(content=message)])

    try:
        response = llm.invoke(messages)
        reply = response.content.strip()

        # Add AI response to history
        add_to_history("assistant", reply)

        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": f"Error aa gaya: {str(e)}"}), 500


@app.route('/analyze', methods=['POST'])
def analyze():
    """Image analysis with memory."""
    if 'image' not in request.files:
        return jsonify({"error": "Photo daalo bhai!"}), 400

    file = request.files['image']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({"error": "Sahi image file daalo (PNG, JPG, WEBP)."}), 400

    user_text = request.form.get('message', '').strip()

    # Save temp
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        # Encode image
        with open(filepath, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")

        ext = file.filename.rsplit('.', 1)[1].lower()
        mime = {'png':'image/png','jpg':'image/jpeg','jpeg':'image/jpeg','webp':'image/webp','gif':'image/gif'}.get(ext, 'image/jpeg')

        # Add to history
        hist_text = user_text if user_text else "[Photo bheji gayi]"
        add_to_history("user", hist_text)

        # Build image message
        img_content = [
            {"type": "text", "text": IMAGE_PROMPT + (f"\n\nKisan ka sawaal: {user_text}" if user_text else "\n\nIs photo ko check karo.")},
            {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}", "detail": "high"}}
        ]

        messages = build_messages([HumanMessage(content=img_content)])
        response = llm.invoke(messages)
        raw = response.content.strip()

        # Parse JSON
        try:
            text = raw
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip()
            result = json.loads(text)

            # Add summary to history
            if result.get("disease_name"):
                add_to_history("assistant", f"Photo check ki: {result.get('crop_name','')} mein {result.get('disease_name','')} mili. Severity: {result.get('severity','')}")
            else:
                add_to_history("assistant", f"Photo check ki: {result.get('crop_name','fasal')} theek lag rahi hai.")

            return jsonify({"success": True, "analysis": result})
        except json.JSONDecodeError:
            add_to_history("assistant", raw)
            return jsonify({"reply": raw})

    except Exception as e:
        return jsonify({"error": f"Analysis mein gadbad: {str(e)}"}), 500
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)


@app.route('/clear', methods=['POST'])
def clear():
    """Clear conversation memory."""
    session.pop('history', None)
    return jsonify({"ok": True})


if __name__ == '__main__':
    print("=" * 50)
    print("  Himanshu AI - Crop Disease Chat Agent")
    print("=" * 50)
    api_status = "SET" if os.getenv("OPENAI_API_KEY") and os.getenv("OPENAI_API_KEY") != "your_openai_api_key_here" else "NOT SET"
    print(f"  OpenAI API Key: {api_status}")
    print(f"  Server: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
