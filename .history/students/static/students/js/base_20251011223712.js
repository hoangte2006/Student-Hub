document.addEventListener('DOMContentLoaded', function () {
  const bubble = document.getElementById('aiBubble');
  if (bubble) {
    bubble.addEventListener('click', () => {
      alert('👋 Chào Te! Em cần anh giúp gì không?');
    });
  } else {
    console.warn('Không tìm thấy phần tử #aiBubble');
  }
});

document.getElementById('aiInput').addEventListener('keydown', async (e) => {
  if (e.key === 'Enter') {
    const input = e.target.value.trim();
    if (!input) return;

    const messages = document.getElementById('aiMessages');
    messages.innerHTML += `<div><b>Em:</b> ${input}</div>`;

    // Gọi Gemini API (giả lập)
    const response = await fetch('https://api.example.com/gemini', {
      method: 'POST',
      body: JSON.stringify({ prompt: input }),
      headers: { 'Content-Type': 'application/json' }
    });
    const data = await response.json();

    messages.innerHTML += `<div><b>AI:</b> ${data.reply}</div>`;
    e.target.value = '';
  }
});
