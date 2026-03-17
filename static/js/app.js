// =============================================================================
// Himanshu AI - Chatbot with Memory
// =============================================================================

document.addEventListener('DOMContentLoaded', () => {
    const chatArea = document.getElementById('chat-area');
    const fileInput = document.getElementById('file-input');
    const previewStrip = document.getElementById('preview-strip');
    const previewThumb = document.getElementById('preview-thumb');
    const btnRemove = document.getElementById('btn-remove');
    const btnSend = document.getElementById('btn-send');
    const chatInput = document.getElementById('chat-input');
    const btnNewChat = document.getElementById('btn-new-chat');

    let selectedFile = null;
    let selectedDataUrl = null;

    // ===== FILE HANDLING =====
    fileInput.addEventListener('change', e => {
        if (e.target.files.length) handleFile(e.target.files[0]);
    });

    btnRemove.addEventListener('click', clearFile);

    function handleFile(file) {
        const ok = ['image/png','image/jpeg','image/jpg','image/webp','image/gif'];
        if (!ok.includes(file.type)) { alert('Sirf image file chalegi!'); return; }
        if (file.size > 16*1024*1024) { alert('16MB se chhoti file daalo!'); return; }
        selectedFile = file;
        const r = new FileReader();
        r.onload = e => {
            selectedDataUrl = e.target.result;
            previewThumb.src = selectedDataUrl;
            previewStrip.style.display = 'block';
        };
        r.readAsDataURL(file);
    }

    function clearFile() {
        selectedFile = null; selectedDataUrl = null;
        previewStrip.style.display = 'none';
        previewThumb.src = ''; fileInput.value = '';
    }

    // ===== SEND =====
    btnSend.addEventListener('click', send);
    chatInput.addEventListener('keydown', e => {
        if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(); }
    });

    async function send() {
        const text = chatInput.value.trim();
        const file = selectedFile;
        const dataUrl = selectedDataUrl;

        if (!text && !file) return;

        // Show user message
        addUserMsg(text, dataUrl);
        chatInput.value = '';
        clearFile();

        // Typing indicator
        const typing = addTyping();

        try {
            let res;
            if (file) {
                // Image analysis (with optional text)
                const fd = new FormData();
                fd.append('image', file);
                if (text) fd.append('message', text);
                res = await fetch('/analyze', { method: 'POST', body: fd });
            } else {
                // Text chat
                res = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
            }

            removeEl(typing);

            if (!res.ok) {
                const err = await res.json();
                addBotMsg(err.error || 'Kuch gadbad ho gayi.');
                return;
            }

            const data = await res.json();

            if (data.analysis) {
                // Structured result
                addBotBubble(buildResult(data.analysis));
            } else if (data.reply) {
                // Text reply
                addBotMsg(data.reply);
            }
        } catch (err) {
            removeEl(typing);
            addBotMsg('Network error — dobara try karo.');
        }
    }

    // ===== NEW CHAT =====
    btnNewChat.addEventListener('click', async () => {
        // Clear memory on server
        try { await fetch('/clear', { method: 'POST' }); } catch(e) {}
        // Clear UI
        chatArea.innerHTML = '';
        addBotBubble('Namaste! 🙏 Naya chat shuru. Photo bhejo ya sawaal pucho!');
    });

    // ===== MESSAGE HELPERS =====
    function addUserMsg(text, imgSrc) {
        const div = document.createElement('div');
        div.className = 'message user-message';
        let inner = '';
        if (imgSrc) inner += `<img src="${imgSrc}" alt="Photo">`;
        if (text) inner += `<div class="${imgSrc ? 'user-text' : ''}">${esc(text)}</div>`;
        div.innerHTML = `<div class="msg-bubble">${inner}</div>`;
        chatArea.appendChild(div);
        scrollBottom();
    }

    function addBotMsg(text) {
        addBotBubble(renderMd(text));
    }

    function addBotBubble(html) {
        const div = document.createElement('div');
        div.className = 'message bot-message';
        div.innerHTML = `<div class="msg-avatar">🌿</div><div class="msg-bubble formatted">${html}</div>`;
        chatArea.appendChild(div);
        scrollBottom();
    }

    function addTyping() {
        const div = document.createElement('div');
        div.className = 'message typing-indicator';
        div.innerHTML = `<div class="msg-avatar">🌿</div><div class="typing-dots"><span></span><span></span><span></span></div>`;
        chatArea.appendChild(div);
        scrollBottom();
        return div;
    }

    function removeEl(el) { if (el?.parentNode) el.parentNode.removeChild(el); }
    function scrollBottom() { setTimeout(() => chatArea.scrollTop = chatArea.scrollHeight, 40); }
    function esc(s) { const d = document.createElement('div'); d.textContent = s; return d.innerHTML; }

    // Simple markdown to HTML renderer
    function renderMd(text) {
        let html = esc(text);
        // Bold: **text**
        html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        // Italic: *text*
        html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
        // Headers: ### text or ## text
        html = html.replace(/^### (.+)$/gm, '<div class="md-h3">$1</div>');
        html = html.replace(/^## (.+)$/gm, '<div class="md-h2">$1</div>');
        // Bullet points: - text or * text
        html = html.replace(/^[-*] (.+)$/gm, '<div class="md-li">▸ $1</div>');
        // Numbered list: 1. text
        html = html.replace(/^\d+\. (.+)$/gm, '<div class="md-li">$1</div>');
        // Line breaks
        html = html.replace(/\n\n/g, '<div class="md-gap"></div>');
        html = html.replace(/\n/g, '<br>');
        return html;
    }

    // ===== RESULT BUILDER =====
    function buildResult(a) {
        if (a.is_plant === false) {
            return `<div class="not-plant-box"><strong>🚫 Yeh fasal nahi hai</strong><br><span style="font-size:0.8rem;color:var(--text-2)">${a.description||'Clear photo daalo.'}</span></div>`;
        }

        let h = '<div class="result-box">';

        // Header
        const sc = {Low:'sev-low',Medium:'sev-medium',High:'sev-high',Critical:'sev-critical'};
        h += `<div class="result-head">
            <div class="result-crop"><span style="font-size:1.3rem">🌿</span><div><div class="result-crop-name">${a.crop_name||'?'}</div><div class="result-disease">${a.disease_name||''}</div></div></div>
            <span class="sev ${sc[a.severity]||'sev-medium'}">${a.severity||'Medium'}</span>
        </div>`;

        if (a.is_healthy) {
            h += `<div class="healthy-box">✅ <strong>Fasal theek hai!</strong></div>`;
        }

        const cn = parseInt(a.confidence)||50;
        h += `<div class="conf-row">Sure: <strong style="color:var(--green-400)">${a.confidence||'50%'}</strong><div class="conf-bar"><div class="conf-fill" style="width:${cn}%"></div></div></div>`;

        if (a.description) h += sec('🔍','Dikkat',`<p>${a.description}</p>`);
        if (a.causes?.length) h += sec('⚡','Karan',li(a.causes));
        if (a.symptoms?.length) h += sec('🔎','Lakshan',li(a.symptoms));
        if (a.treatment?.length) h += sec('💊','Ilaaj',li(a.treatment));
        if (a.prevention?.length) h += sec('🛡️','Bachav',li(a.prevention));
        if (a.fertilizer_recommendation) h += sec('🧪','Khaad',`<p>${a.fertilizer_recommendation}</p>`);
        if (a.soil_impact) h += sec('🌍','Mitti',`<p>${a.soil_impact}</p>`);
        if (a.additional_tips) h += sec('💡','Tip',`<p>${a.additional_tips}</p>`);

        h += '</div>';
        return h;
    }

    function sec(e,t,b) { return `<div class="info-sec"><div class="info-sec-t">${e} ${t}</div><div class="info-sec-b">${b}</div></div>`; }
    function li(arr) { return arr?.length ? '<ul>'+arr.map(i=>`<li>${i}</li>`).join('')+'</ul>' : ''; }
});
